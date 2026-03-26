# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

combined_list = list(zip(products, prices, quantities_sold))
sorted_products = sorted(combined_list)

for product in range(len(sorted_products)):
    product_name, product_price, quanity_sold = sorted_products[product]
    print(f"Product: {product_name}, Price: {product_price}, Quantity Sold: {quanity_sold}")
#while current_stock < min_stock:
#        current_stock += restock_amount
#   inventory[item][0] = current_stock
#    if current_stock > discount_threshold and not on_sale:
 #       inventory[item][3] = True