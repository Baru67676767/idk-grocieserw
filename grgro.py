# ================================ #
# GROCERY BILLING QUEUE
# ================================ #

print("=== Grocery Billing Queue ===\n")

# ---------- PART 1: the five counters & loop control ----------
low_price_items = 0
medium_price_items = 0
high_price_items = 0
customers_served = 0
total_sales = 0
billing = True

# ---------- PART 2 & 3: the OUTER while loop & validation ----------
while billing:
    customer_name = input("Enter customer name: ")
    item_count = int(input("How many items are they buying? "))

    if item_count <= 0:
        print("Invalid item count. Please try again.")
        continue

    # ---------- PART 4: the INNER while loop ----------
    customer_total = 0
    item_number = 1

    while item_number <= item_count:
        item_name = input("Enter item name: ")
        price = int(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))

        # ---------- PART 5: item total and price band ----------
        if price <= 0 or quantity <= 0:
            print("Invalid price or quantity. Skipping item.")
            continue

        item_total = price * quantity
        print(f"{item_name}: {quantity} x {price} = {item_total}")
        
        customer_total += item_total

        # Categorize by total price of the item(s) bought
        if item_total < 50:
            low_price_items += quantity
        elif item_total <= 100:
            medium_price_items += quantity
        else:
            high_price_items += quantity

        item_number += 1

    # ---------- PART 6: finish the customer, ask about the next ----------
    customers_served += 1
    total_sales += customer_total
    print(f"Total for {customer_name}: ${customer_total}\n")

    next_customer = input("Next customer? (yes/no): ").strip().lower()
    if next_customer != "yes":
        billing = False

# ---------- PART 7: the NESTED for report ----------
print("\n=== Daily Summary Report ===")
bands = [
    ("Low Price Items (< 50)", low_price_items),
    ("Medium Price Items (50-100)", medium_price_items),
    ("High Price Items (> 100)", high_price_items)
]

for band_name, count in bands:
    print(f"{band_name}: ", end="")
    for _ in range(count):
        print("*", end="")
    print()

print(f"\nTotal Customers Served: {customers_served}")
print(f"Total Sales: ${total_sales}")