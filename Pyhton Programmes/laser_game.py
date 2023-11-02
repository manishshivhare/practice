
import random, time, os

def drawMaze():
  print("")
  print("    1 2 3 4 5 6 7 8 9 10")
  for i in range(0,12):
    line = ""
    for j in range(0,12):
       line = line + maze[i][j]
    if i>0 and i<10:
      print(" " + str(i) + line)
    elif i==0 or i==11:
      print("  " + line)
    elif i==10:
      print("10" + line)
      
def placeBombs(numberOfBombs):
  for i in range(0,numberOfBombs):
    row = random.randint(1,10)
    col = random.randint(2,9)
    maze[row][col] = "<>"

def place_reflector(row_ref, col_ref, dir):
  if dir == 1:
    maze[row_ref][col_ref] = "/"
  elif dir == 2:
    maze[row_ref][col_ref] = "\\"
            
def shoot():
  global direction
  state="shooting"
  row = source[0]
  col = source[1]
  
  while state=="shooting":
      os.system("cls")
      if direction=="right":
        col+=1
      elif direction == "left":
        col-=1
      elif direction =="up":
        row-=1
      elif direction == "down":
        row+=1
        
      if maze[row][col]=="  ":
        print("")
        maze[row][col]=">>"
      elif maze[row][col]=="[]":
        print("Exit Gate Reached! Level Cleared!")
        state="win"
      elif maze[row][col]=="<>":
        print("Laser beam hits a bomb! Game Over!")
        state="lost"
      elif maze[row][col]==" |" or maze[row][col]=="| " or maze[row][col]=="--":
        print("Laser beam hits a wall! Game Over!")
        state="lost"
      elif maze[row][col]==">>":
        print("Laser beam hits it source! Game Over!")
        state="lost"
      elif maze[row][col]=="/":
            if direction == "down":
              direction = "left"
            elif direction == "up":
              direction = "right"
            elif direction == "left":
              direction = "down"
            elif direction == "right":
              direction = "up"
      elif maze[row][col]=="\\":
            if direction == "down":
              direction = "right"
            elif direction == "up":
              direction = "left"
            elif direction == "left":
              direction = "up"
            elif direction == "right":
              direction = "down"
            
            
            
      drawMaze()
      time.sleep(0.2)    
            
maze = [[" -","--","--","--","--","--","--","--","--","--","--","- "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" |","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","| "],
        [" -","--","--","--","--","--","--","--","--","--","--","- "]
       ]
source = (random.randint(1,10),0)
direction = "right"
maze[source[0]][source[1]] = ">>"
exit = (random.randint(1,10),11) 
maze[exit[0]][exit[1]] = "[]"

print("######### Wlecome to Game ############")
level =int(input("Difficulty Level\n1.Easy\n2.Medium\n3.Hard\n"))
if level == 1:
  placeBombs(4)    
elif level == 2:
  placeBombs(6)    
elif level == 3:
  placeBombs(8)   
else:
  print("wrong Selection") 

drawMaze()    
count_ref = int(input("Count of Reflector: "))
while(count_ref!=0):
      row_ref = int(input("Row: "))
      col_ref = int(input("Col: "))
      dir = int(input("1. '/' 2. '\\': "))
      place_reflector(row_ref, col_ref, dir)
      count_ref-=1
shoot()

      
  

            
      
      
      
                      
      

          




      

      


