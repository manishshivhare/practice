# 2D Dice Grid Scoring Algorithm - http://www.101computing.net/2d-dice-grid-scoring-algorithm/

from random import randint
import psutil

grid = []

#A procedure to generate/shake a new 4 by 4 grid of 16 dice 
def resetGrid():
  global grid
  grid = []
  for row in range(4):
    grid.append([])
    for col in range(4):
      dice = randint(1,6)
      grid[row].append(dice)
  
#A procedure to display the dice grid
def displayGrid():
  global grid
  for row in range(4):
    st="| " 
    for col in range(4):
      st = st + str(grid[row][col]) + " | "
    print(st)

#A function to check if a number is an even number
def isEven(number):
  if number%2 == 0:
    return True
  else:
    return False

#A function to check if a number is an odd number
def isOdd(number):
  if number%2 == 1:
    return True
  else:
    return False

####### Main Program Starts Here #######
resetGrid()
displayGrid()
score = 0

#Check if the four corners are even numbers
if isEven(grid[0][0]) and isEven(grid[0][3]) and isEven(grid[3][0]) and isEven(grid[3][3]):
  print("Four even corners! +20pts")
  score = score + 20

#Complete the grid scoring algorithm here...

  
print("\nGrid score: " + str(score) + " pts.")