# To check if arr1 is subset of arr2

n1= int(input())
n2= int(input())
arr1= list(map(int, input().split()))[:n1]
arr2= list(map(int, input().split()))[:n2]

i=0
j=0
count=0
for i in range(n1):
    for j in range(n2):
        if(arr1[i]==arr2[j]):
            count+=1
            break

    if(j==n2):
        break

if(count==n1):
    print("yes")
else:
    print("no")
