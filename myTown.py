#--------------------
import requests
import datetime
from sheddinglib import currentStatus

# returns local time. yeah.
now = datetime.datetime.now()
today = now.strftime("%a, %d %b")
tomorrow = now + datetime.timedelta(days=1)
tomorrow = tomorrow.strftime("%a, %d %b")


'''
def currentStatus():

   noLoadLevel = -1
   response = requests.get("https://loadshedding.eskom.co.za/Loadshedding/GetStatus")

   if response.ok:
      noLoadLevel = int(response.json()) - 1
      print(noLoadLevel)

   return noLoadLevel
'''

def getTimes(sheddingStatus):

   foundDate = False
   shedDates = {}
   resp = requests.get(f"https://loadshedding.eskom.co.za/Loadshedding/GetScheduleM/1026141/{sheddingStatus}/3/1")
   lines = resp.text.splitlines()

   for line in lines:

      if today in line:
         foundDate = True
         if shedDates.get(today, " ") == " ":
            shedDates[today] = []

      if tomorrow in line:
         foundDate = False

      if (foundDate == True) and \
         "Time" in line and \
         "KUDUBE / MANYALETI" in line:
         timeLine = line.split('{')[1].split('}')[0]
         if timeLine not in shedDates[today]:
            shedDates[today].append(timeLine)

   for key in shedDates.keys():
      print(key)

      shedDates[key].sort()
      for times in shedDates[key]:
         #print(times.split(',')[0][7:].replace('"', '').split(' ')[0])
         print(times.split(',')[0][7:].replace('"', ''))

def main():
   
   howBad = currentStatus()

   if howBad == -1:
      print("Error retrieving loadshedding status")
   elif howBad == 1:
      print("Not loadshedding at the moment")
   else:
      getTimes(howBad)

if __name__ == "__main__":
   main()
