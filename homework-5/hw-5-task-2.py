list1 = ['Mary', 'Jack', 'Peter', 'Elithabeth',  'Tony', 'Ben', 'Nina']
word = input("Word: ")

if word not in list1:
    print("Not found")
elif list1.index(word) % 2 == 0:
    print("it’s all good")
else:
    list1.remove(word)
    print(list1)
