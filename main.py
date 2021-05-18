"main function"

import casting

s1 = input("Please type network address: ")
s2 = input("Please type subnet mask: ")

net_add = s1.split(".")
sub_mas = s2.split(".")

check_arr = ["128", "192", "224", "240", "248", "252", "255"]
for elem in net_add:
    if elem < 0 or elem > 255:
        raise ValueError("The network adress is not correct")
for elem in sub_mas:
    if elem not in check_arr:
        raise ValueError("The subnetmask is not correct")
answer = []
i = 0
while sub_mas[i] == "255":
    answer.append(net_add[i])
    i += 1
bi_sub = casting.de_to_bi(int(sub_mas[i]))
sep = bi_sub.index("0")
bi_net = casting.de_to_bi(int(net_add[i]))
