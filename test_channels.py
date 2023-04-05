import pyvisa as visa
import numpy as np
import mdo3034
import matplotlib.pyplot as plt
import sys
from struct import unpack

visarm = visa.ResourceManager()
osc_name = visarm.list_resources()[0]
osc = visarm.open_resource(osc_name)
osc.write("DATA:SOURCE CH1")
nchan = 4

if nchan == 0:
    nchan = 4
osc.write(f"DATA:SOU CH{nchan}")

ymult = float(osc.query("WFMPRE:YMULT?"))
yzero = float(osc.query("WFMPRE:YZERO?"))
yoff = float(osc.query("WFMPRE:YOFF?"))
xincr = float(osc.query("WFMPRE:XINCR?"))

osc.write("CURVE?")
rawdata = osc.read_raw()
headerlen = 2 + int(rawdata[1])
header = rawdata[:headerlen]
data = rawdata[headerlen:-1]
data = np.array(unpack("%sB" % len(data), data))

yarray = (data - yoff)*ymult + yzero
xarray = np.arange(0.0, xincr*len(yarray), xincr)
osc.close()
plt.plot(xarray,yarray)
plt.show()