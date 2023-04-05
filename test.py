from Horiba_JY_LVPort import HoribaJYMonosManager, HoribaJYMono
from mdo3034 import MDO3034
import matplotlib.pyplot as plt 

monoman = HoribaJYMonosManager()
monos = monoman.GetMonos()
print(monos)

mono = HoribaJYMono(name="H20UVL samba")
mono.Initialize()

mono.SetWavelength(600)

gratings = mono.GetGratings()
curr_grating = mono.GetCurrentGratingTurret()
wl = mono.GetCurrentWavelength()
slit0_width = mono.GetSlitWidth(0)
slit1_width = mono.GetSlitWidth(1)
mirror0_pos = mono.GetMirrorPos(0)
mirror1_pos = mono.GetMirrorPos(1)

print(gratings)
for g in gratings:
    print(g)
print(curr_grating)
print(wl)
print(mono.slitWidths)
print(mono.mirrorPositions)


osc = MDO3034()
osc.Initialize()
points = osc.GetTraceLength()
ts = osc.GetTimeScale()
x, y = osc.GetData(1)
print(points)
print(ts)
plt.plot(x, y)
plt.show()

