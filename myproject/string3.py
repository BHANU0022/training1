st = "The string length or size means the total number of characters present in it."  
for i in range(len(st)):
    print(st[i], end="-")

print("\n")
for i in range(len(st)):
    print(st[i], end="%")

print("\n")
for i in range(len(st)-1,-1,-1):
    print(st[i], end="")
