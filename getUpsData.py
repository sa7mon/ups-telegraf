from __future__ import print_function
import subprocess,sys

if (len(sys.argv) == 2):

    arg = sys.argv[1]

    cmd="upsc "+arg+" > /dev/stdout 2> /dev/null"

    output=""

    string_measurements=["battery.mfr.date", "battery.type", "device.mfr", "device.model","device.serial","device.type",
            "driver.name", "driver.paramter.port", "driver.parameter.synchronous", "driver.version", "driver.version.data",
            "ups.beeper.status", "ups.mfr","ups.model", "ups.serial", "ups.status", "ups.test.result", "driver.parameter.port",
            "driver.parameter.syncronous"]

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
