# Task 3 - Lambda Function: GST Calculator

# Basic Lambda: Adds 18% GST to the original price
gst = lambda price: price + (0.18 * price)

final_price_with_discount = lambda price, discount: (price - ((discount / 100) * price)) + (
        0.18 * (price - ((discount / 100) * price)))

# --- Testing the functions ---

# Test the basic GST lambda
print(f"Price after 18% GST on 100: {gst(90)}")

# Test the Extra lambda (e.g., Price = 100, Discount = 10%)
# Logic: 10% off 100 is 10. Then 18% GST on 90 is 16.2. Total = 106.2.
print(f"Final price after 10% discount and 18% GST: {final_price_with_discount(100, 10)}")
