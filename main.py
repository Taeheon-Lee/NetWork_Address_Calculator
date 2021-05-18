import casting

s1 = input("Please type network address: ")
s2 = input("Please type subnet mask: ")

lst1 = map(int, s1.split("."))
lst2 = map(int, s2.split("."))