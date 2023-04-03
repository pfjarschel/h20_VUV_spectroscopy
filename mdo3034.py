# -*- coding: utf-8 -*-

import pyvisa as visa
import numpy as np
from struct import unpack


class MDO3034:
    # definitions
    idn_string = "MDO3034"
    usbid_hex = "0x0699::0x0408"
    usbid_dec = "1689::1032"
    visarm = None
    visaOK = False
    osc = None
    oscOK = False
    oscID = ""
    traceLength = 1001
    timescale = 10e-3
    simulate = True

    # main functions
    def __init__(self):
        try:
            self.visarm = visa.ResourceManager()
            self.visaOK = True
        except:
            print("Error creating NI VISA Resource Manager!")
            pass
        if not self.visaOK:
            try:
                self.visarm = visa.ResourceManager('@py')
                self.visaOK = True
            except:
                print("Error creating PYVISA Resource Manager!")
                pass

    def __del__(self):
        self.Close()
        return 0

    # OSC functions

    def Connect(self):
        if self.visaOK:
            try:
                oscname = ""
                all = self.visarm.list_resources()
                for name in all:
                    if (self.usbid_dec in name) or (self.usbid_hex in name):
                        oscname = name
                        break
                self.osc = self.visarm.open_resource(oscname)

                if self.idn_string in self.osc.query("*IDN?"):
                    self.oscOK = True
                else:
                    print("Error opening Oscilloscope! Is the address correct?")
            except:
                print("Critical error opening Oscilloscope! Is it connected?")
                pass

    def Initialize(self):
        self.Connect()

        if self.oscOK:
            self.osc.timeout = 10000

            self.osc.write("DATA:WIDTH 1")
            self.osc.wrap_handler("DATA:ENC RPB")

            self.traceLength = self.getTraceLength()
            
        return self.oscOK

    def Close(self):
        if self.oscOK:
            self.oscOK = False
            self.osc.close()

    def GetTraceLength(self):
        if self.oscOK:
            resp = self.osc.query("WFMOutpre:NR_pt?")
            length = int(resp)
            self.traceLength = length
            return length
        else:
            return self.traceLength

    def GetTimeScale(self):
        if self.oscOK:
            resp = self.osc.query("HOR:SCA?")
            scale = 400e-12
            try:
                scale = float(resp)
            except:
                try:
                    scale = float(resp.split(" ")[1])
                except:
                    pass
            self.timescale = scale
            return scale
        else:
            return self.timescale

    def SetTimeScale(self, tscale):
        if self.oscOK:
            if tscale < 400e-12:
                tscale = 400e-12
            if tscale > 1000:
                tscale = 1000
            self.osc.write(f"HOR:SCA {tscale}")

    def GetData(self, chan):
        if self.oscOK:
            nchan = int(np.mod(chan, 4))
            if nchan == 0:
                nchan = 4
            self.osc.write(f"DATA:SOU CH{nchan}")
            
            ymult = self.osc.query("WFMPRE:YMULT?")
            yzero = self.osc.query("WFMPRE:YZERO?")
            yoff = self.osc.query("WFMPRE:YOFF?")
            xincr = self.osc.query("WFMPRE:XINCR?")
            
            self.osc.write("CURVE?")
            rawdata = self.osc.read_raw()
            headerlen = 2 + int(rawdata[1])
            header = rawdata[:headerlen]
            data = rawdata[headerlen:-1]
            data = np.array(unpack("%sB" % len(data), data))

            yarray = (data - yoff)*ymult + yzero
            xarray = np.arange(0.0, xincr*len(yarray), xincr)
        
        elif self.simulate:
            yarray = np.random.randint(0, 10, self.traceLength)/1000.0
            xarray = np.linspace(0.0, self.timescale*10, self.traceLength)

        else:
            yarray = np.zeros(self.traceLength)
            xarray = np.linspace(0.0, self.timescale*10, self.traceLength)

        return xarray, yarray
