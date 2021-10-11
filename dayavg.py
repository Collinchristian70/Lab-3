import re

# open the text file and read the data
file = open('file.log','r')
text = file.read()
# match a regex pattern for formatted dates

i=0
matches = []
count = []
total = 0

total = re.findall(r'local',text) + re.findall(r'remote',text)
print('Total logs in file:')
print(len(total))

while i<32:
    day= str(i)

    if 1<=i<10:
        day= '0'+str(i)
        count = (re.findall(r'('+day+r'/\w\w\w/\d\d\d\d)',text))
        print('day', + i)
        print(len(count))

    else:
        day=str(i)
        count = (re.findall(r'('+day+r'/\w\w\w/\d\d\d\d)',text))
        print('day', + i)
        print(len(count))

    if i<10:
        day= '0'+str(i)
        matches += (re.findall(r'('+day+r'/\w\w\w/\d\d\d\d)',text))
    else:
        day=str(i)
        matches += (re.findall(r'('+day+r'/\w\w\w/\d\d\d\d)',text))

    i+=1


print(len(matches))

