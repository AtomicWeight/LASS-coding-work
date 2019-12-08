lowLimit = ord('A')
highLimit = ord('z')
codeShift = 3
codeText = ""
vowels = 'aAeEiIoOuU'
subLetterE = ['!', '1']
subLetterA = ['@', '2']
subLetterI = ['#', '3']
subLetterO = ['$', '4']
subLetterU = ['%', '5']
plainText = input('Your Sentence:\n')
loopCount1 = 0
loopCount2 = 0
loopCount3 = 0
loopCount4 = 0
loopCount5 = 0



for letter in plainText:
  if letter.isalpha() == True:
    code = ord(letter)
    if letter not in vowels:
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
      newLetter = letter
    codeText = codeText + newLetter
  else:
    codeText = codeText + letter
print('')
print('the encoded message is:\n', codeText)

#Decoder

oldText = ""
oldSubLetter = ['!', '1', '@', '2', '#', '3', '$', '4', '%', '5']
oldSubLetterE = ['!', '1']
oldSubLetterA = ['@', '2']
oldSubLetterI = ['#', '3']
oldSubLetterO = ['$', '4']
oldSubLetterU = ['%', '5']
loopCount = 0

for letter in codeText:
  if letter.isalpha() == True:
    code = ord(letter)
    if code >= lowLimit and code <= highLimit :
      code = code - codeShift
      if (code > highLimit):
        code = code + highLimit - lowLimit
        code = code - codeShift
    oldLetter = chr(code)
  else:
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
    oldLetter = letter
  oldText = oldText + oldLetter
  loopCount += 1

print('')
print(' the message was:\n', oldText, '\n', 'the amount of characters in your text was\n', loopCount)
