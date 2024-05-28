# Conditional Statements
# if  if..else  elif

# Example 1 : print a person is eligible for vote or not
#age>18

# age=25

# if age>=18:
#     print('Eligible for vote')
# else:
#     print('Not eligible for vote')

#  Example 2
# if False:
#     print('true condition')
# else:
#     print('false condition')

# Example 3
# if 0:
#     print('One')
# else:
#     print('Zero')

# Example 4
# Find Number is even or odd  num%2=0
# num=11
#
# if num%2==0:
#     print('Given num is even')
# else:
#    print('Given num is odd')

# Example 5 if else in single line (ternory operator)
# num=11
# print('Even number') if num%2==0 else print('Odd number')

# Example 6 if-else Multiple statement in single line
# a=1
# {print('Hello'),print('python')} if a>=10 else {print('hi'),print('java')}

# Example 7 Multiple condition using elif
weekno=5

if weekno==1:
    print('Sunday')
elif weekno==2:
    print('Monday')
elif weekno==3:
    print('Tuesday')
elif weekno ==4:
    print('Wednesday')
elif weekno==5:
    print('Thursday')
elif weekno==6:
    print('Friday')
elif weekno==7:
    print('Saturday')
else:
    print('Invalid weekno')