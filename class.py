import re
import datetime

date = re.findall(r'(\d\d+/\w\w\w/\w\w\w+)',text)
dt = datetime.strptime(logdate,%d/%b/%Y)

# open the text file and read the data
file = open('file.log','r')
text = file.read()
date = re.findall(r'(\d\d+/\w\w\w/\w\w\w+)',text)
dt = datetime.strptime(logdate,%d/%b/%Y)
