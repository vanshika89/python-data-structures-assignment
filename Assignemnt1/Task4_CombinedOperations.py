# Task 4: Combined Operations (Using lists from Task 1 & 2)

def run_task(products, price_dict, categories):
    # 1. Create the catalog list of tuples
    catalog = []
    for i in range(len(products)):
        name = products[i]
        # Look up price from Task 3's dictionary
        print(price_dict.get(name))
        category = categories[i]
        price = price_dict.get(name, 0)
        catalog.append((name, price, category))

    print(f"\nCatalog: {catalog}")

    # 2. Map categories to product names (Mapping Logic)
    category_to_products = {}
    for name, price, category in catalog:
        # Check if category exists; if not, initialize an empty list
        if category not in category_to_products:
            category_to_products[category] = []
        # Append the product name to the category's list
        category_to_products[category].append(name)

    print(f"Products by Category: {category_to_products}")

    # 3. Find category with most products
    # Lambda Logic: Iterates through keys (k) and compares based on the length (len) of their associated lists
    max_cat = max(category_to_products, key=lambda k: len(category_to_products[k]))

    print(f"\nCategory with most products: {max_cat}")
    print(f"Products in {max_cat}: {category_to_products[max_cat]}")


if __name__ == "__main__":
    print("--- Running Task 4: Combined Operations ---")

    test_prices = {'Apple AirPods': 10000, 'Saree': 3000, 'Men T-Shirt': 400, 'Cap': 200, 'Toaster': 5000,
                   'Cargo Pants': 450, 'Bella Vita': 3000}
    test_categories = ['Electronics', 'Clothing', 'Clothing', 'Accessories', 'Appliances', 'Clothing', 'Fragrance',
                       'Sports']
    test_products = ['Apple AirPods', 'Saree', 'Men T-Shirt', 'Cap', 'Toaster', 'Cargo Pants']

    run_task(test_products, test_prices, test_categories)
