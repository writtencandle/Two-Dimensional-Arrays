sales = [
    [1200, 1500, 1800],
    [2000, 2100, 2200],
    [1600, 1700, 1900]
]
print("Monthly Sales Report")

for row in sales:
    for amount in row:
        print(f"${amount}", end="\t")
print()