print("Right angled triangle out of asterisks")
n=int(input("please enter the number of rows : "))
for i in range (n) :
    for j in range (i+1) :
        print("* ",end="")
    print()