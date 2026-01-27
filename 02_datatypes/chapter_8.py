#Mutable Datatype -> List = [] 

#append and remove in list  
ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")


spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]
#added in both the list bove 
chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")
#it will access at which index we need to put this 
chai_ingredients.insert(2, "black tea") # put this at index 2 
print(f"chai: {chai_ingredients}")

#remove the last element and give them in a variable we provided 
last_added = chai_ingredients.pop()
print(f"{last_added}")
print(f"chai after poped: {chai_ingredients}")

# reverse the list 
chai_ingredients.reverse()
print(f"chai after reversing: {chai_ingredients}")

#sorting the list
chai_ingredients.sort()
print(f"chai after sorting : {chai_ingredients}")

# Finding maximum and minimum in list  
sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]
# adding 2 list 
full_liquid_mix = base_liquid + extra_flavor
print(f"adding 2 list herre : {full_liquid_mix}")

# power in the list 
strong_brew = ["black tea", "water"] * 3
print(f"String brew: {strong_brew}")

#replacing in bytes 
raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")