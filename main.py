"Main function"

import casting

s1 = input("Please type network address: ")
s2 = input("Please type subnet mask: ")

net_add = s1.split(".")
sub_mas = s2.split(".")
if len(net_add) != 4 or len(sub_mas) != 4:
    raise ValueError("The address must consist of 4 octats")

check_arr = ["0", "128", "192", "224", "240", "248", "252", "255"]
for elem in net_add:
    if int(elem) < 0 or int(elem) > 255:
        raise ValueError("The network adress is not correct")
for elem in sub_mas:
    if elem not in check_arr:
        raise ValueError("The subnetmask is not correct")
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

print ("\n======================RETURNS======================\n")
print ("Net Address         : " + ".".join(answer_net))
print ("Broadcast Adress    : " + ".".join(answer_broad))
print ("Allocable range     : " + ".".join(answer_start) + " - " + ".".join(answer_end))
print ("Number of ranges    : " + "2^" + str(CNT) + " - 2 (" + str(2 ** CNT - 2) + ")")
print ()
