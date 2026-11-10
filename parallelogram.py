# num = int(input("Enter Size --> "))
r = 5
c = 9 

for x in range (1, c+1) :
    for y in range (1, r+1) :
        if (x <= 5 and (x + y == 6 or y == 5)) or (x >= 6 and (x + y == 10 or y == 1 )) :
            print("*", end=" ")
        else :
            print(" ", end=" ")
    print()