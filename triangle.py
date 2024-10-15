def triangle(a,b,c):
    if(a+b>c)and (a+c>b)and(b+c>a):
        return True
    else:
        return False
a=int(input("enter the side of A"))
b=int(input("enter the side of B"))
c=int(input("enter the side of C"))
if triangle(a,b,c):
    print("yes")
else:
    print("no")