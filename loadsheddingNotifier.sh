#!/bin/bash

msg=$(/usr/bin/python3 /home/alphacentauri/Projects/pyproj/loadshedding/checkStage.py)

if [ ${#msg} -ne 0 ] ; then
   export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus" && /usr/bin/notify-send -u critical "${msg}"
   /usr/bin/python3 /home/alphacentauri/Projects/pyproj/loadshedding/myTown.py > /home/alphacentauri/Projects/pyproj/loadshedding/offtime.log
fi
