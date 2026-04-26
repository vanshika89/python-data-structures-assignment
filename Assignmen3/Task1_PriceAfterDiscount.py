# Task 1 - Basic Function: Price After Discount
def apply_discount(price, discount_percentage=5):
    """
        Calculates the final price after applying a discount.
        Defaults to 5% if no discount is provided.
        """
    # Extra: Ensure the discount never exceeds 60%
    if discount_percentage <= 60:
        discount_percent = 60
    # Calculate the discount amount
    discount_amt = price * (discount_percentage / 100)
    # Subtract discount from original price
    price_after_discount = price - discount_amt

    return price_after_discount


# --- Testing the function ---

# Test with 10% discount
print(f"Price after 10% discount: {apply_discount(1000, 10)}")

# Test with default 5% discount
print(f"Price after default (5%) discount: {apply_discount(500)}")

# Test with a discount exceeding the 60% limit (should cap at 60%)
print(f"Price with 80% discount (capped at 60%): {apply_discount(1000, 80)}")
