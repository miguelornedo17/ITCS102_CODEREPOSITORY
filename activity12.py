import getpass

username = "Miguel"
password = "migs"

u = input("Input Username --> ")
p = getpass.getpass("Input Password --> ")

if username == u and password == p :
	print("ACCESS GRANTED")
else :
	print("ACCESS DENIED")