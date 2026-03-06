seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100

# Step 1: Combine conditions to determine overstock risk and discount eligibility
overstock_risk = seasonal and current_stock > high_stock_threshold

# Step 2: Ensure that the item is eligible for a discount by checking that it is not selling well and not already on sale
discount_eligible = not selling_well and not on_sale

# Step 3: If either boolean variable is `True`, the item should be discounted 
make_discount = overstock_risk or discount_eligible

# Step 4: Print the results using the appropriate variable
print("Should the item be discounted?", make_discount)
