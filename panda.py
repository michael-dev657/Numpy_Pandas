import pandas as pd
students_data = [{'Name': 'Alice', 'Age': 20, 'Grade': 'A', 'Mark': 85},
                 {'Name': 'Bob', 'Age': 22, 'Grade': 'B', 'Mark': 78},
                 {'Name': 'Charlie', 'Age': 19, 'Grade': 'A', 'Mark': 92},
                 {'Name': 'David', 'Age': 21, 'Grade': 'C', 'Mark': 65},
                 {'Name': 'Eve', 'Age': 20, 'Grade': 'B', 'Mark': 74}]
df = pd.DataFrame(students_data)
print(df)

print(df.head(3))

print(df[['Name', 'Mark']])

print(df[df['Grade'] == 'A'])