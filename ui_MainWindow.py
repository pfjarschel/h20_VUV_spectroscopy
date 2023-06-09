# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\pfjar\OneDrive\Stuff\Unicamp\Controle de Equipamentos\Python\Horiba\H20_VUV\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 642)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\pfjar\\OneDrive\\Stuff\\Unicamp\\Controle de Equipamentos\\Python\\Horiba\\H20_VUV\\spectrum.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMaximumSize(QtCore.QSize(320, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.startSpin = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.startSpin.setKeyboardTracking(False)
        self.startSpin.setDecimals(3)
        self.startSpin.setMinimum(1.0)
        self.startSpin.setMaximum(10000.0)
        self.startSpin.setObjectName("startSpin")
        self.verticalLayout.addWidget(self.startSpin)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.stepSpin = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.stepSpin.setKeyboardTracking(False)
        self.stepSpin.setDecimals(3)
        self.stepSpin.setMinimum(0.001)
        self.stepSpin.setMaximum(1000.0)
        self.stepSpin.setProperty("value", 1.0)
        self.stepSpin.setObjectName("stepSpin")
        self.verticalLayout_3.addWidget(self.stepSpin)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 3, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.stopSpin = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.stopSpin.setKeyboardTracking(False)
        self.stopSpin.setDecimals(3)
        self.stopSpin.setMinimum(1.0)
        self.stopSpin.setMaximum(10000.0)
        self.stopSpin.setProperty("value", 600.0)
        self.stopSpin.setObjectName("stopSpin")
        self.verticalLayout_2.addWidget(self.stopSpin)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 2, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.runBut = QtWidgets.QPushButton(self.groupBox_3)
        self.runBut.setObjectName("runBut")
        self.horizontalLayout.addWidget(self.runBut)
        self.stopBut = QtWidgets.QPushButton(self.groupBox_3)
        self.stopBut.setObjectName("stopBut")
        self.horizontalLayout.addWidget(self.stopBut)
        self.gridLayout_3.addLayout(self.horizontalLayout, 6, 0, 1, 2)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_9.addWidget(self.label_9)
        self.stepintSpin = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.stepintSpin.setKeyboardTracking(False)
        self.stepintSpin.setDecimals(3)
        self.stepintSpin.setMinimum(0.001)
        self.stepintSpin.setMaximum(1000.0)
        self.stepintSpin.setProperty("value", 1.0)
        self.stepintSpin.setObjectName("stepintSpin")
        self.verticalLayout_9.addWidget(self.stepintSpin)
        self.gridLayout_3.addLayout(self.verticalLayout_9, 3, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pointsInd = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pointsInd.sizePolicy().hasHeightForWidth())
        self.pointsInd.setSizePolicy(sizePolicy)
        self.pointsInd.setMinimumSize(QtCore.QSize(113, 0))
        self.pointsInd.setMaximumSize(QtCore.QSize(113, 16777215))
        self.pointsInd.setReadOnly(True)
        self.pointsInd.setObjectName("pointsInd")
        self.horizontalLayout_6.addWidget(self.pointsInd)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.linRadio = QtWidgets.QRadioButton(self.groupBox_3)
        self.linRadio.setChecked(True)
        self.linRadio.setObjectName("linRadio")
        self.horizontalLayout_6.addWidget(self.linRadio)
        self.dbRadio = QtWidgets.QRadioButton(self.groupBox_3)
        self.dbRadio.setObjectName("dbRadio")
        self.horizontalLayout_6.addWidget(self.dbRadio)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 4, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(320, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.gratingCombo = QtWidgets.QComboBox(self.groupBox)
        self.gratingCombo.setObjectName("gratingCombo")
        self.verticalLayout_4.addWidget(self.gratingCombo)
        self.gridLayout_4.addLayout(self.verticalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_10.addWidget(self.label_11)
        self.oscInd = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oscInd.sizePolicy().hasHeightForWidth())
        self.oscInd.setSizePolicy(sizePolicy)
        self.oscInd.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.oscInd.setFont(font)
        self.oscInd.setReadOnly(True)
        self.oscInd.setObjectName("oscInd")
        self.verticalLayout_10.addWidget(self.oscInd)
        self.horizontalLayout_5.addLayout(self.verticalLayout_10)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_12.addWidget(self.label_12)
        self.wavInd = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wavInd.sizePolicy().hasHeightForWidth())
        self.wavInd.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.wavInd.setFont(font)
        self.wavInd.setReadOnly(True)
        self.wavInd.setObjectName("wavInd")
        self.verticalLayout_12.addWidget(self.wavInd)
        self.horizontalLayout_5.addLayout(self.verticalLayout_12)
        self.gridLayout_4.addLayout(self.horizontalLayout_5, 8, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_11.addWidget(self.label_10)
        self.wlSpin = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.wlSpin.setKeyboardTracking(False)
        self.wlSpin.setDecimals(3)
        self.wlSpin.setMinimum(1.0)
        self.wlSpin.setMaximum(10000.0)
        self.wlSpin.setObjectName("wlSpin")
        self.verticalLayout_11.addWidget(self.wlSpin)
        self.horizontalLayout_3.addLayout(self.verticalLayout_11)
        self.shutterCheck = QtWidgets.QCheckBox(self.groupBox)
        self.shutterCheck.setObjectName("shutterCheck")
        self.horizontalLayout_3.addWidget(self.shutterCheck)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.oscchanSpin = QtWidgets.QSpinBox(self.groupBox)
        self.oscchanSpin.setKeyboardTracking(False)
        self.oscchanSpin.setMinimum(1)
        self.oscchanSpin.setMaximum(4)
        self.oscchanSpin.setObjectName("oscchanSpin")
        self.verticalLayout_7.addWidget(self.oscchanSpin)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.oscscaleSpin = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.oscscaleSpin.setKeyboardTracking(False)
        self.oscscaleSpin.setDecimals(6)
        self.oscscaleSpin.setMinimum(1e-06)
        self.oscscaleSpin.setMaximum(10000.0)
        self.oscscaleSpin.setProperty("value", 10.0)
        self.oscscaleSpin.setObjectName("oscscaleSpin")
        self.verticalLayout_8.addWidget(self.oscscaleSpin)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.usedetBut = QtWidgets.QPushButton(self.groupBox)
        self.usedetBut.setObjectName("usedetBut")
        self.gridLayout_5.addWidget(self.usedetBut, 1, 0, 1, 3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.calSpin = QtWidgets.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calSpin.sizePolicy().hasHeightForWidth())
        self.calSpin.setSizePolicy(sizePolicy)
        self.calSpin.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.calSpin.setKeyboardTracking(False)
        self.calSpin.setDecimals(3)
        self.calSpin.setMaximum(1000.0)
        self.calSpin.setProperty("value", 1.0)
        self.calSpin.setObjectName("calSpin")
        self.verticalLayout_6.addWidget(self.calSpin)
        self.gridLayout_5.addLayout(self.verticalLayout_6, 0, 1, 1, 2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.detecInd = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.detecInd.sizePolicy().hasHeightForWidth())
        self.detecInd.setSizePolicy(sizePolicy)
        self.detecInd.setMaximumSize(QtCore.QSize(147, 16777215))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.detecInd.setFont(font)
        self.detecInd.setReadOnly(True)
        self.detecInd.setObjectName("detecInd")
        self.verticalLayout_5.addWidget(self.detecInd)
        self.gridLayout_5.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 9, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.graphHolder = QtWidgets.QGridLayout()
        self.graphHolder.setObjectName("graphHolder")
        self.gridLayout_2.addLayout(self.graphHolder, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 6, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 99, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 5, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_config = QtWidgets.QAction(MainWindow)
        self.actionSave_config.setObjectName("actionSave_config")
        self.actionLoad_config = QtWidgets.QAction(MainWindow)
        self.actionLoad_config.setObjectName("actionLoad_config")
        self.actionSave_final_results = QtWidgets.QAction(MainWindow)
        self.actionSave_final_results.setObjectName("actionSave_final_results")
        self.actionSave_raw_data = QtWidgets.QAction(MainWindow)
        self.actionSave_raw_data.setObjectName("actionSave_raw_data")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionSave_config)
        self.menuFile.addAction(self.actionLoad_config)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_final_results)
        self.menuFile.addAction(self.actionSave_raw_data)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Horiba H20-UVL Sweep"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Sweep config"))
        self.label.setText(_translate("MainWindow", "Start Wavelength (nm)"))
        self.label_3.setText(_translate("MainWindow", "Step wavelength (nm)"))
        self.label_2.setText(_translate("MainWindow", "Stop wavelength (nm)"))
        self.runBut.setText(_translate("MainWindow", "Run"))
        self.stopBut.setText(_translate("MainWindow", "Stop"))
        self.label_9.setText(_translate("MainWindow", "Step interval (s)"))
        self.linRadio.setText(_translate("MainWindow", "mW"))
        self.dbRadio.setText(_translate("MainWindow", "dBm"))
        self.groupBox.setTitle(_translate("MainWindow", "Control/Monitor"))
        self.label_4.setText(_translate("MainWindow", "Grating select"))
        self.label_11.setText(_translate("MainWindow", "Osc. reading (mV)"))
        self.label_12.setText(_translate("MainWindow", "Wavelength (nm)"))
        self.label_10.setText(_translate("MainWindow", "Wavelength (nm)"))
        self.shutterCheck.setText(_translate("MainWindow", "Shutter (blocked)"))
        self.label_7.setText(_translate("MainWindow", "Osc. Channel"))
        self.label_8.setText(_translate("MainWindow", "Osc. scale (ms/div)"))
        self.usedetBut.setText(_translate("MainWindow", "Use detector reading as calibration"))
        self.label_6.setText(_translate("MainWindow", "Cal. factor (V/mW)"))
        self.label_5.setText(_translate("MainWindow", "Det. reading (mV)"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Results"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionSave_config.setText(_translate("MainWindow", "Save config..."))
        self.actionLoad_config.setText(_translate("MainWindow", "Load config..."))
        self.actionSave_final_results.setText(_translate("MainWindow", "Save results..."))
        self.actionSave_raw_data.setText(_translate("MainWindow", "Save raw data..."))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About..."))
