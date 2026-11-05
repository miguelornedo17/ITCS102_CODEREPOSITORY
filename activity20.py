from getpass import getpass

Name = "Migs"
p = "Migs1723"

isLogin = False

while isLogin == False:
    username = input("Enter your username --> ")
    password = getpass("Enter your password --> ")

    if username == Name and password == p:
        print("Login Successful!")
        isLogin = True
    else:
        print("Invalid username or password. Please try again.")
        isLogin = False
