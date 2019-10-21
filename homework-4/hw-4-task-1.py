sentence = "test1, test2, test3, test4, test5"
num = int(input('Number: '))
l_sen = sentence.split(", ")
if num + 1 > len(l_sen) + 1:
    print("Element out of range")
else:
    del l_sen[num - 1]
    print(', '.join(l_sen))


sentence2 = "test1, test2, test3, test4, test5"
n = str(num)
if num < 5:
    delete = "test" + n + ", "
else:
    delete = ", test" + n
print(sentence2.replace(delete, ""))
