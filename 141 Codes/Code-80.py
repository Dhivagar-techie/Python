#  Program to check valid passwords

password=input("enter your password:")

store=[]

lower=False
Capital=False
digital=False
special=False

if  len(password)>6 and len(password)<12:
    
    for i in password:
        if i.islower():
            lower=True
        elif i.isupper():
            Capital=True
        elif i.isdigit():
            digital=True
        elif i in "@#$&":
            special=True

    if lower and Capital and digital and special:
         store.append(password)

print(store)


