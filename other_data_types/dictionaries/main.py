grocery_inventory = {
    "milk": (113,"Dairy"),"Eggs":(116,"Dairy"),
    "Bread":(117,"Bakery"),"Apples":(141,"Produce")}

bread_details = grocery_inventory.get("Bread")
print("Details of Bread:", bread_details)

grocery_inventory.update({"Cookies":(143,"Bakery")})
print("inventory after adding Cookies:", grocery_inventory)
grocery_inventory.pop("Eggs")
print("inventory after removing Eggs:", grocery_inventory)