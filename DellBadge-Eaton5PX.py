from __future__ import print_function
import subprocess,sys

if (len(sys.argv) == 2):

    arg = sys.argv[1]

    cmd="upsc "+arg+" > /dev/stdout 2> /dev/null"

    output=""

    string_measurements=["battery.charge", "battery.charge.low", "battery.current", "battery.runtime", "battery.runtime.low", "battery.temperature", "battery.voltage", "device.mfr", "device.model", "device.type", "driver.name", "driver.parameter.pollfreq", "driver.parameter.pollinterval", "driver.parameter.port", "driver.parameter.snmp_version", "driver.parameter.synchronous", "driver.version", "driver.version.data", "driver.version.internal", "input.bypass.phases", "input.current", "input.frequency", "input.frequency.nominal", "input.phases", "input.realpower", "input.transfer.high", "input.transfer.low", "input.voltage", "input.voltage.nominal", "output.current", "output.frequency", "output.frequency.nominal", "output.phases", "output.power.nominal", "output.realpower", "output.realpower.nominal", "output.voltage", "output.voltage.nominal", "ups.beeper.status", "ups.firmware", "ups.firmware.aux", "ups.load", "ups.mfr", "ups.model", "ups.status", "ups.test.result", "ups.timer.shutdown", "ups.timer.start"]

    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

    for line in p.stdout.readlines(): #read and store result in log file
        line = line.decode("utf-8").rstrip()
        key = line[:line.find(":")]
        value = line[line.find(":")+2:]

        if key in string_measurements:
            if not re.match(r'^(-?)(\d+|\d+\.\d+)$',value):
                value = '"' + value + '"'
            measurement = key + "=" + value
            if output != "":
                measurement = "," + measurement
            output += measurement

    output = "ups " + output.rstrip()
    print(output, end='')
