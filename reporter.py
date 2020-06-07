
import os
import pandas as pd

def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71

CSV_FILENAME = "sales-201711.csv"

csv_filepath = os.path.join("data",CSV_FILENAME)

sales = pd.read_csv(csv_filepath)

total_sales = sales["sales price"].sum()

month = "November"
year = "2017"

product_totals = sales.groupby(["product"]).sum()

product_totals = product_totals.sort_values("sales price", ascending=False)

top_sellers = []
rank = 1
for i, row in product_totals.iterrows():
    d = {"rank": rank, "name": row.name, "total_sales": row["sales price"]}
    top_sellers.append(d)
    rank = rank + 1


print("-------------------")
print("Sales Report!")
print("-----------------")
print(f"MONTH: {month} {year}")
print(f"TOTAL SALES: {to_usd(total_sales)}")

print("-----------------")
print("Top Selling Products:")
for d in top_sellers:
    print(" " + str(d["rank"]) +" " + d["name"] + ": " + to_usd(d["total_sales"]))