# # Variables
# # x = 5


# #! data types
# # strings
# # booleans
# # floats
# # integers
# # lists, tuples, dicts, sets

# # print(type(x))

# # print("The value of x is" + str(x))

# a = 5
# b = 10

# print("The value of a is {}".format(a))
# print("The value of b is {}".format(b))

# print(f"The value of a is {a} and value of b is {b}")

#? operators
# + = adds
# - = subtract
# % = modulus (remainder)
# / = divides
# * = multiply
# // = floor division (returns integer)



#? increment and decrement
# increment = adding value into a variable
# decrement = subtract value into a variable

#? overloaded operators
# + (not only for integers)
# x = "hi"
# y = "there"
# print(x+y)



# x = "i"
# print(x * 5)

#? augmented assignment operators
# x = 1
# x += 2 # x = x + 2

# print(x)

'''
Write instructions/statements that swaps the values of x and y
'''
# x = 5
# y = 10

# temp = x
# x = y 
# y = temp

# print(f"x is {x} and y is {y}")

# x,y = y,x

# print(f"x is {x} and y is {y}")

#? conditional operators

# ==
# >
# >=
# <
# <=







#? user input
# x = eval(input("Enter a value for x: "))
# print(type(x))


#? if, else and elif
# x = 5
# if x == 5:
#     print("x is 5")
# elif x == 10:
#     print("x is 10")
# else:
#     print("X is not 10 or 5")


#? Nested if
# if x > 3:
#     if x > 4:
#         print("x is more than 3 and 4")
#     else:
#         print("X is more than 3 but not 4")
# else:
#     print("X is not more than 3")

#? and & or
# x = 5
# y = 10

# if x > 3 or y > 10:
#     print("Yes")
# else:
#     print("No")














'''
Write a program that reads the three edges of a triangle 
and computes the perimeter if the input is valid. 
The input is valid if the sum of every pair of two edges
is greater than the remaining edge. Otherwise (i.e. else) 
print a message stating that the input is invalid and 
the perimeter cannot be calculated.
(Note: This question does NOT require further input
validation.)
'''

# x = int(input("Enter value for AB: "))
# y = int(input("Enter value for BC: "))
# z = int(input("Enter value for AC: "))

# perimeter = x+y+z

# if x+y>z and x+z>y and y+z>x:
#     print(f"Valid and the perimeter is {perimeter}")
# else:
#     print("Invalid")


# if x + y >= z:
#     print("The perimeter is", x + y + z)
# elif x + z >= y:
#     print("The perimeter is", x+y+z)
# elif y + z >= x:
#     print("The perimeter is", x + y + z)
# else:
#     print("invalid")