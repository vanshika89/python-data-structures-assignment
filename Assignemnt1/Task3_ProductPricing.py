# Task 3: Product Pricing (Dictionaries)

def run_task():
    # 1. Dictionary with 6 entries
    price_dict = {'Apple AirPods': 10000, 'Saree': 3000, 'Men T-Shirt': 400, 'Cap': 200, 'Toaster': 5000,
                  'Cargo Pants': 450, 'Bella Vita': 3000}
    print(price_dict)

    # adding new product
    price_dict['Men Trousers'] = 300

    # 2. Dictionary operations
    if 'Men T-Shirt' in price_dict:      # Remove safely
        del price_dict['Men T-Shirt']
    print(price_dict)

    # 3. Average price (using float division for accuracy)
    avg_price = sum(price_dict.values()) / len(price_dict)
    print(f"Average Price: {avg_price:.2f}")

    # Extra: Print the product NAME with max and min prices
    max_prod = max(price_dict, key=price_dict.get)
    min_prod = min(price_dict, key=price_dict.get)

    print(f"Max: {max_prod} at {price_dict[max_prod]}")
    print(f"Min: {min_prod} at {price_dict[min_prod]}")

    return price_dict

if __name__ == "__main__":
    print("--- Running Task 3: Product Pricing ---")
    run_task()