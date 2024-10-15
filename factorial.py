num=5
factorial=1 
if num<0:
   print("factorial does not exist")
elif num==0:
   print("the facorial of 0 is 1")
else:
    for i in range (1,num+1):
        factorial=factorial*i
    print("the factorial of",num,"is",factorial)