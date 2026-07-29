# Ex 13 Student Marks Table
students = [
["Alice", 85, 90, 88],
["Bob", 75, 82, 91],
["Charlie", 95, 89, 94]
]
for student in students:
    name = student [0]
    total = student[1] + student[2] + student[3]
    average = total /3
    print(name)
    print("Total:", total)
    print("Average:", average)
    print()