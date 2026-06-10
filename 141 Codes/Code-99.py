# Create a function that replaces all the vowels in a string with a specified character.
def replace_volwels(letter,sp_let):
    store="AEIOUaeiou"
    for i in store:
        letter=letter.replace(i,sp_let)
    return letter

A=replace_volwels("Aeiou","*")
print(A)

#Alternative MEthods

def repla_vowels(let,spe_let):
    store="AEIOUaeiou"
    final=""
    for i in let:
             if i in store:
                final+=spe_let
             else:
                final+=i
    return final

print(repla_vowels("hello world", "*"))


