# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 21:16:36 2022



Problem Definition:
use picture of an ocean and you are asked to find how many islands are there in
the ocean. The picture can be visualized as a 2D grid where each cell in the grid represents a pixel in
the picture. If a pixel is part of the water (or sea) then it is represented as 1 in the grid while a land (or
island) pixel is represented as 0 .


function findIslandNumber
  This function to find number of island in picture (2D grid)
  input:
    @ grid: (2D grid) 2D list reprisent island(0) and ocean(1)
  output:
    @ : number of island
    Algorithm:
    1.defind number of row and colume
    2.use if statement if grad is empty or the row 0 will return 0
    3.defind number of island to count the number of island and defult value is 0
    4.use nusted loop to find for evey row then every colume for evey point in grid or list 
     4,1 if this point is land(0) well call the CheckIslandSize() function, and add 1 to number of island
    5.return number of island



function CheckIslandSize
  This function to check Land cells/pixels that are connected (i.e. neighbours)
  input:
    @ grid: (2D grid) 2D list reprisent island(0) and ocean(1)
    @ x: number of row this point 
    @ y: number of colume for this point
    @ row: number of row in grid
    @ col: number of colume in grid
    Algorithm:
    1. use if statement to check for point you aredy visted, if statmunt is true well rerutn nothing(stop function)
    2. convert value of this point in grad to * to market it (this point is already visted)
    3. recursive call function 8 CheckIslandSize() time to check if islands is connected(neighbours) 
       3.1.from below the original point
           3.2 from top the original point
           3.3 from right the original point
           3.4 from left the original point
           3.5 from left,below the original point
           3.6 from left,top the original point
           3.7 from right,top the original point
           3.8 from right,below the original point



function findIslandPoint
  This function to find the size of each island and the pixels that form each island.
  input:
    @ grid: (2D grid) 2D list reprisent island(0) and ocean(1)
    Algorithm:
    1.defind number of row and colume
    2.use if statement if grad is empty or the row 0 will return 0
    3.defind number of island to count the number of island and defult value is 0
    4.use nusted loop to find for evey row then every colume for evey point in grid or list 
     4,1 in the nusted loop if this point is land(0) well call the CheckIslandPoint() function, and add 1 to number of island


function CheckIslandPoint
  This function to check Land cells/pixels that are connected (i.e. neighbours),
   and save pixels(point) in list(listPoint) for every island.
  input:
    @ grid: (2D grid) 2D list reprisent island(0) and ocean(1)
    @ x: number of row this point 
    @ y: number of colume for this point
    @ row: number of row in grid
    @ col: number of colume in grid
    @ numberOfIsland : number of island 
    output:
    @ : (save pixels(point) in list(listPoint) for every island) in listPoint
    Algorithm:
    1. use if statement to check for point you aredy visted, if statmunt is true well rerutn nothing(stop function)
    2. use if statement to if this poit is land well add all info (pixels) in listPoint
    3. convert value of this point in grad to * to market it (this point is already visted)
    4. recursive call function 8 CheckIslandSize() time to check if islands is connected(neighbours) 
       4.1 from below the original point
           4.2 from top the original point
           4.3 from right the original point
           4.4 from left the original point
           4.5 from left,below the original point
           4.6 from left,top the original point
           4.7 from right,top the original point
           4.8 from right,below the original point

    
function main
  This function to use print output (all info for isalnd) ,
  use turtle graphics to display the picture where each island.
    Algorithm:
    1.defind listPoint as global (to use list outside function main)
    2. defind number of grid representing (n*n):
    3. defind grid as array square (n*n) have all ones only
      3.1 use nested loop for every point in array and for every point convert value from 1 to 1 or 0 as randomly.
    4. print grad 
    5. convert grad form array to list 
    6. copy 2D list(grad) to grad2 by deepcopy
    7. call function findIslandNumber() and save number of island(land)
    8. create empty list for save point for every island data in (global listPoint)
      8.1 change size of listPoint list to number of isalnd (to save info point in it) by use for statement loop number of island
    9. print output of island number
    10.call  findIslandPoint() function
    11.defind count to print output by number of island en every line 
      11.1 print output statement 
      11.2 use for loop and print by number of island ,every time use loop well print island number by (count)
      , size of island point by (listPoint[index]), sorted pixels for every island by (listPoint[index])
    
    12.set title name of turtle window
    	12.1 set name of title (myTurtle)
      12.2 set speed for title(myTurtle)
      12.3 set list of color (lstcol)
          12.4 set pen color as white
    13. use for statement and repeat every number of island
      13.1 change fill color for every island from list (lstcol)
      13.2 use for statement and repeat every number of point in this island
      13.3 up pen in myTurtle
      13.4 set point(Pixel) and conver to string
      13.5 use split and replace to get Pixel value (x,y),and set x,y
      13.6 use x,y and convert them to intger (Pixel info) and multiple y by 30 and x by -30 to go in this point(Pixel)
      13.7 start draw the this islands
      13.8 use hideturtle() then turtle.done() and turtle.bye()

      
"""

from copy import copy, deepcopy  # to copy 2D list
import numpy as np 
import turtle
import random




def findIslandNumber(grid):
    
 row = len(grid) #set number of raw
 col = len(grid[0]) #set number of colume
 if row == 0:
     return 0
 
 numberOfIsland=0 #defind number of island
 
 for x in range(row):
        for y in range(col):
            if grid[x][y] == 0:
                CheckIslandSize(grid, x, y ,row ,col)  #check for point for every island
                numberOfIsland += 1
                
 return numberOfIsland

def CheckIslandSize(grid, x, y , row,col):
    if x<0 or x>=row or y<0  or y>=col or grid[x][y] != 0:#check for point you aredy visted
        return
    grid[x][y] = '*'    # islands you visited use * to mark it
    #recursive call function 8 time to check if islands is connected(neighbours)
    CheckIslandSize(grid, x+1, y,row ,col)  #Down
    CheckIslandSize(grid, x-1, y,row ,col)   #top
    CheckIslandSize(grid, x, y+1,row ,col)   #right
    CheckIslandSize(grid, x, y-1,row ,col)   #left
    CheckIslandSize(grid, x+1, y-1,row ,col)   #left,down
    CheckIslandSize(grid, x-1, y-1,row ,col)   #left,top
    CheckIslandSize(grid, x-1, y+1,row ,col)   #right,top
    CheckIslandSize(grid, x+1, y+1,row ,col)   #right,down
    
    



def findIslandPoint(grid):
    
 row = len(grid)  #set number of row
 col = len(grid[0]) #set number of colume
 if row == 0:
     return 0
 
 numberOfIsland=0  #defind number of island
 
 for x in range(row):
        for y in range(col):
            if grid[x][y] == 0:
                 #check for point for every island and enter point for every island
                CheckIslandPoint(grid, x, y ,row ,col,numberOfIsland)   
                
                numberOfIsland += 1 # to count every island
                


def CheckIslandPoint(grid, x, y , row,col,numberOfIsland):
    if x<0 or x>=row or y<0  or y>=col or grid[x][y] != 0: #check for point you aredy visted
        return 
    
    
    if grid[x][y]== 0 :
      listPoint[numberOfIsland].append((x,y))  # to count point for every island
      
    
    grid[x][y] = '*'  # islands you visited use * to mark it
    
    #recursive call function 8 time to check if islands is connected(neighbours)
    CheckIslandPoint(grid, x+1, y,row ,col,numberOfIsland)  #Down
    CheckIslandPoint(grid, x-1, y,row ,col,numberOfIsland)   #top
    CheckIslandPoint(grid, x, y+1,row ,col,numberOfIsland)   #right
    CheckIslandPoint(grid, x, y-1,row ,col,numberOfIsland)   #left
    CheckIslandPoint(grid, x+1, y-1,row ,col,numberOfIsland)   #left,down
    CheckIslandPoint(grid, x-1, y-1,row ,col,numberOfIsland)   #left,top
    CheckIslandPoint(grid, x-1, y+1,row ,col,numberOfIsland)   #right,top
    CheckIslandPoint(grid, x+1, y+1,row ,col,numberOfIsland)   #right,down





def main():  

 global listPoint  # to save all point when use it in another function
 
 n = 5  # for n * n  grid representing
 # to random  grid representing as (array)
 grid = np.ones((n, n), dtype = int)  
 for j in range(0,n-1):
    for i in range(0,n-1):
        randomnumber= random.randint(0, 1)
        grid[j][i]=randomnumber 

 print(grid ,"\n\n") # print grad
 
 
 grid=grid.tolist()   #convert form array to list 
 
 
 grid2 = deepcopy(grid)  # to copy 2D list
 numberisland=findIslandNumber(grid)  # call  findIslandNumber() function
 listPoint = [] #create empty list for save point for every island data 
 for i in range(numberisland):
    listPoint.append([])   # change size of the list by number of island
    
 print("The ocean has ",numberisland," island(s) as follows:") # print output
 findIslandPoint(grid2)  #call  findIslandPoint function
 count = 0 #for print output by number of island
 print("Island No.         Size        Pixels") 
 for j in range(0,numberisland):
     count +=1
     print(count , "                  ",len(listPoint[j]),"       ",sorted(listPoint[j]))
 
 turtle.title("Island")  # title name of turtle window
 myTurtle = turtle.Turtle() 

 myTurtle.speed(100)


 lstcol = ["dark olive green", "forest green","purple", "pink", "brown" ,"light salmon","maroon" ,"gold"] #list for color for every island

 myTurtle.pencolor('white') #color pen


 for j in range(0,numberisland): # start draw island and ocean
   myTurtle.fillcolor(lstcol[j])  
   for i in range(0,len(listPoint[j])):
      myTurtle.up
      point=str(listPoint[j][i])
      xpoint = point.split(",")
      x=xpoint[0].replace("(","")
      y=xpoint[1].replace(")","")
      myTurtle.goto((int(y)*30), int(x)*-30) 
      myTurtle.down()
      myTurtle.pencolor(lstcol[j])
      myTurtle.begin_fill()
      myTurtle.forward(30)
      myTurtle.right(90)
      myTurtle.forward(30)
      myTurtle.right(90)
      myTurtle.forward(30)  
      myTurtle.right(90)
      myTurtle.forward(30)   
      myTurtle.end_fill()
      myTurtle.up()
      myTurtle.home()
      
      
      
 myTurtle.hideturtle()
 turtle.done()
 turtle.bye()
 

     
main()  # call main function
     
    
 

    
    
 
 
 
 
 
 
 