sender = input("Sender Name --> ")
item = input("Type of item --> ")
isFragile = eval(input("is it fragile (if not press Enter)--> "))
weight = float(input("Weight of the item in kg --> "))
distance = float(input("Distance in km --> "))
is_express = eval(input("Express (if not press Enter)--> "))
is_international = eval(input("International (if not press Enter)--> "))

#Calculation steps
base_cost = (weight * 2.50) + (distance * 0.15)

if weight <= 2 and distance <= 100 and is_express == False and is_international == False : 
	print("Shipping fee is Free")
	Total = 0

elif is_international == True and is_express == True :
	print("International Express Product")
	Total = (base_cost * 1.40) + 50
	
elif is_international == True and weight > 20 or is_express == True :
	print("The Product is Express or Heavy international")
	Total = (base_cost * 1.20) + 25

elif weight > 30 or distance > 1000 :
	print("Oversized Weight")
	Total = base_cost + 30

else :
	print("Standard Rate")
	Total = base_cost 

print("---------------------")
print("Name of the sender --> ", sender)
print("Product name -->", item)
print("Total Price --> PHP", Total)

if isFragile == True :
	print("Product is Fragile")

else :
	print("Product is not Fragile")
