# -*- coding: utf-8 -*-

"""
Created on Mon Oct 17 2022

@author: pfjarschel
"""

import win32com.client
import time

######################################
# Control and communication classes. #
######################################

# Generally, not sure if JYMONOLib/JYCONFIGBROWSERCOMPONENTLib prefix is necessary to identify COM/ActiveX libraries
class HoribaJYMonosManager():
    """
    Class to act as an interface between the application and the Horiba configuration manager.
    """

    # Did they fix the typo ('Brower')?
    config_browser = None
    try:
        config_browser = win32com.client.Dispatch("JYConfigBrowserComponent.JYConfigBrowerInterface.1")
    except:
        print("Error communicating with Horiba COM/ActiveX objects! Are they installed?")
    monosDict = {}

    def __init__(self):
        try:
            self.config_browser.Load()
        except:
            print("Error communicating with Horiba interface. Is the software properly installed?")

    def GetMonos(self) -> dict:
        """
        From LabView docs: Use the JYConfiguration Browser to return the
        uniqueIDs and display names all registered monos.
        Build the arrays by calling GetFirstMono followed by
        subsequent calls to GetNextMono. GetNextMono
        will return a blank (null) string when there are
        no more monos.
        """

        self.monosDict = {}
        try:
            firstId, firstName = self.config_browser.GetFirstMono()
            self.monosDict[firstName] = firstId
        
            reachedLast = False
            while not reachedLast:
                id, name = self.config_browser.GetNextMono()
                if name == "":
                    reachedLast = True
                else:
                    self.monosDict[name] = id
        except:
            print("Error finding any monochromator! Is there one connected? Is the official software installed and configured?")
        return self.monosDict


class HoribaGrating():
    """
    Simple class to hold grating properties.
    """

    id = 0
    lines = 0
    blaze = ""
    description = ""

    def __init__(self, id=0, lines="0", blaze="0", desc="None"):
        self.id = id
        self.lines = lines
        self.blaze = blaze
        self.description = desc

    def __str__(self):
        return f"Grating {self.id} - {self.description}:\n{self.lines} l/mm\n{self.blaze} nm blaze\n"


class HoribaJYMono():
    """
    Class to act as an interface between the application and all of the monochromator functions spread across many COM objects
    """

    mono_reqd = None
    try:
        mono_reqd = win32com.client.Dispatch("JYMono.Monochromator.1")
    except:
        print("Error communicating with Horiba COM/ActiveX objects! Are they installed?")

    name = ""
    id = ""
    gratings = []
    turret = 0
    currWavelength = 0.0
    slitWidths = {}
    mirrorPositions = {}

    for i in range(0, 6):
        slitWidths[f"{i}"] = 0
    for i in range(0, 2):
        mirrorPositions[f"{i}"] = 0

    manager = HoribaJYMonosManager()
    timeout = 10
    forcedInit = False
    emulating = False
    monoOK = False
    n_warns = 0
    max_warns = 3

    def __init__(self, name="", id=""):
        self.manager.GetMonos()

    def Initialize(self, forceInit=False, emulate=False, to = 10) -> bool:
        """
        Monochromator initialization procedure.
        If no name or id is supplied during creation of the object (or later),
        it tries to open the first monochromator found.
        
        Parameters:
            - forceInit: Forces the initialization of the motors. If false, they remain in the same positions (recommended).
            - emulate: Emulates the device, useful to test applications before real connections are made.
                       The emulation is performed by Horiba official software.
            - to: timeout for the initialization procedure (seconds).

        Returns: initialization status. 
        """
        self.n_warns = 0
        to = abs(to)
        found_error = False
        if self.id == "":
            if self.name != "":
                try:
                    self.id = self.manager.monosDict[self.name]
                except:
                    found_error = True
                    print("Error finding a monochromator with the provided name. Is it correct?")
            else:
                try:
                    self.name = list(self.manager.monosDict.keys())[0]
                    self.id = list(self.manager.monosDict.values())[0]
                except:
                    found_error = True
                    print("Error opening any monochromator! Is there one connected? Is the official software installed and configured?")
        else:
            try:
                self.name = list(self.manager.monosDict.keys())[list(self.manager.monosDict.values()).index(self.name)]
            except:
                print("Error finding a monochromator with the provided ID. Is it correct?")
                if self.name != "":
                    try:
                        self.id = self.manager.monosDict[self.name]
                        print(f"Managed to find the monochromator with the provided name. The correct ID is {self.id}")
                    except:
                        found_error = True
                        print("Error finding a monochromator with the provided ID or name. Are they correct?")
        
        if found_error:
            print("Errors found while identifying the monochromator. Initialization procedure halted.")
        else:
            try:
                self.mono_reqd.Uniqueid = "Mono5"
                self.mono_reqd.Load()
                self.mono_reqd.OpenCommunications()
                self.mono_reqd.Initialize(forceInit, emulate)
                t0 = time.time()
                while not self.monoOK and (time.time() - t0 < self.timeout):
                    self.monoOK = self.mono_reqd.InitializeComplete
                    time.sleep(0.1)
                self.monoOK = True
                if self.monoOK:
                    print("Initialization OK.")
                else:
                    print("Timeout reached during initialization. If you are SURE it should be OK, set monoOK var to True.")
            except:
                print("Error initializing monochromator!")
        
        return self.monoOK
                
    def GetGratings(self):  # -> list[HoribaGrating]:
        """
        Get information about all gratings configured in the monochromator.
        Returns list of Grating objects containing:
        - id: Grating index
        - lines: Lines/mm density values
        - blaze: Blaze (optimal wavelength)
        - description: Description
        """

        self.gratings = []
        
        if self.monoOK:
            try:
                currDens, densities, blazes, descriptions = self.mono_reqd.GetCurrentGratingWithDetails()
                for i in range(len(densities)):
                    self.gratings.append(HoribaGrating(i, densities[i], blazes[i], descriptions[i]))
            except:
                print("Error getting gratings info!")
        else:
            self.PrintInitWarning()

        if len(self.gratings) == 0:
            self.gratings.append(HoribaGrating())
        return self.gratings

    def GetGratingInfo(self, id) -> HoribaGrating:
        """
        Get information about a grating.
        Returns Grating object containing:
        - id: Grating index
        - lines: Lines/mm density values
        - blaze: Blaze (optimal wavelength)
        - description: Description
        """

        grating = HoribaGrating()
        if self.monoOK:
            id = abs(id)
            if len(self.gratings) == 0:
                self.GetGratings()
            if id < len(self.gratings):
                grating = self.gratings[id]
            else:
                print("Grating index out of range. Returning the highest id grating.")
                try:
                    grating = self.gratings[-1]
                except:
                    print("No grating found")
        else:
            self.PrintInitWarning()
        
        return grating

    def GetCurrentGratingTurret(self) -> int:
        """
        Get current grating turret index.
        """
        
        if self.monoOK:
            try:
                self.turret = self.mono_reqd.GetCurrentTurret()
            except:
                print("Error reading the current turret.")
        else:
            self.PrintInitWarning()
        
        return self.turret

    def SetCurrentGratingTurret(self, turret):
        """
        Set grating turret.
        """
        
        if self.monoOK:
            try:
                turret = abs(turret)
                if len(self.gratings) == 0:
                    self.GetGratings()
                if turret >= len(self.gratings):
                    turret = len(self.gratings) - 1
                self.mono_reqd.MovetoTurret(turret)
                
                busy = True
                t0 = time.time()
                while busy and (time.time() - t0 < self.timeout):
                    busy = self.mono_reqd.IsBusy()
                    time.sleep(0.1)

                self.turret = turret
            except:
                print("Error moving to the new turret.")
        else:
            self.PrintInitWarning()
    
    def GetCurrentGratingInfo(self) -> HoribaGrating:
        """
        Get information about current grating.
        Returns Grating object containing:
        - id: Grating index
        - lines: Lines/mm density values
        - blaze: Blaze (optimal wavelength)
        - description: Description
        """
        grating = HoribaGrating()
        if self.monoOK:
            id = self.GetCurrentGratingTurret()
            try:
                grating = self.GetGratingInfo(id)
            except:
                print("Error getting grating info")
        else:
            self.PrintInitWarning()

        return grating
    
    def GetCurrentWavelength(self) -> float:
        """
        Get current wavelength in nanometers.
        """
        
        if self.monoOK:
            try:
                val = self.mono_reqd.GetCurrentWavelength()
                unit = self.mono_reqd.GetDefaultUnits(1)
                
                if unit == 1:
                    val = val*1e6
                elif unit == 2:
                    val = val*1e3
                elif val == 4:
                    val = val/10.0
                elif val == 5:
                    val = val/1e3

                self.currWavelength = val
            except:
                print("Error reading the current wavelength.")
        else:
            self.PrintInitWarning()
        
        return self.currWavelength

    def SetWavelength(self, wl):
        """
        Moves to the desired wavelength, in nanometers.
        """
        
        if self.monoOK:
            try:
                wl = abs(wl)
                self.mono_reqd.MovetoWavelength(wl)
                
                busy = True
                t0 = time.time()
                while busy and (time.time() - t0 < self.timeout):
                    busy = self.mono_reqd.IsBusy()
                    time.sleep(0.1)

                self.currWavelength = wl
            except:
                print("Error moving to the new wavelength.")
        else:
            self.PrintInitWarning()

    def GetSlitWidth(self, slit_i) -> float:
            """
            Get slit width in millimiters.
            
            Slit numbers:
            0: Front Entrance
            1: Side Entrance
            2: Front Exit
            3: Side Exit
            4: First Intermediate
            5: Second Intermediate
            """
            
            if self.monoOK:
                try:
                    slit_i = abs(slit_i)
                    if slit_i > 5:
                        slit_i = 5
                    val = self.mono_reqd.GetCurrentSlitWidth(slit_i)
                    unit = self.mono_reqd.GetDefaultUnits(2)
                    
                    if unit == 2:
                        val = val/1e3
                    elif val == 3:
                        val = val/1e6
                    elif val == 4:
                        val = val/1e7
                    elif val == 5:
                        val = val/1e9

                    self.slitWidths[f"{slit_i}"] = val
                except:
                    print(f"Error reading the slit {slit_i} width.")
            else:
                self.PrintInitWarning()
            
            return self.slitWidths[f"{slit_i}"]

    def SetSlitWidth(self, slit_i, width):
        """
        Set slit width, in millimiters.

        Slit numbers:
        0: Front Entrance
        1: Side Entrance
        2: Front Exit
        3: Side Exit
        4: First Intermediate
        5: Second Intermediate
        """
        
        if self.monoOK:
            try:
                slit_i = abs(slit_i)
                width = abs(width)
                if slit_i > 5:
                    slit_i = 5
                self.mono_reqd.MovetoSlitPosition(slit_i, width)
                
                busy = True
                t0 = time.time()
                while busy and (time.time() - t0 < self.timeout):
                    busy = self.mono_reqd.IsBusy()
                    time.sleep(0.1)

                self.slitWidths[f"{slit_i}"] = width
            except:
                print(f"Error setting slit {slit_i} width.")
        else:
            self.PrintInitWarning()

    def GetMirrorPos(self, mirror_i) -> int:
            """
            Get mirror position.
            
            Mirror numbers:
            0: Entrance
            1: Exit

            Mirror positions:
            0: Front
            1: Side
            """
            
            if self.monoOK:
                try:
                    mirror_i = abs(mirror_i)
                    if mirror_i > 1:
                        mirror_i = 1
                    val = self.mono_reqd.GetCurrentMirrorPosition(mirror_i)
                    self.mirrorPositions[f"{mirror_i}"] = val
                except:
                    print(f"Error reading mirror {mirror_i} position.")
            else:
                self.PrintInitWarning()
            
            return self.mirrorPositions[f"{mirror_i}"]

    def SetMirrorPos(self, mirror_i, pos):
        """
        Set mirror position.

        Mirror numbers:
        0: Entrance
        1: Exit

        Mirror positions:
        0: Front
        1: Side
        """
        
        if self.monoOK:
            try:
                mirror_i = abs(mirror_i)
                pos = abs(pos)
                if mirror_i > 1:
                    mirror_i = 1
                if pos > 1:
                    pos = 1
                self.mono_reqd.MovetoMirrorPosition(mirror_i, pos)
                
                busy = True
                t0 = time.time()
                while busy and (time.time() - t0 < self.timeout):
                    busy = self.mono_reqd.IsBusy()
                    time.sleep(0.1)

                self.mirrorPositions[f"{mirror_i}"] = pos
            except:
                print(f"Error setting mirror {mirror_i} position.")
        else:
            self.PrintInitWarning()

    def PrintInitWarning(self):
        """
        Function to handle printing of monochromator not initialized warning.
        """
        
        self.n_warns += 1
        if self.n_warns <= self.max_warns:
            print("Warning: Monochromator not initialized.")
