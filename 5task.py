import csv as c
with open("customer.csv", "r", newline="") as csv_5:
    c_reader = c.DictReader(csv_5)
    laptop_b = []
    for r in c_reader:
        if r.get("Product") == "Laptop":
            laptop_b.append(r["Customer_ID"])
print("Customers that bought laptop:",laptop_b)