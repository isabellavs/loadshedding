import requests

def currentStatus():

   noLoadLevel = -1

   try:
      response = requests.get("https://loadshedding.eskom.co.za/Loadshedding/GetStatus")
   except Exception as e:
      noLoadLevel = -1

   if response.ok:
      noLoadLevel = int(response.json()) - 1

   return noLoadLevel

