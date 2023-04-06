# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# There are 365 days in a year, 52 weeks in a year and 12 months in a year.
# You have 12410 days, 1768 weeks, and 408 months left.

EndOfLife = 90

RemainingLifeTime = EndOfLife - int(age)

RemainingDays = RemainingLifeTime * 365
RemainingWeeks = RemainingLifeTime * 52
RemainingMonths = RemainingLifeTime * 12

print(f"You have {RemainingDays} days, {RemainingWeeks} weeks, and {RemainingMonths} months left.")
