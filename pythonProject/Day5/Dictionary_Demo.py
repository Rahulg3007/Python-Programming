#Example 1 : Creating dictionary
# mydic={101:"a", 102:"b", 103:"c"}
# print(mydic) #{101: 'a', 102: 'b', 103: 'c'}

#Example 2 : Access items from dictionary
# mydic={
#     "brand":"Tata",
#     "model":"Safari",
#     "year":2023
# }
# print(mydic["brand"]) #Tata
#
# #Using get()
# x=mydic.get("model")
# print(x) #Safari
# print(mydic.get("model")) #Safari

#Example 3 : Change values in dictionary
# mydic={
#     "brand":"Tata",
#     "model":"Safari",
#     "year":2023
# }
# # print(mydic) #{'brand': 'Tata', 'model': 'Safari', 'Year': '2023'}
# mydic["year"]=2024 #new value
# print(mydic) #{'brand': 'Tata', 'model': 'Safari', 'year': 2024}


#Example 4 : Reading items from dictionary using loop
# mydic={
#     "brand":"Tata",
#     "model":"Safari",
#     "year":2023
# }

# for i in mydic:
#     print(i)  #Prints only keys from dictionary
#
# for i in mydic:
#     print(mydic[i]) #prints only values from dictionary

# for i in mydic.values():
#     print(i) #prints only values from dictionary

# for x,y in mydic.items():
#     print(x,y)  # print keys along with the value

# Example 5 : check key is exist in dictionary or not
# mydic={
#     "brand":"Tata",
#     "model":"Safari",
#     "year":2023
# }
# if "brand" in mydic:
#     print("Exist")
# else:
#     print("Not Exist")

# print("brand" in mydic) # True


#Example 6: find number of items in dictionary
# mydic={
#     "brand":"Tata",
#     "model":"Safari",
#     "year":2023
# }
# print(len(mydic)) #3


#Example 7 : Adding item to dictionary
# mydic={
#     "brand":"Tata",
#     "model":"Safari",
#     "year":2023
# }
# mydic["color"]="red"
# print(mydic) # {'brand': 'Tata', 'model': 'Safari', 'year': 2023, 'color': 'red'}

#Example 8 : Remove item from dictionary
# mydic={
#     "brand":"Tata",
#     "model":"Safari",
#     "year":2023
# }
# mydic.pop("year")
# print(mydic) # {'brand': 'Tata', 'model': 'Safari'}

# del mydic["year"]
# print(mydic) # {'brand': 'Tata', 'model': 'Safari'}

# del mydic
# print(mydic) #NameError: name 'mydic' is not defined

# mydic.clear()
# print(mydic) # {}

#Example 9 : copying dictionary
mydic1={
    "brand":"Tata",
    "model":"Safari",
    "year":2023
}
#Without using copy function
# mydic2=mydic1
# print(mydic2) #{'brand': 'Tata', 'model': 'Safari', 'year': 2023}

# with using copy function
mydic2=mydic1.copy()
print(mydic2)