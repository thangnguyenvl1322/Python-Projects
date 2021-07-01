import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')


for line in fhand:
    x = line.decode().strip()
    divider = x.split()
    print(divider)
