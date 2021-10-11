import re

# open the text file and read the data
file = open('file.log','r')
text = file.read()
m=[]
# match a regex pattern for formatted dates
matches = re.findall(r'(" 2\d\d)',text)
print(len(matches))
matches = re.findall(r'(" 3\d\d)',text)
print(len(matches))
matches = re.findall(r'(" 4\d\d)',text)
print(len(matches))
matches = re.findall(r'(" 1\d\d)',text)
print(len(matches))
matches = re.findall(r'(" 5\d\d)',text)
print(len(matches))

m += re.findall(r'(" 1\d\d)',text)
m += re.findall(r'(" 2\d\d)',text)
m += re.findall(r'(" 3\d\d)',text)
m += re.findall(r'(" 4\d\d)',text)
m += re.findall(r'(" 5\d\d)',text)
print(len(m))