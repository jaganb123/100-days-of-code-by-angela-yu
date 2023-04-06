# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.
# Love Scores less than 10 or greater than 90, > "Your score is **x**, you go together like coke and mentos."
# Love Scores between 40 and 50 > "Your score is **y**, you are alright together."
# Otherwise > "Your score is **z**."

print("Welcome to the LOVE CALCULATOR...")
FirstName = input("Enter your name : ").lower()
SecondName = input("Enter their name : ").lower()

FirstScore = 0
SecondScore = 0

for i in "true":
    FirstScore += (FirstName + SecondName).count(i)
for i in "love":
    SecondScore += (FirstName + SecondName).count(i)

FinalScore = int(str(FirstScore) + str(SecondScore))

if FinalScore < 10 and FinalScore > 90:
    print(f"Your score is {FinalScore}, you go together like coke and mentos.")
elif FinalScore >= 40 and FinalScore < 50:
    print(f"Your score is {FinalScore}, you are alright together.")
else:
    print(f"Your score is {FinalScore}")
