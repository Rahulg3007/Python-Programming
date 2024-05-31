#Example : Creating Tuple
# mytuple=("apple","banana","orange")
# print(mytuple) #('apple', 'banana', 'orange')

#Example 2 : Access tuple items
# mytuple=("apple","banana","orange")
# print(mytuple[1]) #banana
# print(mytuple[-1]) #orange

#Example 3 : range of indexes
# mytuple=("apple","banana","orange","cherry","mango")
# print(mytuple[2:4]) #('orange', 'cherry')
# print(mytuple[-4:-1]) #('banana', 'orange', 'cherry')

#Example 4 : Change the tuple values
#by default tuple can not allow you to change values bcause its immutable
#but there is work around
#tuple->list(modify)->tuple

# mytuple=('banana', 'orange', 'cherry')
#
# mylist=list(mytuple)
# mylist[0]="mango"
#
# mytuple=tuple(mylist)
# print(mytuple) #('mango', 'orange', 'cherry')

#Example 4 : reading tuple item using loop
# mytuple=('mango', 'orange', 'cherry')
# for i in mytuple:
#     print(i)

#Example 6 : check if the item exist(searching of item in tuple)
# mytuple=('mango', 'orange', 'cherry')

# if "banana" in mytuple:
#     print("Item is available")
# else:
#     print("Item is not available")

#Example 7 : Tuple lentgh
# mytuple=('mango', 'orange', 'cherry')
# print(len(mytuple)) #3

#Example 8 : Add items to tuple - not possible bcause tuple is immutable
# mytuple=('mango', 'orange', 'cherry')
# mytuple[0]="orange" #TypeError: 'tuple' object does not support item assignment
# print(mytuple)

#Example 9 : copy tuple
# mytuple1=('mango', 'orange', 'cherry')
# mytuple2=mytuple1
# print(mytuple2) #('mango', 'orange', 'cherry')

#Example 10: Removing item from tuple - not possible because tuple is immutable
# mytuple=('mango', 'orange', 'cherry')
# # mytuple.remove("orange") #invalid statement
# del mytuple
# print(mytuple) #name 'mytuple' is not defined. because tuple is deleted

# Example 11 : join/combine tuple
# mytuple1=("mango","orange","banana")
# mytuple2=(1, 2, 3)
#
# mytuple3=mytuple1+mytuple2
# print(mytuple3) #('mango', 'orange', 'banana', 1, 2, 3)

# Example 12 : Check tuple is equal or not
mytuple1=("mango","orange","banana")
mytuple2=(1, 2, 3)

if mytuple1==mytuple2:
    print("Tuple is equal")
else:
    print("Tuple is not equal")