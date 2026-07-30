sales = [
    [1200, 1500, 1800],
    [2000, 2100, 2200],
    [1600, 1700, 1900]
]

for row in sales:
    for amount in row:
        print(amount, end="\t")
print()