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

# Write your code below this line 👇

from random import randint

Choices = [rock, paper, scissors]

print("Welcome to the Rock Paper Scissors game !!!!!!")

UserChoiceNum = int(input("Hello user Make your choice: 1 for rock, 2 for paper, 3 for scissors : "))
CompChoice = randint(1, 3)

if UserChoiceNum == 1:  # rock
    if CompChoice == 1:
        Winner = "draw"
    elif CompChoice == 2:
        Winner = "comp"
    elif CompChoice == 3:
        Winner = "user"
elif UserChoiceNum == 2:  # Paper
    if CompChoice == 1:
        Winner = "user"
    elif CompChoice == 2:
        Winner = "draw"
    elif CompChoice == 3:
        Winner = "comp"
elif UserChoiceNum == 3:  # scissors
    if CompChoice == 1:
        Winner = "comp"
    elif CompChoice == 2:
        Winner = "user"
    elif CompChoice == 3:
        Winner = "draw"
print(UserChoiceNum, CompChoice)
print(f"Player choose this...\n\n{Choices[UserChoiceNum - 1]}")
print(f"Computer choose this...\n\n{Choices[CompChoice - 1]}")
if Winner == "draw":
    print("OOPS... It's a draw...")
else:
    print(f"The winner is {Winner}...")
