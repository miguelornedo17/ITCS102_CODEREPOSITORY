for x in range(6, 1, -1):
    for y in range(1, x):
        print("*", end=" ")
    print(" ")

for x in range(1, 6):
    for y in range(1, x):
        print(x, end=" ")
    print(x)
