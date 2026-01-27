#set is like in maths  => {}

essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

#all spices
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

#Common spices 
common_spices = essential_spices & optional_spices
print(f"common spices: {common_spices}")

# deleting the optional from essential  
only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices: {only_in_essential}")

#Memebership testing in Set 
print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")

