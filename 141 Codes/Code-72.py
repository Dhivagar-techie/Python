# Write a Python program to check order of character in string using OrderedDict().

# Write a Python program to check order of character in string using OrderedDict()

from collections import OrderedDict

def check_order(string, pattern):
    
    # Create an OrderedDict from the string
    dict1 = OrderedDict.fromkeys(string)

    ptr = 0

    # Traverse through ordered keys
    for key in dict1.keys():
        if key == pattern[ptr]:
            ptr += 1

        # If all characters matched
        if ptr == len(pattern):
            return True

    return False


# Input
string = "engineers rock"
pattern = "egr"

# Function call
if check_order(string, pattern):
    print("Pattern characters are in order")
else:
    print("Pattern characters are not in order")