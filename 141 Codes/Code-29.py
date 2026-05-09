# Write a Python Program to calculate your Body Mass Index.
while True:
    height=int(input("Enter the height:"))
    weight=int(input("Enter the weight:"))

    hei_convert=height/100

    bmi=weight/hei_convert**2

    print("Yours bmi:",round(bmi,2))
    a=input("Calculate again \n type yes or no")
    if a.lower()=="no":
        break


