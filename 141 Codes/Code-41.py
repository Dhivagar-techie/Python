# Remove punctuation from string

punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

letter=input("Enter the Word to check:")

store=""

for i in letter:
    if i not in punctuation:
        store=store+i

print(store)

