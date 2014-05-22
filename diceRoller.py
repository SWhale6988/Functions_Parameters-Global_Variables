#Coin flip program
#The Purpose of this program is to generate a random number from 1 to 6 and display it
#As a dice face. I have then chnaged the program to continue until
#it has rolled a 6
#<(^_^<) <(^_^)> (>^_^)>

import random,time
result = ""
result2 = " "  
dice = ["- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n",
"- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n",
"- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n",  #This part stores the different dice graphics into 6 different variables in a list.
"- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n",
"- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n",
"- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"]

def roll():
    print("rolling.....")
    global result  #This part tells the user the dice is rolling and stores the result in a global variable
    result = random.randint(1,6)




def show_dice():
    print(dice[result-1])  #This prints the dice depending on the roll


while result != 6:
    userinput = input("Press enter to continue")  # This forces the user to press enter to continue the program
    roll() #Runs teh roll function
    time.sleep(1) #Pauses the program
    show_dice() #runs the roll dice function
    

"""
inport instead of import
; instead of ,
Print instead of print
randing instead of randint
else instead of elif
multiple lack of colons (>^_^)>
"""


