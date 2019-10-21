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
  confirmYourPin = int(input('confirm your PIN: '))
  while(confirmYourPin != yourPin):
    print(' ')
    print('ERROR!')
    print(' ')
    confirmYourPin = int(input('confirm your PIN: '))
  print(' ')
  print('success')
else:
  print('ERROR!')

#this program will crack yourPin and also record how much time it would take

startTime = time.time()
loopCount = 0

#this program will crack the yourPin

while(loopCount != yourPin):
  loopCount += 1 
  print(' ')
  print(loopCount)
print(' ')
print('your pin is %d' % loopCount)

#this tells you how much time it took to crack yourPin

endTime = time.time()
elapsedTime = (endTime - startTime)
print(' ')
print('it took', elapsedTime, 'seconds to crack your pin')
