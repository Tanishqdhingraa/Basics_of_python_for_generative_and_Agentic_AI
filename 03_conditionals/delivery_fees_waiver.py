# CONCEPT: Ternary Conditional Operator
# DESCRIPTION: Shows a one-line if-else expression used to assign values based on a condition

order_amount = int(input("Enter the order amount: "))   # take numeric input from user

delivery_fees = 0 if order_amount > 300 else 30         # conditional expression (ternary operator)

print(f"Delivery fees is : {delivery_fees}")
