def add(a,b):
    return a+b
def subract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if(a!=0 and b!=0):
        return a/b
    else:
        return 0
print("CALCULATOR")
x=float(input("ENTER THE FIRST NUMBER:"))
y=float(input("ENTER THE SECOND NUMBER:"))
c=int(input("operation to be performed\n1:addition\n2:subraction\n3:multiplication\n4:division\n what do you prefer:"))
if(c==1):
    d=add(x,y)
    print(f"THE ADDITION OF THE {x} and {y} is {d}")
elif(c==2):
    e=subract(x,y)
    print(f"SUBRACTION of the {x} and {y} is {e}")
elif(c==3):
    f=multiply(x,y)
    print(f" MULTIPLICATION of the {x} and {y} is {f}")
elif(c==4):
    g=divide(x,y)
    print(f"THE DIVISION of the {x} and {y} is {g}")
else:
    print("you choosed the wrong operator")

