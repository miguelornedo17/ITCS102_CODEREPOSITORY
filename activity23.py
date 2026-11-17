shonen = []
sci-fi = []
adventure = []
isekai = []
romans = []
yuri = []

while True:
    ans = int(input("Do you wantch anime --> ")).lower()

    if ans == "yes" :
        print("what kind of anime do you watch or read")
        print("1 shonen \n2 sci-fi\n3 adventure\n4 isekai\n5 romans \n6 yuri")

        choose = int(input("input --> "))
        if choose == 1:
            print("SHONEN")
            title = input("please input the title of the anime --> ")
            shonen.append(title)
            print("list of shonen")
            print(shonen)
            con = input("Do you wish to continue yes/no ").lower()
            if con == "yes":
                continue
            else:
                break
        else:
            print("INVALID choice")
