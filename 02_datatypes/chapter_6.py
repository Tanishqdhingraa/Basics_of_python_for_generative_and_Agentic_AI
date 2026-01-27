chai_type = "Ginger chai"
customer_name = "Priya"
#String are immutable
print(f"Order for {customer_name} : {chai_type} please !")

chai_description = "Aromatic and Bold"

#Lat alphabet is not inclusive 
print(f"First word: {chai_description[:8]}")#from 0 to 7
print(f"Last word: {chai_description[12:]}") # 12 to last index of string 
print(f"Last word: {chai_description[::-1]}")#reversing whole string 


#used a lot
label_text = "Chai Special"
#label text is a inbuild function 
#Encoding here 
ecoded_label = label_text.encode("utf-8")
print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {ecoded_label}")
#decode here 
decoded_label = ecoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")