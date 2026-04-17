# Task 2: Process Multiple Orders
orders = [1200, 2500, 800, 1750, 3000]
# Column headings : <10 aligns text to the left within a 10-character block
print(f"{'Order':<10} | {'Disc%':<10} | {'Final Amount':<10}")
print("_" * 35)
discounted_orders_count = total_revenue = 0

# Discount Logic
for order_amount in orders:
    if order_amount >= 2000:
        discount_percent = 15
    elif 1500 <= order_amount < 2000:
        discount_percent = 10
    elif 1000 <= order_amount < 1500:
        discount_percent = 7
    else:
        discount_percent = 0
    # Count orders that actually received a discount
    if discount_percent > 0:
        discounted_orders_count += 1

    # Calculations
    discount_amt = order_amount * (discount_percent / 100)
    subtotal = order_amount - discount_amt
    # Tax: adding 5% of the subtotal
    tax = subtotal * 0.05
    final_total = subtotal + tax

    total_revenue += final_total

    # Printing till 2 decimal points
    print(f"{order_amount:<10} | {discount_percent:<10} | {final_total:<10}")

print('Total revenue after discount: ', total_revenue)
print('Discounted order count: ', discounted_orders_count)
