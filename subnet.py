"Calculating a max subnetmask both IP addresses"

import casting

def cnt_sub(ip1, ip2):
    ip1 = ip1.split(".")
    ip2 = ip2.split(".")
    i = 0
    cnt = 0
    
    while ip1[i] == ip2[i]:
        cnt += 8
        i += 1
    bi_ip1 = str(casting.de_to_bi(int(ip1[i])))
    bi_ip2 = str(casting.de_to_bi(int(ip2[i])))
    
    i = 0
    while bi_ip1[i] == bi_ip2[i]:
        cnt += 1
        i += 1
    return cnt

def find_netadd(ip1, ip2):
    sub_loc = cnt_sub(ip1, ip2)
    print ("prefix : ", sub_loc)
    ip1 = ip1.split(".")
    ip2 = ip2.split(".")
    answer_net = []
    answer_broad = []
    i = 0
    
    while sub_loc >= 8:
        answer_net.append(ip1[i])
        answer_broad.append(ip1[i])
        i += 1
        sub_loc -= 8
    tmp = str(casting.de_to_bi(int(ip1[i])))
    tmp_net = tmp[:sub_loc+1] + "0" * (8 - sub_loc)
    answer_net.append(str(casting.bi_to_de(int(tmp_net))))
    tmp_broad = tmp[:sub_loc+1] + "1" * (8 - sub_loc)
    answer_broad.append(str(casting.bi_to_de(int(tmp_broad))))
    while len(answer_net) != 4:
        answer_net.append("0")
        answer_broad.append("255")
    
    answer_net = ".".join(answer_net)
    answer_broad = ".".join(answer_broad)
    
    print(answer_net)
    print(answer_broad)

ip1 = input()
ip2 = input()
find_netadd(ip1, ip2)