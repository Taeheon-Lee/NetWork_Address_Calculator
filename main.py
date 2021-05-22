"Main function"

import casting
import subnet

while 1:
    select = input("Type 1 or 2 or 0\n\n\
1. Network Calculator\n\
2. Max subnet mask for communicating\n\
0. Exit program\n\n\
Type number : ")

    if not select.isdecimal():
        print("\033[33m \nType number \033[31monly\n \033[37m")
        continue

    select = int(select)

    if select == 0:
        print("\033[33m \nGOODBYE :)\n \033[37m")
        break

    if select == 1:
        s1 = input("Please type network address: ")
        s2 = input("Please type subnet mask: ")

        net_add = s1.split(".")
        sub_mas = s2.split(".")
        if len(net_add) != 4 or len(sub_mas) != 4:
            print("\033[31m \nThe address must consist of 4 octats\n \033[37m")
            continue

        check_arr = ["0", "128", "192", "224", "240", "248", "252", "255"]
        for elem in net_add:
            if elem.isdecimal() is False or int(elem) < 0 or int(elem) > 255:
                print("\033[31m \nThe network adress is not correct\n \033[37m")
                continue
        for elem in sub_mas:
            if elem.isdecimal() is False or elem not in check_arr:
                print("\033[31m \nThe subnetmask is not correct\n \033[37m")
                continue
        answer_net = []
        answer_broad = []
        i = 0
        while sub_mas[i] == "255":
            answer_net.append(str(net_add[i]))
            answer_broad.append(str(net_add[i]))
            i += 1
        BI_SUB = str(casting.de_to_bi(int(sub_mas[i])))
        DIV = BI_SUB.index("0")
        CNT = 8 - DIV
        BI_NET = str(casting.de_to_bi(int(net_add[i])))
        tmp_net = BI_NET[:DIV] + "0" * (CNT)
        tmp_broad = BI_NET[:DIV] + "1" * (CNT)
        answer_net.append(str(casting.bi_to_de(int(tmp_net))))
        answer_broad.append(str(casting.bi_to_de(int(tmp_broad))))
        i += 1
        while i != 4:
            answer_net.append("0")
            answer_broad.append("255")
            i += 1
            CNT += 8
        answer_start = answer_net[:]
        answer_start[-1] = str(int(answer_start[-1]) + 1)
        answer_end = answer_broad[:]
        answer_end[-1] = str(int(answer_end[-1]) - 1)

        print("\033[31m", "\n======================RETURNS======================\n")
        print("\033[37m", "Net Address         : " + ".".join(answer_net))
        print("Broadcast Adress    : " + ".".join(answer_broad))
        print("Allocable range     : " + ".".join(answer_start) + " - " + ".".join(answer_end))
        print("Number of ranges    : " + "2^" + str(CNT) + " - 2 (" + str(2 ** CNT - 2) + ")")
        print("\033[31m", "\n===================================================\n")
        input("\033[37m Press Enter to continue...\n")

    elif select == 2:
        ip1 = input("Type first IP address : ")
        ip2 = input("Type second IP address : ")
        SUB_LOC = subnet.cnt_sub(ip1, ip2)
        PREFIX = SUB_LOC

        ip1 = ip1.split(".")
        ip2 = ip2.split(".")
        if len(ip1) != 4 or len(ip2) != 4:
            print("\033[31m \nThe address must consist of 4 octats\n \033[37m")
            continue
        for elem in ip1:
            if elem.isdecimal() is False or int(elem) < 0 or int(elem) > 255:
                print("\033[31m \nThe network adress of ip1 is not correct\n \033[37m")
                continue
        for elem in ip2:
            if elem.isdecimal() is False or int(elem) < 0 or int(elem) > 255:
                print("\033[31m \nThe network adress of ip2 is not correct\n \033[37m")
                continue
        answer_net = []
        answer_broad = []
        i = 0

        while SUB_LOC >= 8:
            answer_net.append(ip1[i])
            answer_broad.append(ip1[i])
            i += 1
            SUB_LOC -= 8
        TMP = str(casting.de_to_bi(int(ip1[i])))
        tmp_net = TMP[:SUB_LOC+1] + "0" * (8 - SUB_LOC)
        answer_net.append(str(casting.bi_to_de(int(tmp_net))))
        tmp_broad = TMP[:SUB_LOC+1] + "1" * (8 - SUB_LOC)
        answer_broad.append(str(casting.bi_to_de(int(tmp_broad))))
        while len(answer_net) != 4:
            answer_net.append("0")
            answer_broad.append("255")

        print("\033[31m", "\n======================RETURNS======================\n")
        print("\033[37m", "PREFIX : ", PREFIX)
        print("network address : ", ".".join(answer_net))
        print("broadcast address : ", ".".join(answer_broad))
        print("\033[31m", "\n===================================================\n")
        input("\033[37m Press Enter to continue...\n")

    else:
        print("\033[33m \nInput number is no correct. Type 1 or 2 or 0\n \033[37m")
        continue
