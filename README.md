# Description
Get data from USB-connected UPS into InfluxDB using Telegraf

Transforms `upsc` output like this:
```
battery.charge: 100
battery.charge.low: 10
battery.charge.warning: 20
battery.mfr.date: CPS
battery.runtime: 3133
battery.runtime.low: 300
battery.type: PbAcid
battery.voltage: 13.1
battery.voltage.nominal: 12
```
..into InfluxDB Line Protocol like this: 
```
ups battery.charge=100,battery.charge.low=10,battery.charge.warning=20,battery.mfr.date="CPS",battery.runtime=2970,battery.runtime.low=300,battery.type="PbAcid",battery.voltage=13.1,battery.voltage.nominal=12
```

## Usage

Edit the script `cmd` variable to reflect your setup. Specifically, change 'ups' to whatever you named your UPS in `NUT` or `upsd`.

Call the script from `telegraf.conf` like this
```
[[inputs.exec]]

   commands = ["python /path/to/getUpsData.py"]
   timeout = "5s"
   data_format = "influx"
```

## Compatibility
Tested on:
* Cyberpower CP1000AVRLCDa

If you're using this with a different UPS, please let me know so I can add it to the list
