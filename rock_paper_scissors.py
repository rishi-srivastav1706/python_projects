import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
games_images =["rock", "paper", "scissors"]

user_choice = int(input("enter a number between 0 to 2: \n"))
if user_choice >= 0 and user_choice <= 2:
    print(games_images[user_choice])

computer_choice =random.randint(0,2)

print(games_images[computer_choice])

if user_choice > 3 and user_choice <0:
    print("invalid input!, you lose")
elif user_choice == 2 and computer_choice ==1:
    print("you win!")
elif user_choice == 1 and computer_choice ==2:
    print("you lose!")
elif computer_choice > user_choice:
    print("you lose!")
elif user_choice > computer_choice:
    print("you win")
elif user_choice==computer_choice:
    print("it\'s a draw!")