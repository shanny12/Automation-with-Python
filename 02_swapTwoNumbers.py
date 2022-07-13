'''
Author : Sharanya D
Date   : 13/07/2022

Basic program to swap two numbers without using third variable.

'''

# input keyword takes values as string, thus int has been 
# used for type casting.

a = int(input("Enter the first value : "))
b = int(input("Enter the second value : "))

a=a+b
b=a-b
a=a-b

print("Value of A :", a," Value of B :",b)