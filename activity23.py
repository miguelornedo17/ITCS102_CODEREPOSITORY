shonen = []
sci_fi = []
adventure = []
isekai = []
romans = []
yuri = []

while True:
    ans = input("Do youwatch anime --> ").lower()

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
            rev = input("Do you want to delete an entry? yes/no ").lower()
            if rev == "yes":
                del_title = input("please input the title of the anime you want to delete --> ")
                if del_title in shonen:
                    shonen.remove(del_title)
                    print("list of shonen")
                    print(shonen)
                else:
                    print("title not found")
            con = input("Do you wish to continue yes/no ").lower()
            if con == "yes":
                continue
            else:
                break 
        elif choose == 2:
            print("sci_fi")
            title = input("please input the title of the anime --> ")
            sci_fi.append(title)
            print("list of sci_fi")
            print(sci_fi)
            rev = input("Do you want to delete an entry? yes/no ").lower()
            if rev == "yes":
                del_title = input("please input the title of the anime you want to delete --> ")
                if del_title in sci_fi:
                    sci_fi.remove(del_title)
                    print("list of sci_fi")
                    print(sci_fi)
                else:
                    print("title not found")
            con = input("Do you wish to continue yes/no ").lower()
            if con == "yes":
                continue
            else:
                break
        elif choose == 3:
            print("adventure")
            title = input("please input the title of the anime --> ")
            adventure.append(title)
            print("list of adventure")
            print(adventure)
            rev = input("Do you want to delete an entry? yes/no ").lower()
            if rev == "yes":
                del_title = input("please input the title of the anime you want to delete --> ")
                if del_title in adventure:
                    adventure.remove(del_title)
                    print("list of adventure")
                    print(adventure)
                else:
                    print("title not found")
            con = input("Do you wish to continue yes/no ").lower()
            if con == "yes":
                continue
            else:
                break
        elif choose == 4:
            print("isekai")
            title = input("please input the title of the anime --> ")
            isekai.append(title)
            print("list of isekai")
            print(isekai)
            rev = input("Do you want to delete an entry? yes/no ").lower()
            if rev == "yes":
                del_title = input("please input the title of the anime you want to delete --> ")
                if del_title in isekai:
                    isekai.remove(del_title)
                    print("list of isekai")
                    print(isekai)
                else:
                    print("title not found")
            con = input("Do you wish to continue yes/no ").lower()
            if con == "yes":
                continue
            else:
                break
        elif choose == 5:
            print("romans")
            title = input("please input the title of the anime --> ")
            romans.append(title)
            print("list of romans")
            print(romans)
            rev = input("Do you want to delete an entry? yes/no ").lower()
            if rev == "yes":
                del_title = input("please input the title of the anime you want to delete --> ")
                if del_title in romans:
                    romans.remove(del_title)
                    print("list of romans")
                    print(romans)
                else:
                    print("title not found")
            con = input("Do you wish to continue yes/no ").lower()
            if con == "yes":
                continue
            else:
                break
        elif choose == 6:
            print("yuri")
            title = input("please input the title of the anime --> ")
            yuri.append(title)
            print("list of yuri")
            print(yuri)
            rev = input("Do you want to delete an entry? yes/no ").lower()
            if rev == "yes":
                del_title = input("please input the title of the anime you want to delete --> ")
                if del_title in yuri:
                    yuri.remove(del_title)
                    print("list of yuri")
                    print(yuri)
                else:
                    print("title not found")
            con = input("Do you wish to continue yes/no ").lower()
            if con == "yes":
                continue
            else:
                break
        else:
            print("INVALID choice")
