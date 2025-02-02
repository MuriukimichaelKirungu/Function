def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompting user for input
original_price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage: "))

# Calculating final price
final_price = calculate_discount(original_price, discount_percent)

# Displaying the result
if final_price != original_price:
    print("Final price after applying discount: $", final_price)
else:
    print("No discount applied. Original price: $", original_price)
