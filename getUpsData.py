import subprocess

cmd="upsc ups"
output=""
measurements=["battery.mfr.date", "battery.type", "device.mfr", "device.model","device.serial","device.type",
			"driver.name", "driver.paramter.port", "driver.parameter.synchronous", "driver.version", "driver.version.data",
			"ups.beeper.status", "ups.mfr","ups.model", "ups.serial", "ups.status", "ups.test.result", "driver.parameter.port",
			"driver.parameter.syncronous"]

p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

for line in p.stdout.readlines(): #read and store result in log file
    line = line.decode("utf-8").rstrip()
    key = line.split(':')[0]
    value = line.split(':')[1]

    if key in measurements:
	try: float(value) #check if the value is a number
	except: value = f'"{value}"' #adds quotes around the value string if value is not a number
	measurement =f"{key}={value}"
	if output != "":
            measurement = "," + measurement
	output += measurement

output = "ups " + output.rstrip()
print(output, end='')
