import re

# open the text file and read the data
file = open('file.log','r')
text = file.read()
m=[]
count=0 #set count to 0
avg=0
total=0

total = re.findall(r'local',text) + re.findall(r'remote',text)
print("total request")
print(len(total))

# match a regex pattern for formatted dates
matches = re.findall(r'(" 3\d\d)',text)
print("percentage of the requests were redirected elsewhere:")
print(len(total)//len(matches))

matches = re.findall(r'(" 4\d\d)',text)
print("percentage of the requests were not successful:")
print(len(total)//len(matches))


