# Hamming distance is the number of characters that differ between two strings.
def hamming_Distance(string1,string2):
    if len(string1)!=len(string2):
        return f"string length are not matching"
    
    count=0

    for i in range(len(string1)):
        if string1[i]!=string2[i]:
            count+=1

    return count

string1=input("enter your Sequence:")
string2=input("enter your Sequence:")

print(hamming_Distance(string1,string2))
