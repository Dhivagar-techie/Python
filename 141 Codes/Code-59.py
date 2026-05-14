# Write a Python program to find words which are greater than given length k.

words = ["python", "java", "html", "javascript", "css"]

k=4

for i in words:
    if len(i)>k:
        print(i)