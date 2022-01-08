from __future__ import print_function
import subprocess,sys
import re
import click
import os


@click.command()
@click.option('--config','-c', help='Config File of the UPS')
@click.option('--name','-n', help='Name of the UPS')
def main(config, name):
    try:
        # get file with properties returned by upsc
        path = os.path.dirname(__file__)
        file_config = f'{path}/config/{config}.properties'
        with open(file_config, 'r') as f:
            string_measurements = f.read().splitlines()

        # create the commande
        cmd= f"upsc {name} /dev/stdout 2> /dev/null"

        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        output=""
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
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()