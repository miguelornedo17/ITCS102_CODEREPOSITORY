#	age (integer) 
#	is_employed (boolean) 
#	credit_score (integer) 
#	annual_income (float) 
#	has_collateral (boolean) 

age = int(input("Enter your age ---> "))
is_employed = bool(input("Are you employed? (True/False) ---> "))
credit_score = int(input("Entere your credit score --> "))
annual_income = float(input("Enter your annual income ---> "))
has_collateral = bool((input("Do you havr collateral ? (True/False) --->"))

base_rate = 0.0
if age >= 21 and is_employed == True :
    print("Applicant pass the baseline rewuirment"))
    if credit_score >= 750:
        base_rate = 5.0
        print("You have a high vredit score")
        if annual_income >= 100000 :
            base_rate = 4.5
            print("You have a high annual and credit score:", base_rate)
        else:
            print("You have a high annual income and credit score", base_rate)
    elif credit_score >= 600 and credit_score < 750:
        base_rate = 8.0
        print("Youy have a medium credit score")
        if has_collateral == True:
            base_rate = 
            pass
    else:
        pass
    
else:
    pass