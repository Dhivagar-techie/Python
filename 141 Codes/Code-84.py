# Please write a program to generate all sentences where subject is in ["I", "You"] andverb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]

store=[]

for subject in subjects:

    for verb in verbs:

        for obj in objects:

            sen=f"{subject} {verb} {obj}"

            store.append(sen)

for i in store:
    print (i)


# alternative method

subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]

for subject in subjects:

    for verb in verbs:

        for obj in objects:

            print(subject, verb, obj)

  