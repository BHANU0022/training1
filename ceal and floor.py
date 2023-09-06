a = float(input("Enter value first :"))
b = float(input("Enter value sec:"))
print("a",type(a),"b", type(b))
sum = a + b
print("Sum of a +b", round(sum,3))
# Floor and ceil
import math
print("Floor value of ",math.floor(a))
print("Ceil value of ",math.ceil(a))
a +=a # a = a +a
print(a)