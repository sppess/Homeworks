str1 = input("Enter your string: ")
if len(str1) < 7:
    print("Error")
else:
    a = len(str1)//2 - 1
    b = len(str1)//2 + 1
    print(str1[a:b+1])
