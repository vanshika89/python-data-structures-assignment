# Task 2
def run_task():
    # 1. Parallel list matching 'products' list length (Cleaning the space in 'Cargo Pants')
    products = ['Apple AirPods', 'Saree', 'Men T-Shirt', 'Cap', 'Toaster', 'Cargo Pants', 'Bella Vita', 'Tennis Ball']
    categories = ['Electronics', 'Clothing', 'Clothing', 'Accessories', 'Appliances', 'Clothing', 'Fragrance', 'Sports']

    # Creating the set
    categories_set = set(categories)
    print(f"Original Categories: {categories_set}")

    # 2. Adding a new category and showing duplicates are ignored.
    categories_set.add('Footwear') # Adding something new
    categories_set.add('Clothing') # This is a duplicate (will be ignored)
    print(f"Updated set (duplicates ignored): {categories_set}")

    # 3. Show how to check whether a category exists (Boolean Result)
    exists = 'Electronics' in categories_set
    print(f"Does 'Electronics' exist? {exists}")

    # Extra: Total number of unique categories
    print(f"Total number of unique categories: {len(categories_set)}")

# The Main Line
if __name__ == "__main__":
    print("--- Running Task 2: Categories ---")
    run_task()