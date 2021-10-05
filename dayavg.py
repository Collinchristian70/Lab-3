import re

# open the text file and read the data
file = open('file.log','r')
text = file.read()
# match a regex pattern for formatted dates

i=0
matches = []
count = []
total = 0

lines = file.readlines()
for line in lines:
    total=total+1

print('Total logs in file:')
print(total)

while i<32:
    day= str(i)

    if i<10:
        day= '0'+str(i)
        count = (re.findall(r'('+day+r'/\w\w\w/\d\d\d\d)',text))
        print('day', + i)
        print(len(count))
        avg = int(total)/len(count)
        print('avg:', + avg)

    else:
        day=str(i)
        count = (re.findall(r'('+day+r'/\w\w\w/\d\d\d\d)',text))
        print('day', + i)
        print(len(count))
        avg = int(total)/len(count)
        print('avg:', + avg)

    if i<10:
        day= '0'+str(i)
        matches += (re.findall(r'('+day+r'/\w\w\w/\d\d\d\d)',text))
    else:
        day=str(i)
        matches += (re.findall(r'('+day+r'/\w\w\w/\d\d\d\d)',text))

    i+=1


print(len(matches))

