# Task 3: User Menu
order_list = []
total = 0

while True:
    print("--- Menu ---") # Display options
    print("1 — Add order amount")
    print("2 — Show all orders and totals")
    print("q — Quit")
    try:
        choice = input('Choose an action from above menu: ')
    except Exception as e:
        print(e)
    if choice == 'q':
        break
    # Option 1: Collect new order amounts from the user
    elif choice == '1':
        order_len = int(input('Enter the total number of order amounts you need to enter:'))
        for o in range(order_len):
            amt = int(input("Enter amount to add: "))
            if amt:
                order_list.append(amt)
            else:
                print("Invalid amount. Returning to menu.")
                continue
        print("Orders updated successfully!")
    # Option 2: Calculate discounts and display the summary
    elif choice == '2':
        print('All orders', order_list)
        for order_amount in order_list:
            if order_amount >= 2000:
                discount_percent = 15
            elif 1500 <= order_amount < 2000:
                discount_percent = 10
            elif 1000 <= order_amount < 1500:
                discount_percent = 7
            else:
                discount_percent = 0
            # Calculate the final price after applying the discount
            discount_value = order_amount * (discount_percent / 100)
            final_total = order_amount - discount_value
            print(f'For order: {order_amount} Total after discount {discount_percent}% is {final_total}')
    # Handle invalid menu selections
    else:
        print("Invalid choice, please try again.")
        continue
