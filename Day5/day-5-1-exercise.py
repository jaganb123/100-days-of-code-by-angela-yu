# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# print(student_heights)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
Total = 0
for n in student_heights:
    Total += n
Avg = round((Total / len(student_heights)))
print(Avg)
