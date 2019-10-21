str1 = input("Enter your str: ")
num1 = int(input("Enter index: "))
if len(str1) < num1:
    print("Word is too short to cut index")
else:
    print(str1[:num1] + str1[num1 + 1:])
