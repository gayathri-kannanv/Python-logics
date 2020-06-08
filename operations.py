num1= int(input("Enter the first number : "))
num2= int(input("Enter the second number : "))
def oper():
    op= int(input("Which operation to perform? \n 1: ARITHMETIC \n 2: RELATIONAL \n 3: LOGICAL \n 4: BITWISE \n 5: ASSIGNMENT \n 6: EXIT"))
    operation(op)

def operation(op):
    switcher = {
        1: lambda: arithmetic(),
        2: lambda: relational(),
        3: lambda: logical(),
        4: lambda: bitwise(),
        5: lambda: assignment(),
        6: lambda: exit()
    }
    return switcher.get(op, lambda: "Invalid value")()


def arithmetic():
    ar=int(input("Which arithmetic operation to perform? \n1: ADD \n2: SUB \n3: MUL \n4: DIV \n5: POWER "))
    
    if ar==1: print(num1+num2)
    elif ar==2: print(num1-num2)
    elif ar==3: print(num1*num2)
    elif ar==4: print(num1/num2)
    elif ar==5: print(num1**num2)
    else: print("Invalid value")
    oper()
 
def relational():
    re=int(input("Which relational operation to perform? \n1: >\n2: <\n3: ==\n4: !=\n5: >=\n6: <= "))
    if re==1: print(num1>num2)
    elif re==2: print(num1<num2)
    elif re==3: print(num1==num2)
    elif re==4: print(num1!=num2)
    elif re==5: print(num1>=num2)
    elif re==6: print(num1<=num2)
    else: print("Invalid value")
    oper()

def logical():
    lo=int(input("Which logical operation to perform? \n1: AND\n2: OR\n3: NOT"))
    if lo==1: print(num1 and num2)
    if lo==2: print(num1 or num2)
    if lo==3: print(not num1, not num2)
    else: print("Invalid value")
    oper()
  
def bitwise():
    bi=int(input("Which bitwise operation to perform? \n1: Bitwise AND   \n2: Bitwise OR   \n3: Bitwise NOT   \n4: Bitwise XOR  "))
    if bi==1: print(num1 & num2)
    elif bi==2: print(num1 | num2)
    elif bi==3: print(~ num1, ~ num2)
    elif bi==4: print(num1 ^ num2)
    else: print("Invalid value")
    oper()
 
def assignment():
    num=2
    ass=int(input("Which assignment operation to perform? \n1: +=\n2: -= \n3: *=\n4: /= \n5: %= "))
    if ass==1:
        num += num2
        print(num)
    elif ass==2:
        num -= num2
        print(num)
    elif ass==3:
        num *= num2
        print(num)
    elif ass==4:
        num /= num2
        print(num)
    elif ass==5:
        num %= num2
        print(num)
    else: print("Invalid value")
    oper()
     
oper()
