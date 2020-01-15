lowLimit = ord('A')
highLimit = ord('z')
codeShift = 3
codeText = ""
vowels = 'aAeEiIoOuU'
specialLetters = 'yYzZxX'
subLetterE = ['!', '1']
subLetterA = ['@', '2']
subLetterI = ['#', '3']
subLetterO = ['$', '4']
subLetterU = ['%', '5']
specialLetterY = ['^', '6']
specialLetterZ = ['&', '7']
specialLetterX = ['*', '8']
plainText = input('Your Sentence:\n')
loopCount1 = 0
loopCount2 = 0
loopCount3 = 0
loopCount4 = 0
loopCount5 = 0
loopCount6 = 0
loopCount7 = 0
loopCount8 = 0



for letter in plainText:
  if letter.isalpha() == True:
    code = ord(letter)
    if letter not in vowels and letter not in specialLetters:
      if code >= lowLimit and code <= highLimit :
        code = code + codeShift
        if (code > highLimit):
          code = code - highLimit + lowLimit
      newLetter = chr(code)
    else:
      if letter in 'eE':
        letter = subLetterE[0]
        if loopCount1 >= 1:
          letter = subLetterE[1]
        loopCount1 += 1
      if letter in 'Aa':
        letter = subLetterA[0]
        if loopCount2 >= 1:
          letter = subLetterA[1]
        loopCount2 += 1
      if letter in 'iI':
        letter = subLetterI[0]
        if loopCount3 >= 1:
          letter = subLetterI[1]
        loopCount3 += 1
      if letter in 'oO':
        letter = subLetterO[0]
        if loopCount4 >= 1:
          letter = subLetterO[1]
        loopCount4 += 1
      if letter in 'uU':
        letter = subLetterU[0]
        if loopCount5 >= 1:
          letter = subLetterU[1]
        loopCount5 += 1
      if letter in 'yY':
        letter = specialLetterY[0]
        if loopCount6 >= 1:
          letter = specialLetterY[1]
        loopCount6 += 1
      if letter in 'xX':
        letter = specialLetterX[0]
        if loopCount7 >= 1:
          letter = specialLetterX[1]
        loopCount7 += 1
      if letter in 'zZ':
        letter = specialLetterZ[0]
        if loopCount8 >= 1:
          letter = specialLetterZ[1]
        loopCount8 += 1
      newLetter = letter
    codeText = codeText + newLetter
  else:
    codeText = codeText + letter
print('')
print('the encoded message is:\n', codeText)

code = open("encodedMessege.txt", 'w+')
code.write(codeText)
code.close()

#Decoder 

encodedFile = open("encodedMessege.txt", "r+")
theMessege = open("theMessege.txt", "w+")

oldText = ""
oldSubLetter = ['!', '1', '@', '2', '#', '3', '$', '4', '%', '5']
oldSpecialLetters = ['^', '6', '&', '7', '*', '8']
oldSubLetterE = ['!', '1']
oldSubLetterA = ['@', '2']
oldSubLetterI = ['#', '3']
oldSubLetterO = ['$', '4']
oldSubLetterU = ['%', '5']
oldSpecialLetterY = ['^', '6']
oldSpecialLetterZ = ['&', '7']
oldSpecialLetterX = ['*', '8']
loopCount = 0

for line in encodedFile:
  for letter in line:
    if letter.isalpha() == True:
      code = ord(letter)
      if code >= lowLimit and code <= highLimit :
        code = code - codeShift
        if code > highLimit:
          code = code + highLimit - lowLimit
          code = code - 6
      oldLetter = chr(code)
      loopCount += 1
    elif letter in oldSubLetter or letter in oldSpecialLetters:
      if letter in oldSubLetterE:
        letter = 'e'
      if letter in oldSubLetterA:
        letter = 'a'
      if letter in oldSubLetterO:
        letter = 'o'
      if letter in oldSubLetterI:
        letter = 'i'
      if letter in oldSubLetterU:
        letter = 'u'
      if letter in oldSpecialLetterX:
        letter = 'x'
      if letter in oldSpecialLetterZ:
        letter = 'z'
      if letter in oldSpecialLetterY:
        letter = 'y'
      oldLetter = letter
      loopCount += 1
    else:
      oldLetter = letter
    oldText = oldText + oldLetter

theMessege.write(oldText)

print('')
print('the message was:\n', oldText)
print('')
print('the amount of characters in your text was:\n', loopCount)

theMessege.close()
encodedFile.close()
