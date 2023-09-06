a=int(input("enter the number"))
s=0
even_sum=0
odd_sum=0
while a>0:
    d=a%10
    if (d%2==0):          
        even_sum=even_sum+d
    else:
          odd_sum=odd_sum+d    
    a=a//10
print("even sum", even_sum)
print("even sum", odd_sum)