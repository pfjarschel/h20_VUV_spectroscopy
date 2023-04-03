# -*- coding: utf-8 -*-

import numpy as np

class H20UVL:
    # definitions
    devOK = False
    
    grating = 0
    wavelength = 100.0
    simulate = True

    # main functions
    def __init__(self, dev_id):
        # TODO
        # Connect to ActiveX
        # List devices
        # Find right device 
        # Connect
        # OK
        
        self.devOK = True

    def __del__(self):
        self.close()
        return 0

    # Monochromator functions
    def init(self):
        if self.devOK:
            # TODO
            # Perform initializations
            # Check/Set grating
            # Go to default (or load last) WL
            self.setGrating(0)

    def close(self):
        if self.devOK:
            # TODO
            # Perform safety stuff
            # Disconnect
            self.devOK = False

    def setGrating(self, gratnum):
        if self.devOK:
            # TODO
            # Set grating
            self.grating = gratnum
        
    def getGrating(self):
        # TODO
        # Get grating info from activex
        return self.grating
    
    def setWl(self, wl):
        if self.devOK:
            # TODO
            # Set WL
            self.wavelength = wl
            
    def getWL(self):
        if self.devOK:
            # TODO
            # Get wavelength info from activex
            return self.wavelength
    