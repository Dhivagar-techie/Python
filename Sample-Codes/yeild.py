def increment(n):
    i=1
    while i<=n:
        yield i
        i+=1



for number in increment(5):
    print(number)

