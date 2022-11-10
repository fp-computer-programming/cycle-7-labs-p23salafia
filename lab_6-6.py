#JS Lab 6-6 11/9/2022
#Collect word inputs
w1 = input("Please input a word: ")
w2 = input("Please input different word that does not match any other word input: ")
w3 = input("Please input third word that does not match any other word input: ")
w4 = input("Please input fourth word that does not match any other word input: ")
w5 = input("Please input fifth word that does not match any other word: ")

#Create a list
word_list=[w1,w2,w3,w4,w5]
#Find the index length of each word
length_1 = len(w1)
length_2 = len(w2)
length_3 = len(w3)
length_4 = len(w4)
length_5 = len(w5)
#List the index length of each word
index_list = [length_1, length_2, length_3, length_4, length_5]
print(index_list)