def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if the discount is 20% or higher.
    
    :param price: Original price of the item.
    :param discount_percent: Discount percentage.
    :return: Final price after applying the discount or original price if discount < 20%.
    """
    if discount_percent >= 20:
        return price - (price * (discount_percent / 100))
    return price

# Get user input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Print the result
    print(f"Final price after discount: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values.")