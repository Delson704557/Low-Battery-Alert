#!/usr/bin/python
import time
from playsound import playsound
power_now = open("/sys/class/power_supply/BAT1/charge_now", "r").readline()
power_full = open("/sys/class/power_supply/BAT1/charge_full", "r").readline()
total_battery = (float(power_now)/float(power_full))*100
print (float(total_battery))
while total_battery <= 90:
	print("")
	power_now = open("/sys/class/power_supply/BAT1/charge_now", "r").readline()
	power_full = open("/sys/class/power_supply/BAT1/charge_full", "r").readline()
	total_battery = (float(power_now)/float(power_full))*100
	print (float(total_battery))
	time.sleep(60)
	if total_battery <= 15:
		playsound('bell.mp3')
		quit()
  
