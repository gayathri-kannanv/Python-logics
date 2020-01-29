n=int(input("Enter a number:"))
prod=1
while(n>0):
    dig=n%10
    prod=prod*dig
    n=n//10
print("The total sum of digits is:",prod)
