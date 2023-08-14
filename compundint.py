# compund intrest=p(1+r/100)^t-p
p=int(input("enter the principle amount"))
r=int(input("enter the rate"))
t=int(input("enter the time period"))
a=p*(pow((1+r/100),t))
print("final amount is",a)
ci=a-p
print("compound intrest is", ci)





