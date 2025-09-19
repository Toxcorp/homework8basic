import csv as c
file_4 = []
for i in range(12):
    row = ""
    for j in range(12):
        if 2 <= i <= 9 and 2 <= j <= 9:
            row += "#"
        else:
            row += "*"
    file_4.append({"row": row})
fieldnames = ["row"]
with open("4.csv", "w", newline="", encoding="utf-8") as f_4:
    writer_ASCII = c.DictWriter(f_4, fieldnames=fieldnames)
    writer_ASCII.writeheader()      
    writer_ASCII.writerows(file_4)