import csv as c
from math import sqrt
with open("2.csv", "r", newline ="") as f:
    file_1 = c.DictReader(f)
    rows = list(file_1)
    print(rows)
    new_file = []
    for i in rows:
        x = int(i.get("px_height", 0))
        y = int(i.get("px_width", 0))
        z = [sqrt(x*x + y*y)]
        i["diagonal:"] = z
        i.pop("px_height")
        i.pop("px_width")
        new_file.append(i)
        print(new_file)
fieldnames = (list(new_file[0].keys()))
with open("2.1.csv", "w", newline="") as f1:
    file_2 = c.DictWriter(f1, fieldnames=fieldnames)
    file_2.writeheader()
    file_2.writerows(new_file)