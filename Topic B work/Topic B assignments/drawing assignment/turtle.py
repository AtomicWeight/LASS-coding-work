import turtle 
mP = turtle.Turtle()
mP.color('black')
mP.speed(-1)

position = 0
image = int(input('please input the numbers of images you want(it must be in between 0 and 6):\n'))

if(image > 6 or image < 0):
  while(image > 6 or image < 0):
    image = int(input('the number of images must be in between 0 and 6:\n'))
  print('images shall now form')
else:
  print('images shall now form')    

for x in range(image):
  count = 0

  while(count <= 270):
    mP.left(1)
    mP.forward(100)
    mP.right(90)
    mP.forward(100)
    mP.right(90)
    mP.forward(100)
    mP.forward(100)
    mP.right(90)
    mP.forward(100)
    mP.right(90)
    mP.forward(100)
    count += 1

  position += 284

  mP.up()
  mP.goto(position,0)
  mP.down()
  
print('done')
