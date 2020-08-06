import urllib.request, urllib.error, urllib.parse

file1= urllib.request.urlopen('F:\count_txt.txt')
counts= dict()
for line in file1:
	words= line.decode().split()
    for i in words:
        counts[i]= counts.get(i,0)+1
        
print(counts)