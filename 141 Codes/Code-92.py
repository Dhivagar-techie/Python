# Write a function that stutters a word as if someone is struggling to read it. The firsttwo letters are repeated twice with an ellipsis ... and space after each, and then theword is pronounced with a question mark ?.

def stutters(n):
    A=f"{n[:2]}..{n[:2]}..{n}?"
    return A

n=input("enter the words:")

print(stutters(n))