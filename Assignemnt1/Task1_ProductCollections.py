# 1. list containing product names
products = ['Apple AirPods', 'Saree', 'Men T-Shirt', 'Cap', 'Toaster', ' Cargo Pants']

# 2. tuple stores (product_name, price, category) for one product.
sample_product = ('Apple AirPods4', 20000, 'Electronics')

# 3. Print the 2nd and last product
second_product = products[1]
last_product = products[-1]
print(f'second product: {second_product}')
print(f'last product: {last_product}')

# 4. Append two new product names to products and then print the updated list.
products.append('Bella Vita')
products.append('Tennis Ball')
print(products)

# Extra (optional): Convert sample product into a list, change its price, and convert it back to a tuple.
list_sample_product = list(sample_product)
list_sample_product[1] = 12000
sample_product = tuple(list_sample_product)
print(sample_product)