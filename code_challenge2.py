money = 1456
money1 = 1456
thousand = money//1000
money = money-thousand*1000
fivehundred = money//500
money = money-fivehundred*500
twohundred = money//200
money = money-twohundred*200
onehundred = money//100
money = money-onehundred*100
fifty = money//50
money = money-fifty*50
twenty = money//20
money = money-twenty*20
ten = money//10
money = money-ten*10
five = money//5
money = money-five*5
one = money//1
money = money-one*1

print("Money to Deposit -->", money)
print("Money to Deposit -->", thousand)
print("Money to Deposit -->", fivehundred)
print("Money to Deposit -->", twohundred)
print("Money to Deposit -->", onehundred)
print("Money to Deposit -->", fifty)
print("Money to Deposit -->", twenty)
print("Money to Deposit -->", ten)
print("Money to Deposit -->", five)
print("Money to Deposit -->", one)
