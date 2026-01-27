is_boiling = True
stri_count = 5
#true act as 1 

total_actions = stri_count + is_boiling # upcasting
print(f"Total actions: {total_actions}")

#false act as 0 
milk_present = 0 # no milk
print(f"Is there milk? {bool(milk_present)}")


# Logical Operator
water_hot = True
tea_added = False

can_server = water_hot and tea_added
print(f"Can serve chai? {can_server}")

can_we_server = water_hot or tea_added
print(f"Can serve chai? {can_we_server}")