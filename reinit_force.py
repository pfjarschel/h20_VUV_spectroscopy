import pyvisa as visa

visarm = visa.ResourceManager()
osc_name = visarm.list_resources()[0]
osc = visarm.open_resource(osc_name)
osc.write("DATA:SOURCE CH1")
osc.close()