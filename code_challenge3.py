sender = input("Sender Name --> ")
item = input("Type of item --> ")
isFragile = bool(input("is it fragile --> "))
weight = float(input("Weight of the item in kg --> "))
distance = float(input("Distance in km --> "))
is_express = bool(input("Express --> "))
is_international = bool(input("International --> "))

if weight <= 2 and distance <= 100 and is_express == False and is_international == False : 
	print("Shipping fee is Free")
elif is_international 

base_cost = (weight * 2.50) + (distance * 0.15)
if isFragile == True :
	print("Fragile") 
else : 
	print("Not Fragile")
