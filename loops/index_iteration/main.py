prices = [29.99, 45.50, 12.75, 38.20]
discount = [0.1, 0.2, 0.15, 0.05]

for cost in range(len(prices)):
    prices[cost] -= prices[cost] * discount[cost]
    print(f"Updated price for item {cost + 1}: ${prices[cost]:.2f}")
    
    
