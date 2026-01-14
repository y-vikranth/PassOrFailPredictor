import pandas as pd
import numpy as np

#Number of Students
n = 60

#Generating Attendance and Internal Marks for students
attendance  = np.random.randint(50, 100, n)
internal_marks = np.random.randint(10, 60, n)

#Labelling Pass or Fail
result = []

for i in range(n):
    if (attendance[i] >= 75) and (internal_marks[i] >= 21):
        result.append(1)
    else:
        result.append(0)

#Creating the DataFrame using Pandas

df = pd.DataFrame({
    "attendance": attendance,
    "internal_marks": internal_marks,
    "result": result
})

#Saving the DataFrame as CSV into student_pass_fail.csv
df.to_csv('data/student_pass_fail.csv', index = False)

print(df.head())
print("\nClass distribution:")
print(df['result'].value_counts())