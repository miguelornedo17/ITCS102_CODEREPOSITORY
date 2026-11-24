def numbers(size):
    for x in range (size):
        for y in range (size, 0, -1):
            print("*", end=" ")
        print()

def sum(x, y):
    return x+y

def box(size):
    for x in range(size + 1):
        for y in range (size + 1):
            if x == 0 or y == 0 or x == size or y == size:
                print("*", end=" ")
            else :
                print(" ", end=" ")
        print()

def my_Factorial(number):
    fact = 1
    for x in range (number, 0, -1):
        fact *= x
    return fact

numbers(10)
numbers(5)
numbers(8)

print(sum(10, 5))
print(sum(5, 20))
print(sum(20, 10))

box(6)
box(10)

print(my_Factorial(4))