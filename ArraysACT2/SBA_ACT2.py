nums = [
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45],
]
for row in nums:
    for value in row:
        print(value)

print("\t \33[33mSales List 2\33[0m")
sales = [
    [1200, 1500, 1800, 2000],
    [1400, 1600, 1900, 2200],
    [1300, 1700, 2100, 2300],
]
total = 0
for row in sales:
    for value in row:
        total += value
print("Total Sales:", total)