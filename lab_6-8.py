#JS Lab 6-8 11/10/2022
#collect a list of 3 numbers
a = input("Please input a number: ")
b = input("Please input another number: ")
c = input("Please input a third number: ")

#Create a list of the inputs
list = [a,b,c]

#Set string inputs to be integers
integer1 = int(a)
integer2 = int(b)
integer3 = int(c)
#Conditional to determine whether the list is, even, odd, or mixed
if integer1 % 2 == 0 and integer2 % 2 == 0 and integer3 % 2 == 0:
    print("The even numbers in the list are: " + a + ", " + b + ", and " + c)
elif integer1 % 2 != 0 and integer2 % 2 != 0 and integer3 % 2 != 0:
    print("The odd numbers in this list are: " + a + ", " + b + ", and " + c)
else:
    print("The numbers "+ a + ", " + b + ", and " + c + " are mixed")