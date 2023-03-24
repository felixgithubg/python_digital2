# Set the prices of each item
tomato_price = 3
cucumber_price = 2
cola_price = 5
chicken_price = 20

# Set the quantities of each item
tomato_qty = 2
cucumber_qty = 5
cola_qty = 6
chicken_qty = 5

# Calculate the subtotal
subtotal = (tomato_price * tomato_qty) + (cucumber_price * cucumber_qty) + \
    (cola_price * cola_qty) + (chicken_price * chicken_qty)

# Calculate the tax
tax_rate = 0.17  # 17% tax rate
tax = subtotal * tax_rate

# Calculate the total price
total = subtotal + tax

# Round the total to two decimal places
total = round(total, 2)

# Display the total price
print("Total price including tax: {} NIS".format(total))