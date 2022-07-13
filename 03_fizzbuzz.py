'''
Author : Sharanya D
Date   : 13/07/2022

FizzBuzz problem :
For a range given print the numbers, if the number 
is divisible by 3 print fizz, if divisible by 5 then 
buzz and if it is divisible by both 3 and 5 print fizzbuzz.

'''

x = int(input("Enter the range : "))
for i in range(1,x+1):
    if(i%15==0):
        print("fizzbuzz")
    elif(i%3==0):
        print("fizz")
    elif(i%5==0):
        print("buzz")
    else:
        print(i)