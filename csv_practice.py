# Reflection Questions:
# 1. Python is quicker and more easily repeatable, especially for large datasets while Excel allows for more of a visual perspective while working.
# 2. If the pipeline were to randomly break some day, an append-mode log file allows us to pinpoint the exact date and time the problem  
# occurred since using append allows us to preserve the operational history safely without disturbing its past entries.

print("--- Exercise 1: Get the file ---")
print("--- Exercise 2: Read and print raw rows ---")
print("--- Exercise 3: Skip the header ---")
print("--- Exercise 4: Compute totals ---")
# Exercises 1-4 are all mixed into each other

processed = []
qty_rows = 0

import csv
with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader) # skip the header row
    print(header)

    for row in reader:
        print(row) # read each row as lists separately
        product, price_str, qty_str = row
        price = float(price_str) # converting type before calculating
        qty = int(qty_str)
        total = price * qty
        print(f"{product}: {qty} units x ${price:.2f} = ${total:.2f}")
        processed.append({"product": product, "price": price, "qty": qty, "total": total})

        qty_rows += 1 # count of how many rows excluding header

total_revenue = sum(total['total'] for total in processed)
print(f"Total Revenue: ${total_revenue:,.2f}")

print("--- Exercise 5: Filter and write ---")

high_value = [r for r in processed if r["total"] > 100] # filter to totals greater than $100

with open("data/cleaned.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for r in high_value:
        writer.writerow([r["product"], r["price"], r["qty"], f"{r['total']:.2f}"])

print(f"{len(high_value)} rows of high-value orders out of {qty_rows} original rows")

print("--- Exercise 6: csv.DictReader ---")

totals = []

with open("data/sales.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        product = row["product"]
        price = float(row["price"])
        qty = int(row["quantity"])
        total = price * qty
        totals.append(total)
        print(f"{product}: {qty} units x ${price:.2f} = ${total:.2f}") # same totals as Exercise 4

# reader would be preferred if I just wanted the values when printing by row
# DictReader would be preferred if I wanted both the key and value when printing by row

print("--- Exercise 7: Sales summary by product ---")

sales_by_product = {}
for sale in processed:
    product = sale["product"]
    sales_by_product[product] = sales_by_product.get(product, 0) + sale["total"]

for key, value in sales_by_product.items():
    print(f"{key}: ${value:.2f}")

print("--- Exercise 8: Append mode log ---")

from datetime import datetime
timestamp = datetime.now()

with open("data/run_log.txt", "a") as f:
    f.write(f"Current date/time: {timestamp} | Total Revenue: ${total_revenue:,.2f}\n")