"Calculating a max subnetmask both IP addresses"

import casting

def cnt_sub(ip1, ip2):
    """
    Find location seperated
    """
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
