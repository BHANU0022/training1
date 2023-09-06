#sum and digit number using while loop

number = int(input("Pls input the number"))
sum =0
while number>1000:
    digit = number%10
    sum = sum +digit
    number = number//10
print("- > number - ", number)
print("digit",digit)
print("sum",sum)