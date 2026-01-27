#Starting Tuples here  () -> immutable 

#it cannot be changed 
masala_spices = ("cardamom", "cloves", "cinnamon")
#Giving name to all index 
(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")



ginger_ratio, cadramom_ratio = 2, 1
print(f"Ratio is G :{ginger_ratio} and C: {cadramom_ratio}")
#Switching the value here 
ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio
print(f"Ratio is G :{ginger_ratio} and C: {cadramom_ratio}")

# membership testing -> {'cinnamon' in masala_spices}
print(f"Is cinnamon in masala spices ? {'cinnamon' in masala_spices}")