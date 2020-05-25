#!/usr/bin/python
# Written by Delson
import time
import notify2
from playsound import playsound
flag=True
while flag:
	power_now = open("/sys/class/power_supply/BAT1/charge_now", "r").readline()
	power_full = open("/sys/class/power_supply/BAT1/charge_full", "r").readline()
	total_battery = (float(power_now)/float(power_full))*100
	battery=int(total_battery)
	print (total_battery)
	while total_battery <= 110:
		power_now = open("/sys/class/power_supply/BAT1/charge_now", "r").readline()
		power_full = open("/sys/class/power_supply/BAT1/charge_full", "r").readline()
		total_battery = (float(power_now)/float(power_full))*100
		time.sleep(70)
		if total_battery <= 20:
			notify2.URGENCY_CRITICAL
			notify2.init('critical')
			n = notify2.Notification('Kindly put it on Charge' , 'CRITICAL BATTERY  ' + str(battery) + '%')
			n.show()
			playsound('battery.mp3')

