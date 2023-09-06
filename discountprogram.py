product_price=float(input("pls enter the price of product="))
if product_price>=4000 and product_price<5000:
   product_dis=(product_price*18)/100
   final_price=product_price-product_dis
   print("this is final_price with 18% dis=",final_price)
elif product_price>=1000:
   product_dis=(product_price*12)/100
   final_price=product_price-product_dis
   print("this is final_price with 12% dis=",final_price)
else:
   flat_dis=(product_price*10)/100
   final_price=product_price-flat_dis
   print("this is final_price with 10% flat dis=",final_price)