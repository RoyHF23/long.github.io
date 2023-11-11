a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if a+b>c and a+c>b and b+c>a :
   p=(a+b+c)/2
   s=p*(p-a)*(p-b)*(p-c)
   import math 
   S= math.sqrt(s)
   X= round(S,3)
   print("Dien tich=",X,sep="")
else :
  print("Khong hop le")
  