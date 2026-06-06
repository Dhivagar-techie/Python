# Write a program to compute the frequency of the words from the input. The outputshould output after sorting the key alphanumerically.

Texts=input("enter your Sentances:")

word=Texts.split()

Funct={}

for i in word:
    if i in Funct:
        Funct[i]+=1
    else:
        Funct[i]=1

for j in sorted(Funct):
    print(f"{j}:{Funct[j]}")