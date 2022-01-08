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
into InfluxDB Line Protocol like this: 
```
ups battery.charge=100,battery.charge.low=10,battery.charge.warning=20,battery.mfr.date="CPS",battery.runtime=2970,battery.runtime.low=300,battery.type="PbAcid",battery.voltage=13.1,battery.voltage.nominal=12
```

## Usage

see all UPS existant in the config directory 

Call the script from `telegraf.conf` like this
```
[[inputs.exec]]

   commands = ["python /full/path/to/getUpsData.py --config eaton/eco --name MyUPS"]
   timeout = "5s"
   data_format = "influx"
```

if your UPS does not appear in the configuration directory, you can simply create by saving the result in the correct folder :
```
upsc THE_UPS 2>/dev/null | awk -F ":" '{ $2 = "" ; print $0 }'
```







## Compatibility
Tested on:
* Cyberpower CP1000AVRLCDa
* CyberPower SL700U (`CyberPower/SL700U`)
* Dell UPS 1000T/1920T/1920R HV (`Dell/5PX`)
* MGE Pulsar 2200 (`Eaton/Pulsar`)
* Eaton eco 1600 (`Eaton/Eco`)


If you're using this with a different UPS, please let me know so I can add it to the list

## Contributors

Thanks to the following for helping improve this repo.

* @openincident
* @mattster98
* @Graffics
* @Depfryer
