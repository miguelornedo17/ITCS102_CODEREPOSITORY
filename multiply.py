col = int(input("Enter number of column --> "))

for i in range (1, 11):
    for j in range (1, col + 1):
        print(i, "x", j, "=", i*j, end="\t")
    print()