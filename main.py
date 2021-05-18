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
bi_sub = casting.de_to_bi(int(sub_mas[i]))
div = bi_sub.index("0")
bi_net = casting.de_to_bi(int(net_add[i]))
tmp_net = bi_net[:div] + "0" * (8 - div)
tmp_broad = bi_net[:div] + "1" * (8 - div)
answer_net.append(str(casting.bi_to_de(int(tmp_net))))
answer_broad.append(str(casting.bi_to_de(int(tmp_broad))))
i += 1
while i != 4:
    answer_net.append("0")
    answer_broad.append("255")
    i += 1
print (".".join(answer_net))
print (".".join(answer_broad))