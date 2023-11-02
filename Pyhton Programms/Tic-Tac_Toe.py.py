import random, os
grid = [[" "," "," "],[" "," "," "],[" "," "," "]]
row = random.randint(0,2)
col = random.randint(0,2)
def displayBanner():
  print("XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO")
  print("O                              X")
  print("X     Noughts and Crosses      O")
  print("O                              X")
  print("XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO")
  print("")

#Defining the grid a 2D array (3x3)!
def displayGrid(grid):
  print(" " + grid[0][0] + " | " + grid[0][1] + " | " + grid[0][2])
  print("-----------")
  print(" " + grid[1][0] + " | " + grid[1][1] + " | " + grid[1][2])
  print("-----------")
  print(" " + grid[2][0] + " | " + grid[2][1] + " | " + grid[2][2])

def place_nought():
    row = random.randint(0,2)
    col = random.randint(0,2)
    if grid[row][col]!=" ":
        
        place_nought()
    else:
        grid[row][col] = "X"

def place_Zero():
    row = int(input("Row: "))
    col = int(input("Col: "))
    if grid[row][col] != " ":
        place_Zero()
    else:
        grid[row][col] = "O"
        
        
        
  
def checkGrid(grid):
       #Checking the first row...
   if grid[0][0]=="X" and grid[0][1]=="X" and grid[0][2]=="X":
        print("Three Xs in a row.")
        exit()
        
   elif grid[0][0]=="O" and grid[0][1]=="O" and grid[0][2]=="O":
        print("Three Os in a row.")
        exit()
        
   #Checking the second row...
   if grid[1][0]=="X" and grid[1][1]=="X" and grid[1][2]=="X":
        print("Three Xs in a row.")
        exit()
        
   elif grid[1][0]=="O" and grid[1][1]=="O" and grid[1][2]=="O":
        print("Three Os in a row.")
        exit()
        
   #Checking the third row...
   if grid[2][0]=="X" and grid[2][1]=="X" and grid[2][2]=="X":
        print("Three Xs in a row.")
        exit()
        
   elif grid[2][0]=="O" and grid[2][1]=="O" and grid[2][2]=="O":
        print("Three Os in a row.")
        exit()
   
   #Checking the first column
   if grid[0][0]=="X" and grid[1][0]=="X" and grid[2][0]=="X":
        print("Three Xs in a column.")
        exit()
        
   elif grid[0][0]=="O" and grid[1][0]=="O" and grid[2][0]=="O":
        print("Three Os in a column.")
        exit()
      
   #Checking the second column
   if grid[1][0]=="X" and grid[1][1]=="X" and grid[1][2]=="X":
        print("Three Xs in a column.")
        exit()
        
   elif grid[1][0]=="O" and grid[1][1]=="O" and grid[1][2]=="O":
        print("Three Os in a column.")
        exit()
   
   #Checking the third column
   if grid[2][0]=="X" and grid[2][1]=="X" and grid[2][2]=="X":
        print("Three Xs in a column.")
        exit()
        
   elif grid[2][0]=="O" and grid[2][1]=="O" and grid[2][2]=="O":
        print("Three Os in a column.")
        exit()
        
   #Checking the first diagonale
   if grid[0][0]=="X" and grid[1][1]=="X" and grid[2][2]=="X":
        print("Three Xs in a column.")
        exit()
        
   elif grid[0][0]=="O" and grid[1][1]=="O" and grid[2][2]=="O":
        print("Three Os in a column.")
        exit()
 
   #Checking the second diagonale
   if grid[0][2]=="X" and grid[1][1]=="X" and grid[2][0]=="X":
        print("Three Xs in a column.")
        exit()
        
   elif grid[0][2]=="O" and grid[1][1]=="O" and grid[2][0]=="O":
        print("Three Os in a column.")
        exit()
   
def start():
    while(1):
        os.system("cls")  
        displayBanner()
        displayGrid(grid)
        place_nought()
        place_Zero()
        checkGrid(grid)
        
start()
    
    

    
   






  