from socket import *
import random


class Splitt:
    def __init__(self, phrase):
        self.phrase = phrase

    def spliting(self):
        
        x = list(self.phrase)
        return x

    def packets(self):
        floor = len(self.phrase)//4
        normal = len(self.phrase)/4
        
        n = 0
        if (floor == normal):
            n = floor
        else:
            n = floor + 1

        packetlist = []
        for i in range(n):
            packetlist.append([0,0,0,0,0])
        
        lengthoflist = len(self.phrase)
        i1 = 0
        i3 = 0
        while i1 < n :
            i2 = 0
            while i2 < (len(packetlist[0])-1):
                if(i3 < lengthoflist):
                    packetlist[i1][i2] = self.phrase[i3]

                i3 = i3 + 1
                i2 = i2 + 1
            i1 = i1 + 1
        print(packetlist)
        return packetlist
    def converttostring(self,packetlist1):
        self.packetlist1 = packetlist1
        string1 = ''
        for i in packetlist1:

            string1 += str(i)
        return string1
    

class Checksum:
    def __init__(self, packet):
        self.packet = packet
    
    def sum(self):
        n = 0 
        x = 0
        sum = 0
        while x < len(self.packet)-2:
            sum = sum + ord(self.packet[x])
            x = x + 1
        sum = sum % 256
        self.packet[len(self.packet) -1] = sum
        n = n + 1
        return self.packet

        
    def sum_after_recive(self,packetafter):
        self.packetafter = packetafter
        sum = 0
        x = 0
        while x < len(self.packetafter)-2:
            sum = sum + ord(self.packetafter[x])
            x = x + 1
        sum = sum % 256
        if(self.packetafter[len(self.packetafter) -1] == sum):
            return packetafter
        else:
            
            print('packet is corrupted!!!!')
            


alphabet = "abcdefghijklmnopqrstuvwxyz0123456789" #Liter from a to z by ordar


class encryption: 

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
                   newmessage+=alphabet[index] # save output in newmessage for all letter in newmessage
                else:
                    newmessage+=' '    #to add space in newmessage
            message=newmessage 
        return newmessage # return Decrypt value(Decrypt message)
    
    def updateKey(self,Key): #update key vlaue
        self.Key=Key



def main():
    start = True
    serverPort = 12000
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print("The server is ready to receive")
    connectionSocket, addr = serverSocket.accept()
    connected = connectionSocket.recv(1024)
    if connected.decode() == 'connect':
        print('connected')
        start = False
        sent = 'connectedd'
        connectionSocket.send(sent.encode())
        randkey = random.randrange(1, 26)
        strrandkey = str(randkey)
        connectionSocket.send(strrandkey.encode())
        dencrypt = encryption(randkey)
        print('encryption key is: '+strrandkey)
    xxx = True

    while 1:
        if(xxx):
            
            packetlistlength = connectionSocket.recv(1024)
            packetlistlength1 = packetlistlength.decode()

            xxx = False
            cc = 0
            liststr = []
            
            msgafter = ''
            
            
        
        message = connectionSocket.recv(1024)
        message = message.decode()
        
        decryptmessage = dencrypt.Decrypt(message)
        
        list1 = []
        list1 = list(decryptmessage)
        
        list2 = ['','','','','']
        
        x = 0
        z = True
        i = 0
        str2= ''
        while z:
            if(i <=  3):
                list2[i] = list1[i]
                i +=1
            if(i >= 4 and i < len(list1)):
                str2 += list1[i]
                i += 1
            if(i== len(list1)):
                z = False
        
        list2[4] = int(str2)
        message1 = Checksum(list2).sum_after_recive(list2)
        
        
        j = 0
        while j <= len(message1)-1:
            if(str(message1[j]).isalpha() or message1[j] == ' '):
                msgafter = msgafter + message1[j]
            j = j + 1

        
        cc += 1
        if(cc == int(packetlistlength1)):   
            print(msgafter)
            xxx = True
        
    
    connectionSocket.close()


main()