row= 3
space=row-1
for i in range (1,row+1) :
    for j in range(1,space+1) :
        print(end=" ")
    space = space-1

    for j in range(2*i-1) :
        print(end="*")
    print()

space = 1
for i in range(1,row) :
    for j in range(1, space + 1) :
        print(end=" ")
    space = space + 1
    for j in range(1,2*(row-i)) :
        print(end="*")
    print()