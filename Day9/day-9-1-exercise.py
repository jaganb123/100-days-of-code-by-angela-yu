student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# 91 - 100: Grade = "Outstanding"
# 81 - 90: Grade = "Exceeds Expectations"
# 71 - 80: Grade = "Acceptable"
# 70 or lower: Grade = "Fail"

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for i, j in student_scores.items():
    if j > 90:
        student_grades[i] = "Outstanding"
    elif j > 80:
        student_grades[i] = "Exceeds Expectations"
    elif j > 70:
        student_grades[i] = "Acceptable"
    else:
        student_grades[i] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visit": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuggart"], "total_visit": 16}
}
