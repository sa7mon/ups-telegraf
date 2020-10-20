# https://github.com/sa7mon/ups-telegraf
from __future__ import print_function
import subprocess

cmd="upsc CyberPowerSL700U"
output=""
string_measurements=["battery.charge","battery.charge.low","battery.charge.warning","battery.mfr.date","battery.runtime","battery.runtime.low","battery.type","battery.voltage","battery.voltage.nominal","device.mfr","device.type","driver.parameter.bus","driver.parameter.lowbatt","driver.parameter.offdelay","driver.parameter.ondelay","driver.parameter.pollfreq","driver.parameter.pollinterval","driver.parameter.port","driver.parameter.productid","driver.parameter.synchronous","driver.parameter.vendor","driver.parameter.vendorid","driver.version.internal","input.transfer.high","input.transfer.low","input.voltage","input.voltage.nominal","output.voltage","ups.beeper.status","ups.delay.shutdown","ups.delay.start","ups.load","ups.mfr","ups.productid","ups.realpower.nominal","ups.status","ups.timer.shutdown","ups.timer.start","ups.vendorid"]

p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

for line in p.stdout.readlines(): #read and store result in log file
    line = line.decode("utf-8").rstrip()
    key = line[:line.find(":")]
    value = line[line.find(":")+2:]

    if key in string_measurements:
        if value.isalpha():
            value = '"' + value + '"'
        measurement = key + "=" + value
        if output != "":
            measurement = "," + measurement
        output += measurement

output = "ups " + output.rstrip()
print(output, end='')
