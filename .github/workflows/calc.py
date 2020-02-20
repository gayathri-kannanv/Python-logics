import maths.add
import maths.sub
import maths.mul
import maths.div
import maths.expo

ch='y'
while(ch=='y'):
    option={1:"ADD",2:"SUB",3:"MUL",4: "DIV",5:"EXPONENT"}
    calc=int(input("CALCULATION- ENTER YOUR OPTION:\n1: ADD\n2:SUB\n3:MUL\n4:DIV\n5:EXPONENT\n=> "))
    if calc not in option:
        print("invalid option!!")
    else:
        if calc==1:
            print ("ENTER THE VALUES TO ADD:\n")
        
            print (maths.add.add())
        elif calc==2:
            print ("ENTER THE VALUES TO SUB:\n")
        
            print (maths.sub.sub())
        elif calc==3:
            print ("ENTER THE VALUES TO MULTIPLY:\n")
        
            print (maths.mul.mul())
        elif calc==4:
            print ("ENTER THE VALUES TO DIVIDE:\n")
       
            print (maths.div.div())
        elif calc==5:
            print ("ENTER THE VALUES TO EXPONENT:\n")
       
            print (maths.expo.expo())
    ch=input("DO U WANT TO CONTINUE?(y/n): ")
    print ("==========================================================================")
     
