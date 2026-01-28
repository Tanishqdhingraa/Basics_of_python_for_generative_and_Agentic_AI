chai_menu = {"masala": 30, "ginger": 40}


#This is a  example of key Error here 
#because key is not available in dictorniary 
try:
    chai_menu["elaichi"]
except KeyError:
    print("The key that you are tying to access does not exists")

#This will print safely 
print("Hello chai code")
