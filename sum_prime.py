max=int(input("ENTER THE MAXIMUM VALUE OF THE RANGE:"))
sum=0
for i in range (1,max):
  if i>1:
    for j in range (2,i):
      if i%j==0:
        break;
    else:
      sum=sum+i
print("THE SUM OF PRIME NUMBERS IN THE GIVEN RANGE IS: ",sum)
