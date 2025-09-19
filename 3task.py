import csv as c

from dask.dataframe.methods import values

customer_purchases = [
{"Customer_ID": 1001, "Product": "Laptop", "Category": "Electronics", "Purchase_Date": "2024-02-01"},
{"Customer_ID": 1002, "Product": "Smartphone", "Category": "Electronics", "Purchase_Date": "2024-02-02"},
{"Customer_ID": 1003, "Product": "Sofa", "Category": "Furniture", "Purchase_Date": "2024-02-03"},
{"Customer_ID": 1001, "Product": "Tablet", "Category": "Electronics", "Purchase_Date": "2024-02-10"},
{"Customer_ID": 1002, "Product": "Chair", "Category": "Furniture", "Purchase_Date": "2024-02-15"},
{"Customer_ID": 1003, "Product": "Laptop", "Category": "Electronics", "Purchase_Date": "2024-02-18"},
{"Customer_ID": 1004, "Product": "Desk", "Category": "Furniture", "Purchase_Date": "2024-02-20"},
]
fieldnames = list(customer_purchases[0].keys())
with open("customer.csv", "w", newline="") as f3:
    w_file = c.DictWriter(f3, fieldnames = fieldnames)
    w_file.writeheader()
    w_file.writerows(customer_purchases)
