# Task 5: Loop Control
daily_sales = [200, 150, 0, 400, 50, -1, 300]
total_sales = 0

for sales in daily_sales:
    if sales == -1: # If data is -1, stop
        print(f"Corrupted data ({sales}). Stopping process.")
        break  # Terminate the loop entirely, 300 at the end will never be reached
    elif sales == 0:
        print("No Sales, Skipping...")
        continue # Skip the rest of this iteration and move to the next number in the list
    else:
        # Add valid sales to the running total
        total_sales += sales
        print(f"Added sales = {sales}, Running total = {total_sales}")

# Final output after the loop finishes or is broken
print('Final Total Sales', total_sales)
