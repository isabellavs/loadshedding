import requests

# TODO: turn this into a way to find an Eskom area with timeslots for an area not controlled by Eskom


def currentStatus():

   noLoadLevel = -1
   response = requests.get("https://loadshedding.eskom.co.za/Loadshedding/GetStatus")

   if response.ok:
      noLoadLevel = int(response.json()) - 1
      print(noLoadLevel)
   else:
      print("error opening loadshedding url")

   return noLoadLevel


def getMunicipalities(sheddingStatus):

#   response = requests.get("https://loadshedding.eskom.co.za/Loadshedding/GetMunicipalities/?Id=3")
#   print(response.json())
#   AuthoritiesList = response.json()
   # {'Disabled': False, 'Group': None, 'Selected': False, 'Text': 'City of Tshwane', 'Value': '167'}

   foundDate = False
   dateLine = ""
   shedDates = {}
   for i in range(24):
      print(i)
      # Kudube is on page 12
      response = requests.get(f"https://loadshedding.eskom.co.za/Loadshedding/GetSurburbData/?pagesize=100&pagenum={i}&id=167")
      if response.ok:
         suburbs = response.json()['Results']

         for item in suburbs:
            if item['Tot'] != 0:
               # below was before we knew that Kudube is similair to Villieria
               resp = requests.get(f"https://loadshedding.eskom.co.za/Loadshedding/GetScheduleM/{item['id']}/{sheddingStatus}/3/1")
               print("page:", i, item)
               #resp = requests.get(f"https://loadshedding.eskom.co.za/Loadshedding/GetScheduleM/1026141/{sheddingStatus}/3/1")
               lines = resp.text.splitlines()

               for line in lines:
                  if ("Thu, 05 Jan" in line) or ("Fri, 06 Jan" in line) or ("Sat, 07 Jan" in line) or ("Sun, 08 Jan" in line) or ("Mon, 09 Jan" in line):
                     foundDate = True
                     dateLine = line.replace(',', '').replace(' ', '')
                     if shedDates.get(dateLine, " ") == " ":
                        shedDates[dateLine] = []

                  if ("Tue, 10 Jan" in line):
                     foundDate = False
                     dateLine = ""

                  if (foundDate == True) and ("Time" in line) and ("08:00 -" in line or "10:00 -" in line or "18:00 -" in line or "02:00 -" in line or "00:00 -" in line or "16:00 -" in line):
                     timeLine = line.split('{')[1].split('}')[0]
                     if timeLine not in shedDates[dateLine]:
                        shedDates[dateLine].append(timeLine)
            break
   print(shedDates)

   for key in shedDates.keys():
      print(key)

      shedDates[key].sort()
      for times in shedDates[key]:
         print(times)

   # {'id': '1027184', 'text': 'Villeria', 'Tot': 0}
   # if Tot == 0, Eskom does not have the suburb's schedule

   # <suburb_id>/<stage>/<province_id>/<municipality_total>
   #response = requests.get(f"https://loadshedding.eskom.co.za/Loadshedding/GetScheduleM/1027184/{sheddingStatus}/3/1")
   if response.ok:
      print(response)
   else:
      print("error opening loadshedding url")

   # for Tshwane, Villieria = block 11

def main():
   
   noEskomLevel = currentStatus()
   getMunicipalities(noEskomLevel)

if __name__ == "__main__":
   main()
