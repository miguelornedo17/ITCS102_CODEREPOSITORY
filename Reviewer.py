age = int(input("What is your Age --> "))
rev = float(input("What is your Monthly Revenue --> "))
cs = int(input("What is your Credit Score -- > "))
years_in_business = float(input("How many years are you in Business --> "))
has_default = bool(input("Do you hsve Dafaults --> "))
collateral_name = str(input("What is the Collateral Name --> "))
collateral_value = float(input("What is your Collateral Value --> "))

max_loan = 0
base_value = 0

if age >= 21 and years_in_business >= 2.0 and has_default == False :
    print("Baseline pass")
    if cs >= 720:
        max_loan = 3 * rev
        print("You have High credit score, You can loan maximum amount of ", max_loan)
        if rev >= 50000 :
            base_value = max_loan * 0.015
            print("You have a High Monthly Revenue and you can loan", base_value)
        else :
            base_value = max_loan * 0.025
            print("Your Base fee rate is", base_value)
        if collateral_value >= max_loan :
            print("Collateral", collateral_name, "withta value of",collateral_value,"is Accepted")
        else: 
            print("Rejected: Insufficient collateral value for", collateral_name)
        surge_fee_rate = max_loan * base_value
        if max_loan % 500 != 0 :
            surge_fee_rate += 250
            print("Updated base fee is", surge_fee_rate)
    elif cs >= 620 and cs < 720 :
        max_loan = 1.5 * rev
        print("Your credir score is inside of 620 to 720 and you can loan at the maximum amount of", max_loan)
        if years_in_business >= 5.00 :
            base_value = 0.02 * max_loan
            print("Your Base free rate is", base_value)
        else :
            base_value = 0.035 * rev
            print("Your Business is less than 5 years")
            print("Your Base free rate is", base_value)
        if collateral_value >= max_loan :
            print("Collateral", collateral_name, "withta value of",collateral_value,"is Accepted")
        else: 
            print("Rejected: Insufficient collateral value for", collateral_name)
        surge_fee_rate = max_loan * base_value
        if max_loan % 500 != 0 :
            surge_fee_rate += 250
            print("Updated base fee is", surge_fee_rate)
    elif cs < 620 :
        print("Rejected: Credit Score is to Low")
    else:
        print("You have low credit score")
else :
    print("You did not meet the requirements")
