num = int(input("Enter Size --> "))

for x in range (num) :
    for y in range (num) :
        if x + y == num -1 or y == num-1 :
            print("*", end=" ")
        else :
            print(" ", end=" ")
    print()

for x in range (num) :
    for y in range (num) :
        if x + y == num -1 or y == 0 :
            print("*", end=" ")
        else :
            print(" ", end=" ")
    print()