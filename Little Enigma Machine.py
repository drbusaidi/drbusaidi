# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 19:22:24 2022

@author: JABER


Problem Definition:
use (The Little Enigma Machine) to decode and encode, 
basic operation of the Enigma machine is to substitute each letter from
the original plaintext message with another letter and must use oop to solve Problem.

        
function __init__
  This function to defind value of key in object
  input:
    @ Key: set value Key of object
    Algorithm:
    1.defind number of key in object





        
function Encrypt
  This function to Encrypt message 
  input:
    @ message : text messages
    @  n : number of Encrypt 
  output:
    @ newmessage :text messages Encrypt , defult value is None
    Algorithm:
    1.Check n value if none or not (overlaping)
    2.set value of key and  alphabetnew is empty
    3.use for statement will be repeat 26-key
     3.1 save all letter from  26-key of alphabet in alphabetnew
     3.2 save other letter in the end of alphabetnew 
    4.use for statement repeat for every Encrypt(n value)
    5.use for statement will be repeat length of message 
    6.use if statement to determine this is Letter only ,else add space in newmessage
    7.get Letter value by index i and convert to upper Letter
    9.use  for statement to repeat 26 time to compare litter with modified letter
    10.find index of value to find index in modified letter
    11.save output in newmessage for all letter in newmessage
    12.update message value
    13 return output
    
    
    
            
function Decrypt
  This function to Decrypt message 
  input:
    @ message : text messages
    @  n : number of Decrypt , defult value is None
  output:
    @ newmessage :text messages Decrypt 
    Algorithm:
    1.Check n value if none or not (overlaping)
    2.set value of key and  alphabetnew is empty
    3.use for statement will be repeat 26-key
     3.1 save all letter from  26-key of alphabet in alphabetnew
     3.2 save other letter in the end of alphabetnew 
    4.use for statement repeat for every Decrypt(n value)
    5.use for statement will be repeat length of message 
    6.use if statement to determine this is Letter only ,else add space in newmessage
    7.get Letter value by index i and convert to upper Letter
    9.use  for statement to repeat 26 time to compare litter with modified letter
    10.find index of value to find index in modified letter
    11.save output in newmessage for all letter in newmessage
    12.update message value
    13 return output
    
    
    
            
function updateKey
  This function to update key vlaue of object
  input:
    @ Key : set new value Key of object
    Algorithm:
    1.update valur of Key of this object

    
    
    

"""




alphabet = "abcdefghijklmnopqrstuvwxyz" #Liter from a to z by ordar


class Engima: 

    def __init__(self,Key): 
        self.Key = Key   #every class must have Key for Encrypt or Decrypt

    def Encrypt(self,message, n = None):
        if n==None: # for overlaping
            n=1
        
        key=self.Key #defind key by use class key value
        alphabetnew=""  #create empty string to save modified letters by order
        # start save modified letters in alphabetnew
        for i in range(key,len(alphabet)):  #for statement will be repeat 26-key
            alphabetnew+=alphabet[i] #save modified letter in alphabetnew
        for i in range(0,key) :  #for statement will be repeat (key value) 
            alphabetnew+=alphabet[i]  #save modified letter in alphabetnew
            # end of save modified letters in alphabetnew       

        for i in range(n): # for repeat n time or for every Encrypt
            newmessage=""   #create empty string to output (Encrypt text)
            for i in range(0,len(message)):  #for statement will be repeat length of message 
               
                if not message[i].isspace():   #to determine this is Letter only
                   litermessage=message[i].upper() #get Letter value by index i and convert to upper Letter
                   for x in range(0,len(alphabetnew)-1):# for repeat 26 time to compare litter with modified letter
                       index=0 # deflut value of index is 0
                       if litermessage == alphabet[x].upper(): #find index of value to find index in modified letter
                           index=x 
                           break
                   newmessage+=alphabetnew[index].upper() # save output in newmessage for all letter in newmessage
                else:
                    newmessage+=' '    #to add space in newmessage
            message=newmessage 
        return newmessage # return Encrypt value(Encrypt message)
    
     
    def Decrypt(self,message, n=None):
        if n==None: # for overlaping
            n=1
        key=self.Key #defind key by use class key value
        alphabetnew=""  #create empty string to save modified letters by order
        # start save modified letters in alphabetnew
        for i in range(key,len(alphabet)):  #for statement will be repeat 26-key
            alphabetnew+=alphabet[i] #save modified letter in alphabetnew
        for i in range(0,key) :  #for statement will be repeat (key value) 
            alphabetnew+=alphabet[i]  #save modified letter in alphabetnew
            # end of save modified letters in alphabetnew   
            
        for i in range(n): # for repeat n time or for every Decrypt
            newmessage=""   #create empty string to output (Decrypt text)
            for i in range(0,len(message)):  #for statement will be repeat length of message 
               
                if not message[i].isspace():   #to determine this is Letter only
                   litermessage=message[i].upper() #get Letter value by index i and convert to upper Letter
                   for x in range(0,len(alphabetnew)-1):# for repeat 26 time to compare litter with modified letter
                       index=0 # deflut value of index is 0
                       if litermessage == alphabetnew[x].upper(): #find index of value to find index in modified letter
                           index=x 
                           break
                   newmessage+=alphabet[index].upper() # save output in newmessage for all letter in newmessage
                else:
                    newmessage+=' '    #to add space in newmessage
            message=newmessage 
        return newmessage # return Decrypt value(Decrypt message)
    
    def updateKey(self,Key): #update key vlaue
        self.Key=Key
        



#test output a,b

sm=Engima(5)


message="HELLO WORLD"
print ("PLAINTEXT:  ",message)
x=sm.Encrypt(message)
print("CIPHERTEXT: ",x)
print("PLAINTEXT:  ", sm.Decrypt(x))
print("\n")


#test output d,e
message2="A"
n=2
print ("PLAINTEXT:  ",message2)
x=sm.Encrypt(message2,n)
print("CIPHERTEXT: ",x)
print("PLAINTEXT:  ", sm.Decrypt(x,n))

print("\n")
#test output f
sm.updateKey(4)
message3="message"
print ("PLAINTEXT:  ",message3)
x=sm.Encrypt(message3)
print("CIPHERTEXT: ",x)




      
    
 
    
