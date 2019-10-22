import time

#this is where you enter a pin number stored in yourPin

print('enter your PIN')
print(' ')
yourPin = str(input())
pinlength = len(yourPin)

#check to see if yourPin is valid or not 

if(pinlength == 4):
  yourPin = int(yourPin)
  print(' ')
  confirmYourPin = int(input('Confirm your PIN: '))
  while(confirmYourPin != yourPin):
    print(' ')
    print('ERROR!')
    print(' ')
    confirmYourPin = int(input('Confirm your PIN: '))
  print(' ')
  print('Success')
else:
  print('ERROR!')
  while(pinlength != 4):
    print('')
    print('please enter your pin again')
    yourPin = str(input())
    pinlength = len(yourPin)
  print(' ')
  yourPin = int(yourPin)
  confirmYourPin = int(input('confirm your PIN: '))
  while(confirmYourPin != yourPin):
    print(' ')
    print('ERROR!')
    print(' ')
    confirmYourPin = int(input('confirm your PIN: '))

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
  code(yourPin, loopCount)

#this tells you how much time it took to crack yourPin

endTime = time.time()
elapsedTime = (endTime - startTime)
print(' ')
print('your pin is', yourPin)
print(' ')
print('it took', elapsedTime, 'seconds to crack your pin')

#this tells you how much time it took to crack yourPin

endTime = time.time()
elapsedTime = (endTime - startTime)
print(' ')
print('it took', elapsedTime, 'seconds to crack your pin')
