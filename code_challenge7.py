size = int(input("What is the size? --> "))

for x in range(size):
    for y in range(size - x - 1):
        print(" ", end="")
    for z in range(2 * x + 1):
        print("*", end="")
    print()
    
for x in range(size - 1):
    for y in range(x + 1):
        print(" ", end="")
    for z in range(2 * (size - x - 2) + 1):
        print("*", end="")
    print()
