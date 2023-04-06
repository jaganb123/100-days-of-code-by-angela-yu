import pandas

student = {
    "Student" : ["Jagan", "Preethi", "Sri Madhi"],
    "Score" : [85, 76, 95]
}

student_dataframe = pandas.DataFrame(student)
print(student_dataframe)

# for key,value in student_dataframe.items():
#     print(value)
for (index, row) in student_dataframe.iterrows():
    if row.Student == "Jagan":
        print(row.Score)