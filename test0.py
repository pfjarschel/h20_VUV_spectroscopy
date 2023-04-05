import win32com.client
import time

mono_reqd = win32com.client.Dispatch("JYMono.Monochromator.1")
mono_reqd.Uniqueid = "Mono5"
mono_reqd.Load()
mono_reqd.OpenCommunications()
mono_reqd.Initialize(False, False)
t0 = time.time()
monoOK = False
while not monoOK and (time.time() - t0 < 10):
    monoOK = mono_reqd.InitializeComplete
    time.sleep(0.1)
print(mono_reqd.InitializeComplete)

val = mono_reqd.GetCurrentWavelength()
print(val)