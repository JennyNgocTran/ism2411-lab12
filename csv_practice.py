# Reflection Questions:
# 1.
# 2.

print("--- Exercise 1: Get the file ---")
print("--- Exercise 2: Read and print raw rows ---")
print("--- Exercise 3: Skip the header ---")
print("--- Exercise 4: Compute totals ---")

processed = []
qty_rows = 0

import csv
with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader) # skip the header row
    print(header)

    for row in reader:
        print(row)
        product, price_str, qty_str = row
        price = float(price_str) # converting type before calculating
        qty = int(qty_str)
        total = price * qty
        print(f"{product}: {qty} units x ${price:.2f} = ${total:.2f}")
        processed.append({"product": product, "price": price, "qty": qty, "total": total})

        qty_rows += 1 # count of how many rows excluding header

print("--- Exercise 5: Filter and write ---")

high_value = [r for r in processed if r["total"] > 100]

with open("data/cleaned.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for r in high_value:
        writer.writerow([r["product"], r["price"], r["qty"], f"{r['total']:.2f}"])

print(f"{len(high_value)} rows of high-value orders out of {qty_rows} original rows")

# print("--- Exercise 6: csv.DictReader ---")

# print("--- Exercise 7: Sales summary by product ---")

# print("--- Exercise 8: Append mode log ---")