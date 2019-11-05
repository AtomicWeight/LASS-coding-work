import time

#this is where you enter a pin number stored in yourPin

print('enter your PIN')
print(' ')
yourPin = str(input())
pinlength = len(yourPin)

#check to see if yourPin is valid or not 
for element in yourPin:
  while element in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm,./;'[]{}\|`~!@#$%^&*()-_+=?<>:":
    print(' ')
    print('error')
    print(' ')
    yourPin = str(input())
    if(yourPin not in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm,./;'[]{}\|`~!@#$%^&*()-_+=?<>:"):
      break
    else:
      print(' ')
      print('error')

pinlength = len(yourPin)

if(pinlength == 6):
  print(' ')
  confirmYourPin = str(input('Confirm your PIN: '))
  for element in confirmYourPin:
    while element in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm,./;'[]{}\|`~!@#$%^&*()-_+=?<>:":
      print(' ')
      print('error')
      print(' ')
      confirmYourPin = str(input())
      if(confirmYourPin not in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm,./;'[]{}\|`~!@#$%^&*()-_+=?<>:"):
        break
      else:
        print(' ')
        print('error')
  while(confirmYourPin != yourPin):
    print(' ')
    print('ERROR!')
    print(' ')
    confirmYourPin = str(input('Confirm your PIN: '))
  print(' ')
  print('Success')
  if(yourPin[0] == yourPin[1] and yourPin[1] == yourPin[2] and yourPin[2] == yourPin[3] and yourPin[3] == yourPin[4] and yourPin[4] == yourPin[5]):
    print('yourPin is an easy pin to break')
    yourPin = int(yourPin)
  else:
    yourPin = int(yourPin)
else:
  print('ERROR!')
  while(pinlength != 6):
    print('')
    print('please enter your pin again')
    yourPin = str(input())
    pinlength = len(yourPin)
  print(' ')
  confirmYourPin = str(input('confirm your PIN: '))
  for element in confirmYourPin:
    while element in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm,./;'[]{}\|`~!@#$%^&*()-_+=?<>:":
      print(' ')
      print('error')
      print(' ')
      confirmYourPin = str(input())
      if(confirmYourPin not in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm,./;'[]{}\|`~!@#$%^&*()-_+=?<>:"):
        break
      else:
        print(' ')
        print('error')
  while(confirmYourPin != yourPin):
    print(' ')
    print('ERROR!')
    print(' ')
    confirmYourPin = str(input('confirm your PIN: '))
  if(yourPin[0] == yourPin[1] and yourPin[1] == yourPin[2] and yourPin[2] == yourPin[3] and yourPin[3] == yourPin[4] and yourPin[4] == yourPin[5]):
    print('yourPin is an easy pin to break')
    yourPin = int(yourPin)
  else:
    yourPin = int(yourPin)

#this program will crack yourPin and also record how much time it would take

startTime = time.time()
loopCount = 0

#this program will crack the yourPin

class cracker:
  def code(p, loopCount):
    while(True):
      p = str(p)
      if(p[0] == p[1] and p[1] == p[2] and p[2] == p[3]):
        break
      else:
        p = int(p)
        while(loopCount != p):
          loopCount = loopCount + 1 
          print(' ')
          print(loopCount)
          if(loopCount == p):
            print(' ')
            print('cracked')
            break
        break
  code(yourPin, loopCount)

#this tells you how much time it took to crack yourPin

endTime = time.time()
elapsedTime = (endTime - startTime)
print(' ')
print('your pin is', yourPin)
print(' ')
print('it took', elapsedTime, 'seconds to crack your pin')
