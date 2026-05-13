
# Another method of HarshadNumber

num = int(input("Enter number: "))

digit_sum = sum(int(i) for i in str(num))

store=digit_sum

if num%store==0:
    print("ok")
else:
    print("error")