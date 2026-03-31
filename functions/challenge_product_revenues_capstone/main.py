def calculate_revenue(prices, quantities_sold):
    revenue = []
    for x in range(len(prices)):
        revenue.append(prices[x] * quantities_sold[x])
    return revenue

def formatted_output(revenues):
    for x in sorted(revenues):
        print(f"{x[0]} has total revenue of ${x[1]}")
  
    

# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

revenue = calculate_revenue(prices, quantities_sold)

revenue_per_product = list(zip(products,revenue))

formatted_output(revenue_per_product)

# Example of expected output line (do not remove):
#print(f"{revenue[0]} has total revenue of ${revenue[1]}")

#revenue = []
#for x in range(4):
#    revenue.append(prices[x] * quantities_sold[x])
    

#revenue_per_product = sorted(list(zip(products,revenue)))
#print(revenue_per_product)

#for product, total_rev in revenue_per_product.item():
 #   print(f"{product} has total revenue ${total_rev}")


#combined_list = list(zip(products, prices, quantities_sold))
#sorted_products = sorted(combined_list)
   # for product, stock in product_stock.items():