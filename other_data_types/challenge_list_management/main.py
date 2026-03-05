meat = ["Ham",3.99,50,"Sliced"]
cheese = ["Cheddar",5.49,100,"Sharp"]
condiment = ["Mustard",1.99,75,"Spicy"]
#create main list
deli_dept = [meat,cheese,condiment]
print("Initial Deli List:",deli_dept)
#restock item:
if "Ham" in meat and meat[2]<100:
    meat[2] = 100

#Add Seasond Meat:
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)
#Remove condiment
deli_dept.remove(condiment)
#Sort list
deli_dept.sort()

print("Updated Deli List: ",deli_dept)