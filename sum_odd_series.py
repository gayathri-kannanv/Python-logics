min=int(input("ENTER THE MINIMUM VALUE OF THE RANGE:"))
max=int(input("ENTER THE MAXIMUM VALUE OF THE RANGE:"))
sum=0
for i in range (min,max):
  if i%2!=0:        
    sum=sum+i
print("THE SUM OF PRIME NUMBERS IN THE GIVEN RANGE IS: ",sum)

