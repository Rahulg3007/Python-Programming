# create string variable
 #Example 1:
# ways of creating string variables
# s='welcome'
# s="welcome"
# s=str('welcome')
# s=str("welcome")

# creating empty string variables
# name=""
# name=''
# name=str()

#Example 2:
# mutable-can change the value of variable
# immutable-can not change the value of variable
# string is immutable
# if the value is changed after update then it is mutable

# str1="welcome"
# print(id(str1)) # 2628529820640
#
# str1=str1+"to python"
# print(id(str1)) # 2024991963312

# Example 3: + and * wit string
# str1='welcome'
# print(str1 + 'programming')  # welcomeprogramming   concatenation
# print(str1*2) #welcomewelcome

# Example 4: Slicing
# str1='welcome'
# print(str1[1:3]) # el
# print(str1[:6]) # welcom
# print(str1[3:]) # come
#
# print(str1[1:-1]) #elcom  last 1 char removed

#Example 5: ord() and chr()
# print(ord('A')) #65  returns the ASCII code of the character
# print(chr(65)) # A return character represented by ASCII number

#Example 6: max() min() len()
# print(max('abc')) # c
# print(min('abc')) # a
# print(len('abc')) # 3

#Example 7: in , not in operation
# s="Welcome"
# print("come" in s) # True
# print("abe" in s) # False

# print("come" not in s) # False
# print("abc" not in s) # True

#Example 8: string comparison
# print("python"=="lion") # False
# print("free" != "freedom") # True
# print("python" > "java") # True
# print("right" >= "left") # True
# print("teeth" < "tee") # False
# print("yellow" <= "white") # False
# print("abc" > "") # True

#Example 9: Testing strings True/False
# s = "welcome to python"
# print(s.isalnum()) # False
# print(s.isalpha()) # False
# print("100".isdigit()) # True
# print("first number".isidentifier()) # False
# print(s.islower()) # True
# print("WELCOME".isupper()) # True
# print(" ".isspace()) # True

#Example 10 : searching for substrings
# s = "welcome to python"
# print(s.endswith("on")) # True
# print(s.startswith("hi")) # False
# print(s.find("come")) # 3
# print(s.find("become")) #-1 not found
# print(s.count("o")) # 3  Returns number of occurences of substring the string

#Example 11: Converting string
# s = "Welcome to python"
# print(s.capitalize()) # Welcome to python
# print(s.title()) # Welcome To Python
# print(s.lower()) # welcome to python
# print(s.upper()) # WELCOME TO PYTHON
# print(s.swapcase()) #wELCOME TO PYTHON
# print(s.replace("python", "Java")) # Welcome to Java


# Example 12 : Reverse Strting
#Method 1
# s="python"
# rev_str=""
# for i in s:
#     rev_str=i+rev_str
# print("Reversed string is: "+rev_str) #nohtyp

#Method 2  slicing
s="python"
rev_str=s[::-1]
print(rev_str) # nohtyp