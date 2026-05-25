# Write a program that accepts a sequence of whitespace separated words as inputand prints the words after removing all duplicate words and sorting themalphanumerically.

alpha=input("enter the words with spaces:")

store1=alpha.split()

store1.sort()

store3=set(store1)

store2=" ".join(store3)

print(store2)