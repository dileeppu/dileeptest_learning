
import random
computer_choice = random.choice(['scissors', 'rock', 'papers'])
user_choice = input("Do you want - rock, paper, or scissors \n")
if computer_choice == user_choice:
  print('TIE')
elif user_choice == 'rock' and computer_choice =='scissors':
  print('Win')
else:
    print("you loss comp win ", computer_choice)