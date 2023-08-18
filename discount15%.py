product_price=float(input("pls enter the price of product="))
product_newprice=(product_price*15)/100
print("this is product new price with 15% dis=",product_newprice)

if product_newprice>=4000 and product_price<5000:
   product_dis=(product_newprice*18)/100
   final_price=product_newprice-product_dis
   print("this is final_price with 18% dis=",final_price)

elif product_newprice>=1000:
   product_dis=(product_newprice*12)/100
   final_price=product_newprice-product_dis
   print("this is final_price with 12% dis=",final_price)

else:
   flat_dis=(product_newprice*10)/100
   final_price=product_newprice-flat_dis
   print("this is final_price with 10% flat dis=",final_price)
