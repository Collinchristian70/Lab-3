import re

# open the text file and read the data
file = open('file.log','r')
text = file.read()
# match a regex pattern for formatted dates

i=0
while i<32:
    day= str(i)
    matches = re.findall(r'('+day+r'/\w\w\w/\d\d\d\d)',text)
    i+=1

print(len(matches))

