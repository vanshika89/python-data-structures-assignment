# task 1
def run_task():
    # 1. list containing product names
    products = ['Apple AirPods', 'Saree', 'Men T-Shirt', 'Cap', 'Toaster', 'Cargo Pants']

    # 2. tuple stores (product_name, price, category) for one product.
    sample_product = ('Apple AirPods4', 20000, 'Electronics')

    # 3. Print the 2nd and last product
    print(f'second product: {products[1]}')
    print(f'last product: {products[-1]}')

    # 4. Append two new product names
    products.append('Bella Vita')
    products.append('Tennis Ball')
    print(f"Updated Products: {products}")

    # Extra: Modify tuple via list conversion
    list_sample_product = list(sample_product)
    list_sample_product[1] = 12000
    sample_product = tuple(list_sample_product)
    print(f"Updated Sample Product: {sample_product}")


if __name__ == "__main__":
    print("--- Running Task 1: Product Collections ---")
    run_task()
