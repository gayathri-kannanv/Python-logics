import urllib.request, urllib.error, urllib.parse

file1= urllib.request.urlopen('file:///F:/website.html')
for line in file1:
	print(line.decode().strip())
