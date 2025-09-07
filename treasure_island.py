print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("you're at a cross road. where do you want to go ? type left or right")
if choice1 == "right":
    print("Fall into a hole. Game over")
else:
    print("you have come to an lake. There is an island in the middle of the lake.")
    choice2=input("type \"wait\" to wait for a boat. Type \"swim\" to swim across.")
    if choice2 == "swim":
        print("attacked by trout. Game over")
    else:
        print("you arrive at the island unharmed. There ia a house with 3 doors.")
        choice3= input("one red, one yellow and one blue. Which color do you choose?")
        if choice3 == "red":
            print("burned by fire. Game over")
        elif choice3 == "blue":
            print("eaten by beats. Game over")
        elif choice3 == "yellow":
            print("you win!")
        else:
            print("game over.")