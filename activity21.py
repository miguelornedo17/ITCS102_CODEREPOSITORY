sum = 0 

continue_loop = True

while continue_loop == True:
    x = int(input("Enter a number --> "))

    if x == 0:
        print("Loop Terminated")
        print("The sum is: ", sum)
        break
    else:
        print("Continue Looping")
        print("The current sum is: ", sum)
        sum += x
        continue 
    