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

#Write your code below this line 👇
import random
shapes = [rock, paper, scissors]
computer_choice = random.randint(0, 2)

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors."))
print(shapes[choice])



print("Computer choice")
print(shapes[computer_choice])


if choice == computer_choice:
  print("It's a tie! You both chose the same shape!")
elif (choice == 0 and computer_choice == 1) or (choice == 1 and computer_choice == 2) or (choice == 2 and computer_choice == 0):
  print("Computer won!")
else:
  print("You won!")

