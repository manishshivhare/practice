#Back to the Future - Time Machine - www.101computing.net/back-to-the-future/
from datetime import *

#Typing Text Effect...
import time,os,sys
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

def printBanner():
  print(">>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<")
  print(">>>                                 <<<")
  print(">>> Back To The Future Time Machine <<<")
  print(">>>                                 <<<")
  print(">>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<")
  print("")
os.system("cls")  
printBanner()

#Get Today's Date
today = date.today()
print("Today: " +  today.strftime('%d, %B %Y'))
print("Today is " +  today.strftime('%A'))
print("")

#Asking the user how many days to they want to time travel
delta = int(input(" >>> Enter a number of days for your time travel. (A negative number to go back in time, a positive number to visit the future)"))

print("")
typingPrint(">>> Going Back to the Future >>>\n")
print("")

#Work out the end date based on the delta chosen by the user
endDate = today + timedelta(days=delta)

#Output end date
print("End Date: " +  endDate.strftime('%d, %b %Y'))
#Display the day of the week (Monday to Sunday) corresponding to the EndDate.
print("Day of the week: " +endDate.strftime("%A") + ".")
