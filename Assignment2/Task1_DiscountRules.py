# Task 1: Discount Rules
try:
    order_amount = int(input("Enter the order amount: "))
    # Determine discount percentage
    if order_amount >= 2000:
        discount_percent = 15
    elif 1500 <= order_amount < 2000:
        discount_percent = 10
    elif 1000 <= order_amount < 1500:
        discount_percent = 7
    else:
        discount_percent = 0
    # Calculations
    discount_amt = order_amount * (discount_percent / 100)
    subtotal = order_amount - discount_amt
    taxed_amount = subtotal * 0.05 # 5% tax
    final_total = subtotal+taxed_amount
    print('_' * 30)
    print(f"Order amount = Rs {order_amount:.2f}\nDiscount({discount_percent}%)=   - {discount_amt}\nTax (5%)     =  + {subtotal}\nFinal Total  = Rs {final_total}")

except Exception as e: # handling case when input is non numeric
    print('Please enter valid Integer.....', e)
