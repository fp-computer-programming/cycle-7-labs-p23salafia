#JS Lab 6-5 11/9/2022
#Make a list of numbers
numbers = ["30","10","40"]

#Conditional to make sure there are at least 2 numbers
#Sort the list
#Print the highest and lowest number
if len(numbers)< 2:
    print("Error: List does not meet specifications")
else:
    numbers.sort(reverse=True)
    print(numbers[0] + " is the highest number")
    print(numbers[-1] + " is the lowest number")


