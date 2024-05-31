#Example 1 : creating set
# myset={"apple","orange","mango"}
# print(myset) #{'mango', 'orange', 'apple'}

#Example 2 : Accesing item from set
# myset={"apple","orange","mango"}
#
# for i in myset:
#     print(i)

#Example 3 : Check value exist or not
# myset={"apple","orange","mango"}
#
# print("Banana" in myset) #False

#Example 4 : Adding items to set
#add()  Function   add single time
# myset={"apple","orange","mango"}
# myset.add("Banana")
# print(myset)

#update() Function  Adding multiple item
# myset.update(["Grapes","Strawberry"])
# print(myset)


#Example 5 : find number of items in a set
# myset={"apple","orange","mango"}
# print(len(myset)) #3

#Example 6 : Remove item from set
#remove ()
# myset={"apple","orange","mango"}
# myset.remove("orange")
# print(myset) #{'apple', 'mango'}
# myset.remove("xyz")  #keyError: 'xyz
# print(myset) # if the value is not present in set then it will throw keyError: 'xyz

#discard
# myset={"apple","orange","mango"}
# myset.discard("orange")
# print(myset) #{'apple', 'mango'}
# myset.discard("xyx")
# print(myset) # do not throw any error

#Example 7 : clear all items from set
# myset={"apple","orange","mango"}
# myset.clear()
# print(myset) #set()
#
# del myset
# print(myset) #NameError: name 'myset' is not defined

#Example 8: Joining 2 sets
#union()
# myset1={"apple","orange","mango"}
# myset2={1,2,3}
# myset3=myset1.union(myset2)
# print(myset3) #{'mango', 1, 'apple', 2, 3, 'orange'}

#update()
myset1={"apple","orange","mango"}
myset2={1,2,3}
myset1.update(myset2)
print(myset1) #{'mango', 1, 2, 'orange', 3, 'apple'}