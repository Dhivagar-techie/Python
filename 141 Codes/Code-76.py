#Write a program that accepts a comma separated sequence of words as input andprints the words in a comma-separated sequence after sorting them alphabetically

Alpha=input("Enter the words without comma:")

store=Alpha.split(",")

store.sort()

sto=",".join(store)

print(sto)

