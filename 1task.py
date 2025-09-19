import csv as c

with open("1.csv", "r", newline ="") as f:
    file_1 = c.DictReader(f)
    rows = list(file_1)
D = {}
for j in rows:
    phone = j["battery_power"]
    price = j["price_range"]
    if price not in D:
        D[price] = []
    D[price].append(phone)
print(sorted(D.items()))