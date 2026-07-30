sales = [
    [1200, 1500, 1800],
    [2000, 2100, 2200],
    [1600, 1700, 1900]
]

count = 0

for row in sales:
    for amount in row:
        count += 1

print("Count:", count)