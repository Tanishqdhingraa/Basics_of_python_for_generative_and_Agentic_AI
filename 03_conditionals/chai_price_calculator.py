# CONCEPT: Conditional Statements (if-elif-else)
# DESCRIPTION: Demonstrates decision-making in Python based on user input

cup = input("Choose your cup size (small/medium/large): ").lower()  # take input & normalize to lowercase

if cup == "small":                         # condition check
    print("Price is 10 rupees")
elif cup == "medium":                      # another condition
    print("Price is 15 rupees")
elif cup == "large":                       # another condition
    print("price is 20 rupees")
else:                                      # fallback if none match
    print("Unknown cup size")
