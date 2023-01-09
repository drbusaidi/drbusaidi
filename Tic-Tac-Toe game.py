# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from random import randint
class Game:
    def __init__(self):
     self.board = ['', '', '', '', '', '', '', '', '']
     

    def displayBoard(self):
         print("-+-+-")
         print(self.board[0],"|",self.board[1],"|",self.board[2])
         print("-+-+-")
         print(self.board[3],"|",self.board[4],"|",self.board[5])
         print("-+-+-")
         print(self.board[6],"|",self.board[7],"|",self.board[8])
         print("-+-+-")
     
    def updateBoard(self,position,XorO):
            
            position=int(position)-1
            self.board[position]=XorO
            
        
        
    def checkWinningMatch(self):
        
            
            # we have 8 possible winning configurations (horizontally, vertically or diagonally)are available in board.
            #if any one of this is true return value
            # this for check Winning Match vertically
            if self.board[0]==self.board[1] and self.board[1]==self.board[2] and self.board[0]!='' :
                return self.board[0]
            if self.board[3]==self.board[4] and self.board[4]==self.board[5] and self.board[3]!='' :
                return self.board[3]
            if self.board[6]==self.board[8] and self.board[8]==self.board[7] and  self.board[7]!='':
                return self.board[6]
            
            # this for check Winning Match diagonally
            if self.board[2]==self.board[4] and self.board[4]==self.board[6] and self.board[2]!='':
                return self.board[2]
            if self.board[0]==self.board[4] and self.board[4]==self.board[8] and self.board[0]!='':
                return self.board[0]
            
            # this for check Winning Match horizontally
            if self.board[0]==self.board[3] and self.board[3]==self.board[6] and self.board[0]!='':
                return self.board[0]
            if self.board[1]==self.board[4] and self.board[4]==self.board[7] and self.board[1]!='':
                return self.board[1]
            if self.board[2]==self.board[5] and self.board[5]==self.board[8] and  self.board[2]!='':
                return self.board[2]
            return False
    def checkFullBoard(self):
        for x in self.board:
            if x=='':
                return True
        return False
       
        

      
def main():    
    GAME1=Game()
    
    x=randint(1, 2)
    if x==1:
        player1='O'
        player2='X'
    else:
        player1='X'
        player2='O'
        
    while GAME1.checkFullBoard():
        
            
        GAME1.displayBoard()
        
        
        if player1=='O':
           player1='X'
        else:
             player1='O'
        

        
        if GAME1.checkWinningMatch()!=False:
            print("================== GAME OVER ===================")
            print("Player ",GAME1.checkWinningMatch(), "wins the game!")
            break
        if GAME1.checkFullBoard() ==False:
            print("Game draw!")
            
        print("Player ",player1,"enter the position:",end="")
        position=input()
        print("—-----------------------------------------------")
        GAME1.updateBoard(position, player1)
                
main()            