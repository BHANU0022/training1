a=int(input("enter the number="))
return_number=0
while a>0:
    d=a%10
    return_number=d+return_number*10
    a=a//10
print("return_number=",return_number)


