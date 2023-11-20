total_amount = 0
with open("./Data/portfolio.csv", "r") as file:
    lines = file.readlines()
    for line in lines[1:]:
        row = line.strip().split(",")
        total_amount += int(row[1]) * float(row[2])

print(f"Total cost {total_amount}")
