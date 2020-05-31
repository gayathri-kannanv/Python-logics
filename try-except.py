num=input("ENTER A NUMBER: ")
try:
    n=int(num)
except:
    n=-1

if(n>=0):
    print("It's a valid number")
else:
    print("Not a number")
