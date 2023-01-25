from os.path import exists
from sheddinglib import currentStatus
from datetime import datetime

newStatus = int(currentStatus())

if newStatus < -1:
   exit(-1);

oldStatus = -1
if exists("stage.log"):
   with open ("stage.log", "r") as savedStage:
      oldStatus = int(savedStage.read().rstrip())

if oldStatus != newStatus:
   print(f"Stage {newStatus} @ {datetime.now().strftime('%Y-%m-%d %H:%M')}")
   saveNew = open("stage.log", mode="w", encoding="utf-8")
   saveNew.write(str(newStatus) + "\n")
   saveNew.close
