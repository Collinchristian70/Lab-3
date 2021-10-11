import re
import datetime

# open the text file and read the data
file = open('file.log','r')
text = file.read()
date = re.findall(r'(\d\d+/\w\w\w/\w\w\w+)',text)
dt = datetime.strptime(logdate,%d/%b/%Y)


matches = re.findall(r'(\d\d+/\w\w\w/\d\d\d\d+)'
df= datetime.strptime(log_date, "%d/%b/%Y")
print(df)

    