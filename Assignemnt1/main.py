import Task1_ProductCollections
import Task2_Categories
import Task3_ProductPricing
import Task4_CombinedOperations

if __name__ == "__main__":
    print("--- Starting Full Inventory Suite ---")

    # 1. Run Task 1 (Lists & Tuples)
    Task1_ProductCollections.run_task()
    print("-" * 30)

    # 2. Run Task 2 (Sets)
    Task2_Categories.run_task()
    print("-" * 30)

    # 3. Run Task 3 and CAPTURE the dictionary it returns
    updated_prices = Task3_ProductPricing.run_task()
    print("-" * 30)

    # 4. Run Task 4 using the actual lists and the captured price_dict
    # We define the lists here so they can be passed to Task 4
    products = ['Apple AirPods', 'Saree', 'Men T-Shirt', 'Cap', 'Toaster', 'Cargo Pants', 'Bella Vita', 'Tennis Ball']
    categories = ['Electronics', 'Clothing', 'Clothing', 'Accessories', 'Appliances', 'Clothing', 'Fragrance', 'Sports']

    Task4_CombinedOperations.run_task(products, updated_prices, categories)

    print("\n" + "=" * 40)
    print("  ALL TASKS COMPLETED SUCCESSFULLY  ")
    print("=" * 40)