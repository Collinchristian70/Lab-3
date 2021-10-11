import re

# open the text file and read the data
file = open('file.log','r')
text = file.read()
# match a regex pattern for formatted dates
matches = re.findall(r'(\d\d+/Apr/1995+)',text) + re.findall(r'(\d\d+/May/1995+)',text) + re.findall(r'(\d\d+/Jun/1995+)',text) + re.findall(r'(\d\d+/Jul/1995+)',text) + re.findall(r'(\d\d+/Aug/1995+)',text) + re.findall(r'(\d\d+/Sep/1995+)',text) + re.findall(r'(\d\d+/Oct/1995+)',text)
print('logs in file from last six months(april-oct):')
print(len(matches))