#Example: how to create list

# mylist1=[10,20,30,40]
# mylist2=["apple","banana","cherry"]
# mylist3=["apple",10,"banana",20]
# mylist=list() #empty list
#
# print(mylist1)
# print(mylist2)
# print(mylist3)
# print(mylist)

#Example 2 : Accessing items from list
# mylist=["apple","banana","cherry"]
# print(mylist[0])
# print(mylist[-1])

#Example 3: Range of Indexes
# mylist=["apple","banana","cherry","orange","pineapple"]
# print(mylist[1:3]) #['banana', 'cherry']
#
# print(mylist[-3:-1]) #['cherry', 'orange']

#Example 4: change item value
# mylist=["apple","banana","cherry"]
# print(mylist) #["apple","banana","cherry"]
# mylist[0]="orange"
# print(mylist) #["orange","banana","cherry"]

#Eample 5 : Read the list item using loop
# mylist=["apple","banana","cherry"]
#
# for i in mylist:
#     print(i)

#Example 6 : Check if the item exist in the list or not
# mylist=["apple","banana","cherry"]
#
# if "apple" in mylist:
#     print("Item is present in list")
# else:
#     print("Item is not present")

#Example 7 : List lenght (counting number of itmes in a list)
# mylist=["apple","banana","cherry"]
# print(len(mylist)) #3

#Example 8 : Add new item in list  append()  insert()
# mylist=["apple","banana","cherry"]
# mylist.append("orange")  #["apple","banana","cherry"]      insert new item at the end
# mylist.insert(1,"orange") #['apple', 'orange', 'banana', 'cherry']  insert new item between list
# print(mylist) #['apple', 'banana', 'cherry', 'orange']

#example 9: remove item from the list
# pop()   Function
# mylist=["apple","banana","cherry"]
# mylist.pop(1)  #here we should specify index not the value
# print(mylist) #['apple', 'cherry']

#del   (keyword)
# mylist=["apple","banana","cherry"]
# del mylist[1]   #here del command removes single item based on the index
# print(mylist) #['apple', 'cherry']

#clear()   Function
# mylist=["apple","banana","cherry"]
# mylist.clear()   #clear all items
# print(mylist)


# Example 10: Copy list
#list()   Function
# mylist1=["apple","banana","cherry"]
# mylist2=list(mylist1)
# print(mylist1) #['apple', 'banana', 'cherry']
# print(mylist2) #['apple', 'banana', 'cherry']

#copy()  Function
# mylist1=["apple","banana","cherry"]
# mylist2=mylist1.copy()
# print(mylist1) #['apple', 'banana', 'cherry']
# print(mylist2) #['apple', 'banana', 'cherry']

#Example 11 : combine/join list
# using + operator
# mylist1=["apple","banana","cherry"]
# mylist2=[1,2,3]
# mylist3=mylist1+mylist2
# print(mylist3) #['apple', 'banana', 'cherry', 1, 2, 3]

#using looping statement
# mylist1=["apple","banana","cherry"]
# mylist2=[1,2,3]
#
# for i in mylist2:
#     mylist1.append(i)
# print(mylist1) #['apple', 'banana', 'cherry', 1, 2, 3]

#Using extend()
# mylist1=["apple","banana","cherry"]
# mylist2=[1,2,3]
# mylist1.extend(mylist2)
# print(mylist1) #['apple', 'banana', 'cherry', 1, 2, 3]

# Example 12 : Check list is equal or not
mytuple1=["mango","orange","banana"]
mytuple2=[1, 2, 3]

if mytuple1==mytuple2:
    print("list is equal")
else:
    print("list is not equal")