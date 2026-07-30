salaries = [
    [5000, 5200, 5100],
    [4800, 4950, 5050],
    [6000, 6100, 6200]
]

highest = salaries[0][0]
lowest = salaries[0][0]

for row in salaries:
    for salary in row:
        print(f"${salary}", end="\t")

if salary > highest:
    highest = salary

if salary < lowest:
    lowest = salary
print()

print("\nHighest Salary: $", highest)
print("\nLowest Salary: $", lowest)