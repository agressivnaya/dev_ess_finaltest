import pandas as pd
import matplotlib.pyplot as plt

data = {
    'student_name': ['Andrey Ivanov', 'Stepan Petrov', 'Bill Gates', 'John Golt', 'Michael Jackson'],
    'attendance (%)': [100, 89, 34, 52, 77],
    'mark (points)': [95, 80, 100, 70, 40]
}

df = pd.DataFrame(data)
print(df)

plt.figure(figsize=(5, 3))
plt.scatter(df['attendance (%)'], df['mark (points)'], color='red', marker='o')
plt.title('Correlation between Attendance and Marks')
plt.xlabel('Attendance (%)')
plt.ylabel('Mark (points)')
plt.grid(True)

plt.show()