import random 

#Show options
print("rock , paper , scissor")

#Number of games
while True :
     

#Select option
    while True :
        enter=input("Start :")
        enter=enter.lower()
#find bad input

        if enter[0]!="r" and enter[0]!="s" and enter[0]!="p" :
         print("Enter again!! You entered incorrectly")
        
#Bad entry not found        
        elif True :
         break

#Robot selection    
    play=["rock","paper","scissor"]
    play2= random.choice(play)
    print("computer selection is " , play2)


#Determine the winne


    if enter[0]=="r" and play2=="rock":
     print("equaled !!")
    elif enter[0]=="p" and play2=="paper":
     print("equaled !!")
    elif enter[0]=="s" and play2=="scissor":
     print("equaled !!")

    elif enter[0]=="r" and play2=="scissor":
     print("you win !!")
    elif enter[0]=="p" and play2=="rock":
     print("you win !!")
    elif enter[0]=="s" and play2=="paper":
     print("you win !!")
    else :
     print("computer win !!") 

#Continue the game    
    want=input("Want to play again? Y/N : ")
   
    if want!="Y" and want!="y" :
     break
