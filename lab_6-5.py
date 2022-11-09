#JS Lab 6-5 11/9/2022
#Make a list of numbers
numbers = [30,10,20]
#statements to sort #s
numbers.sort(reverse=True)
#Conditional to make sure there are at least 2 numbers
if len(numbers) < numbers[2]:
    print("Error: List does not meet specifications")
#Contitional to make sure there are at least 2 unique numbers
if numbers[0]==numbers[1]:
    print("Error: List does not meet specifications")

print()
