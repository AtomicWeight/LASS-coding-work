teams = ["Raptors","Leafs","Jays","TFC","Argos","Rock"]
fileHandle = open("answers.txt", "w+")
fileHandle.write("Teams I Like:\n")
stopProgram = False
numAnswers = 0
for team in teams:
  answer = ""
  while not((answer == "yes") or (answer == "no")):
    print("Please answer yes or no (or type stop to end the program)")
    answer = input("Do you like the %s? " %(team))
    if answer == 'stop':
      stopProgram = True
      break
    elif((answer == 'yes') or (answer == 'no')):
      numAnswers += 1
      fileHandle.write("Team %s, answer %s\n" %(team, answer))
  if stopProgram == True:
    break
fileHandle.close()
print("You have answered %d questions!" % numAnswers)
