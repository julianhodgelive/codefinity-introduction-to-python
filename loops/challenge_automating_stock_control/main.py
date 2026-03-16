# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

#currentstock = inventory.get("Bread")[:3]
#print(currentstock)

print("Processing Started:")

for item in inventory:
    while inventory.get(item)[0] <= inventory.get(item)[1] :
        currentstock = inventory.get(item)[0]
        minimumstock = inventory.get(item)[1]
        restockvalue = inventory.get(item)[2]
        salesstatus = inventory.get(item)[3]
        currentstock += restockvalue
        inventory.update({item:currentstock})
        
    
        
        
    print(f"Processing {item}")
    print(inventory)


#    currentstock = item
#    print(currentstock)
    
#      current_stock = item[]
    