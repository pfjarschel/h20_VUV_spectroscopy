# -*- coding: utf-8 -*-

"""
Created on Mon Sep 26 14:59:19 2022

@author: pfjarschel
"""

import sys, time, os.path
import json, h5py, ctypes
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5 import uic
from PyQt5.QtCore import Qt, QTimer, QDir
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QSpinBox, QDoubleSpinBox, QCheckBox, QRadioButton, QMessageBox
from PyQt5.QtGui import QIcon

# from h20uvl import H20UVL
from Horiba_JY_LVPort import HoribaJYMono
from mdo3034 import MDO3034

FormUI, WindowUI = uic.loadUiType("MainWindow.ui")


class MainWindow(FormUI, WindowUI):

    def __init__(self):
        super(MainWindow, self).__init__()
        
        # Variables
        self.timeout = 10.00
        self.settingsfile = "last_settings.json"
        self.fullpath = str(__file__)
        self.lastdir = QDir.homePath()
        self.inited = False
        
        # Measurement vars
        self.begin_wait = 1.0
        self.points = 100
        self.oscpoints = 1001
        self.wlsArray = np.zeros([self.points])
        self.rawdataArray = np.zeros([self.points, self.oscpoints])
        self.results = np.zeros([self.points])
        self.dbresults = np.zeros([self.points])
        self.sweepcount = 0
        self.sweeping = False
        self.sweep_t0 = time.time()
      
        # Set up
        self.setupUi(self)
        self.setupOtherUi()
        self.SetupActions()
        self.show()
        resizeEvent = self.OnWindowResize
        self.setWindowIcon(QIcon("spectrum.ico"))

        # Devices
        self.osc = MDO3034()
        self.mono = self.mono = HoribaJYMono()
        QTimer.singleShot(100, Qt.CoarseTimer, self.InitializeDevices)
        self.loadSettings()
        self.UpdateGraph()
        self.StartMonitor()

    def OnWindowResize(self, event):
        pass

    def setupOtherUi(self):
        self.statusbar.showMessage(f"Initializing...")
        self.OnStartStopChanged()

        self.figure = plt.figure()
        self.graph = FigureCanvas(self.figure)
        self.graphToolbar = NavigationToolbar(self.graph, self)
        self.graphHolder.addWidget(self.graphToolbar)
        self.graphHolder.addWidget(self.graph)
        self.graph_ax = self.figure.add_subplot()
        self.graph_line, = self.graph_ax.plot(self.wlsArray, self.results)
        self.graph_ax.set_xlabel("Wavelength (nm)")
        self.graph_ax.set_ylabel("Power (mW)")
        self.graph_ax.set_title("Spectrum")
        self.graph_ax.grid(True)
        self.graph.draw()

    def SetupActions(self):
        # Buttons and etc
        self.runBut.clicked.connect(self.Run)
        self.stopBut.clicked.connect(self.Stop)
        self.startSpin.valueChanged.connect(self.OnStartStopChanged)
        self.stopSpin.valueChanged.connect(self.OnStartStopChanged)
        self.stepSpin.valueChanged.connect(self.OnStartStopChanged)
        self.wlSpin.valueChanged.connect(self.OnWlChanged)
        self.gratingCombo.currentIndexChanged.connect(self.OnGratingChanged)
        self.linRadio.clicked.connect(self.OnChangeScale)
        self.dbRadio.clicked.connect(self.OnChangeScale)
        self.oscscaleSpin.valueChanged.connect(self.OnTimeScaleChanged)
        
        self.actionSave_config.triggered.connect(self.OnSaveSettings)
        self.actionLoad_config.triggered.connect(self.OnLoadSettings)
        self.actionSave_final_results.triggered.connect(self.OnSaveResults)
        self.actionSave_raw_data.triggered.connect(self.OnSaveData)
        self.actionExit.triggered.connect(self.Exit)
        self.actionAbout.triggered.connect(self.About)

        # Timers
        self.measTimer = QTimer()
        self.measTimer.timeout.connect(self.measLoop)
        self.measTimer.setInterval(1000)
        
        self.monitorTimer = QTimer()
        self.monitorTimer.timeout.connect(self.monitorLoop)
        self.monitorTimer.setInterval(100)

    def InitializeDevices(self):
        self.statusbar.showMessage(f"Initializing...")
        error_text = ""

        self.osc = MDO3034()
        # self.osc.simulate = True
        osc_ok = self.osc.Initialize()
        if osc_ok:
            tscale = 1000*self.osc.GetTimeScale()
            self.oscscaleSpin.setValue(tscale)
        else:
            error_text += ("Error communicating with the MDO3034 oscilloscope! " + 
                           "Check if it is connected to a USB port and succesfully detected by the computer!\n\n")
        
        self.mono = HoribaJYMono()
        mono_ok = self.mono.Initialize()
        if mono_ok:
            grats = self.mono.GetGratings()
            currGrating = self.mono.GetCurrentGratingTurret()
            for grat in grats:
                self.gratingCombo.addItem(f"{grat.id}: {grat.lines} l/mm, blaze {grat.blaze}, {grat.description}")
            self.gratingCombo.setCurrentIndex(currGrating)
        else:
            error_text += ("Error while initializing Monochromator! " + 
                           "Check if Horiba software is properly installed and configured! " + 
                           "Additionally, the Python console output can offer more detailed information.\n\n")
        
        # Devices status
        if len(error_text) > 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Errors found while initializing devices:")
            msg.setInformativeText(error_text)
            msg.setWindowTitle("Error")
            msg.exec_()
        
        statusmsg = ""
        if self.osc.oscOK and self.mono.monoOK:
            statusmsg = "Devices OK!"
        else:
            
            if self.osc.oscOK:
                statusmsg += "Oscilloscope OK! "
            else:
                statusmsg += "Oscilloscope ERROR! "
            if self.mono.monoOK:
                statusmsg += "Monochromator OK! "
            else:
                statusmsg += "Monochromator ERROR! "
        self.statusbar.showMessage(statusmsg)
        self.inited = True
        
    def StartMonitor(self):
        self.monitorTimer.start()
    
    def monitorLoop(self):
        if self.inited:
            #datax, datay = self.osc.GetData(self.oscchanSpin.value())
            #val = np.mean(datay)
            val = self.osc.GetMean(self.oscchanSpin.value())
            self.oscInd.setText(f"{val*1000:.3f} mV".rjust(10))

            wl = self.mono.GetCurrentWavelength()
            self.wavInd.setText(f"{wl:.3f} nm".rjust(10))
        
    def Run(self):
        if not self.sweeping and self.inited:
            self.statusbar.showMessage(f"Preparing sweep...")
            
            self.monitorTimer.stop()
            if self.startSpin.value() < self.stopSpin.value():
                self.wlsArray = np.arange(self.startSpin.value(), self.stopSpin.value() + self.stepSpin.value(), self.stepSpin.value())
            else:
                self.wlsArray = np.arange(self.startSpin.value(), self.stopSpin.value() + self.stepSpin.value(), -1*self.stepSpin.value())
            self.points = len(self.wlsArray)
            self.results = np.zeros([self.points])
            self.dbresults = np.zeros([self.points])
            self.oscpoints = self.osc.GetTraceLength()
            self.rawdataArray = np.zeros([self.points, self.oscpoints])
            self.mono.SetWavelength(self.startSpin.value())
            self.sweeping = True
            
            self.UpdateGraph()
            
            time.sleep(self.begin_wait)
            self.sweepcount = 0
            self.measTimer.setInterval(int(self.stepintSpin.value()*1000))
            self.measTimer.start()
            self.sweep_t0 = time.time()

    def measLoop(self):
        if self.sweeping and self.inited:
            #thisdatax, thisdatay = self.osc.GetData(self.oscchanSpin.value())
            #thisvalue = np.mean(thisdatay)
            thisvalue = self.osc.GetMean(self.oscchanSpin.value()) 
            calval = thisvalue/self.calSpin.value()    
            if calval > 0.0:
                self.dbresults[self.sweepcount] = 10.0*np.log10(calval)
            else:
                self.dbresults[self.sweepcount] = -200
            self.results[self.sweepcount] = calval
            # self.rawdataArray[self.sweepcount] = thisdatay            
            
            self.oscInd.setText(f"{thisvalue*1000:.3f} mV".rjust(10))
            self.UpdateGraph()

            self.sweepcount += 1
            percent = 100*self.sweepcount/self.points
            etr = (100 - percent)*(time.time() - self.sweep_t0)/percent
            self.statusbar.showMessage(f"Sweep running... {percent:.2f}% complete. ETR: {etr:.2f} s")
            if self.sweepcount >= self.points:
                self.Stop()
            else:
                self.mono.SetWavelength(self.wlsArray[self.sweepcount])
                # self.wlSpin.setValue(self.wlsArray[self.sweepcount])
                self.wavInd.setText(f"{self.wlsArray[self.sweepcount]:.3f} nm".rjust(10))
            
    def Stop(self):
        if self.sweeping and self.inited:
            self.sweeping = False
            self.measTimer.stop()
            self.monitorTimer.start()
            self.statusbar.showMessage(f"Sweep stopped")
            
    def UpdateGraph(self):
        self.graph_line.set_xdata(self.wlsArray)
        if self.dbRadio.isChecked():
            self.graph_ax.set_ylabel("Power (dBm)")
            self.graph_line.set_ydata(self.dbresults)
        elif self.linRadio.isChecked():
            self.graph_ax.set_ylabel("Power (mW)")
            self.graph_line.set_ydata(self.results)
         
        self.graph_ax.relim()
        self.graph_ax.autoscale_view(True,True,True)
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()
        
    def OnStartStopChanged(self):
        points = np.abs((self.startSpin.value() - self.stopSpin.value())/self.stepSpin.value()) + 1
        self.pointsInd.setText(f"{points:.0f} sweep points")
        self.statusbar.showMessage(f"Sweep conditions updated")
        
    def OnWlChanged(self):
        if self.inited and not self.sweeping:
            self.statusbar.showMessage(f"Current wavelength changed")
            self.mono.SetWavelength(self.wlSpin.value())

    def OnGratingChanged(self):
        if self.inited and not self.sweeping:
            self.statusbar.showMessage(f"Current grating changed")
            self.mono.SetCurrentGratingTurret(self.gratingCombo.currentIndex())
            
    def OnChangeScale(self):            
        self.UpdateGraph()
        self.statusbar.showMessage(f"Scale changed")

    def OnTimeScaleChanged(self):
        self.osc.SetTimeScale(self.oscscaleSpin.value()/1000.0)
        
    def OnSaveSettings(self):
        file = QFileDialog.getSaveFileName(self, "Save settings", self.lastdir, "json files (*.json)")
        filename = file[0]
        
        lastslash = filename.rfind("/")
        self.lastdir = filename[:lastslash + 1]
       
        self.saveSettings(filename)
        
        self.statusbar.showMessage(f"Settings saved")
    
    def OnLoadSettings(self):
        file = QFileDialog.getOpenFileName(self, "Load settings", self.lastdir, "json files (*.json)")
        filename = file[0]
        
        lastslash = filename.rfind("/")
        self.lastdir = filename[:lastslash + 1]
        
        self.loadSettings(filename)
        
        self.statusbar.showMessage(f"Settings loaded")
    
    def OnSaveResults(self):
        file = QFileDialog.getSaveFileName(self, "Save results", self.lastdir, "Data files (*.txt *.csv *.dat *.hdf5)")
        filename = file[0]
        
        lastslash = filename.rfind("/")
        self.lastdir = filename[:lastslash + 1]
       
        if filename[-5:] == ".hdf5":
            with h5py.File(filename, 'w') as f:
                f.create_dataset("Wavelength (nm)", data=self.wlsArray)
                f.create_dataset("Power (mW)", data=self.results)
                f.create_dataset("Power (dBm)", data=self.dbresults)
                f.close()
                self.statusbar.showMessage(f"Results saved")
        elif filename[-4:] == ".csv":
            with open(filename, 'w') as f:
                f.write("Wavelength (nm),Power (mW),Power (dBm)\n")
                for i in range(self.points):
                    f.write(f"{self.wlsArray[i]:.3f},{self.results[i]:.6f},{self.dbresults[i]:.6f}\n")
                f.close()
                self.statusbar.showMessage(f"Results saved")
        elif len(filename) > 0:
            with open(filename, 'w') as f:
                f.write("Wavelength (nm),Power (mW),Power (dBm)\n")
                for i in range(self.points):
                    f.write(f"{self.wlsArray[i]:.3f},{self.results[i]:.6f},{self.dbresults[i]:.6f}\n")
                f.close()
                self.statusbar.showMessage(f"Results saved")
    
    def OnSaveData(self):
        file = QFileDialog.getSaveFileName(self, "Save raw data", self.lastdir, "Data files (*.txt *.csv *.dat *.hdf5)")
        filename = file[0]
        
        lastslash = filename.rfind("/")
        self.lastdir = filename[:lastslash + 1]
       
        if filename[-5:] == ".hdf5":
            with h5py.File(filename, 'w') as f:
                f.create_dataset("Wavelength (nm)", data=self.wlsArray)
                f.create_dataset("Raw data", data=self.rawdataArray)
                f.close()
                self.statusbar.showMessage(f"Raw data saved")
        elif filename[-4:] == ".csv":
            with open(filename, 'w') as f:
                for i in range(self.points):
                    f.write(f"V_{self.wlsArray[i]:.3f},")
                f.write("\n")
                for j in range(self.oscpoints):
                    for i in range(self.points):
                        f.write(f"{self.rawdataArray[i][j]:.6f},")
                    f.write("\n")
                f.close()
                self.statusbar.showMessage(f"Raw data saved")
        elif len(filename) > 0:
           with open(filename, 'w') as f:
                for i in range(self.points):
                    f.write(f"V_{self.wlsArray[i]:.3f}\t")
                f.write("\n")
                for j in range(self.oscpoints):
                    for i in range(self.points):
                        f.write(f"{self.rawdataArray[i][j]:.6f}\t")
                    f.write("\n")
                f.close()
                self.statusbar.showMessage(f"Raw data saved")

    def saveSettings(self, filename=""):
        if filename == "":
            filename = self.settingsfile    
        settings_dict = {}
        settings_dict["__lastdir__"] = self.lastdir
        for w in self.findChildren(QSpinBox):
            settings_dict[w.objectName()] = w.value()
        for w in self.findChildren(QDoubleSpinBox):
            settings_dict[w.objectName()] = w.value()
        for w in self.findChildren(QCheckBox):
            settings_dict[w.objectName()] = w.isChecked()
        for w in self.findChildren(QRadioButton):
            settings_dict[w.objectName()] = w.isChecked()
            
        json.dump(settings_dict, open(filename, "w"))
        
    def loadSettings(self, filename=""):
        if filename == "":
            filename = self.settingsfile
        lastslash = self.fullpath.rfind("/")
        path = self.fullpath[:lastslash + 1] + filename

        if os.path.isfile(path):
            settings_dict = json.load(open(path, "r"))
            if "__lastdir__" in settings_dict:
                self.lastdir = settings_dict["__lastdir__"]
            for key in settings_dict:
                if key[:2] != "__" and key[-2:] != "__":
                    w = self.findChild(QWidget, key)
                    if "Spin" in key:
                        w.setValue(settings_dict[key])
                    if "Check" in key:
                        w.setChecked(settings_dict[key])
                    if "Radio" in key:
                        w.setChecked(settings_dict[key])

    def Exit(self):
        quit()

    def About(self):
        QMessageBox.about(self, "About", "This software was created to simplify spectral data " +
                          "acquisitions using Horiba H20-UVL Monochromator and MDO3034 oscilloscope.\n\n" +
                          "It depends on the following python packages:\n" +
                          "\t- PyQt5\n" +
                          "\t- Numpy\n" +
                          "\t- Matplotlib\n" +
                          "\t- H5Py\n" +
                          "\t- Pyvisa\n" +
                          "It also depends on ActiveX components to communicate with the monochromator, hence, " +
                          "it is compatible with Windows only!\n\n" +
                          "Created by Paulo F. Jarschel, 2022")
    
    def CloseDevices(self):
        self.statusbar.showMessage(f"Devices closed")

    def closeEvent(self, event):
        self.Stop()
        self.saveSettings()
        self.CloseDevices()

#Run
if __name__ == "__main__":
    myappid = 'pfjarschel.pyinterfaces.horiba-h20.0.1'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec_())
