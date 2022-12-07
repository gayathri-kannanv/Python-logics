s='1 w 2 r 3g'
a=s.split(" ")
b=[]
for i in a:
    try:
            i=i.capitalize()
            b.append(i)
    except:
            b.append(i)
print(b)
print(" ".join(b))