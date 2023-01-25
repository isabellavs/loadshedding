from os.path import exists
from datetime import datetime

if exists("/home/alphacentauri/Projects/pyproj/loadshedding/offtime.log"):
   with open ("/home/alphacentauri/Projects/pyproj/loadshedding/offtime.log", "r") as timeTable:
      for i in timeTable.readlines():
         if i.rstrip[:2].isnumeric():
            hr = i.rstrip()
            startd = datetime.strptime(startDate, "%Y-%m-%d").date()

#if oldStatus != newStatus:
#   print(f"Stage {newStatus} loadshedding started")
#   saveNew = open("stage.log", mode="w", encoding="utf-8")
#   saveNew.write(str(newStatus) + "\n")
#   saveNew.close
