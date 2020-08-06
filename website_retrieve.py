import urllib.request, urllib.error, urllib.parse

file1= urllib.request.urlopen('https://google.com')
for line in file1:
	print(line.decode().strip())