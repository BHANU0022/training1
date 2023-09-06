# program for odd even no sum.
digit=int(input("enter the digit="))
even_sum=0
odd_sum=0
num=1
while (num<=digit):          # when we take digit is 4 then even sum is 4 but  via the pen calculation 
     if (num%2==0):          # sum is 6 but in program show the 4.
        even_sum=even_sum+num  #now fix the problem , problm is even_se
     else:
          odd_sum=odd_sum+num
     num+=1   
print("sum of even number",even_sum)
print("sum of odd number",odd_sum)