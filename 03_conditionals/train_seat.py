# CONCEPT: Match-Case (Structural Pattern Matching - Python 3.10+)
# DESCRIPTION: Cleaner alternative to multiple if-elif statements for comparing values

seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower()  # user input normalized

match seat_type:
    case "sleeper":   # pattern match
        print("Sleeper - No AC, beds available")
    case "ac":
        print("AC - Air conditioned, comfy ride")
    case "general":
        print("General - Cheapest option, no reservation")
    case "luxury":
        print("Luxury - Premium seats with meals")
    case _:           # default case (like else)
        print("Invalid seat type")
