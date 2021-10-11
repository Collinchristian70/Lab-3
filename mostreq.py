#import re

# open the text file and read the data
#file = open('file.log','r')
#text = file.read()


# match a regex pattern for formatted dates
#html = re.findall(r'.html',text) 
#gif = re.findall(r'.gif',text)
#xmb = re.findall(r'.xmb',text)

#print(len(html)
#print(len(gif))
#cprint(len(xmb))

import collections

logfile = open("file.log", "r")

clean_log=[]

for line in logfile:
    try:
        # copy the URLS to an empty list.
        # We get the part between GET and HTTP
        clean_log.append(line[line.index("GET")+4:line.index("HTTP")])
    except:
        pass

counter = collections.Counter(clean_log)

# get the Top 50 most popular URLs
for count in counter.most_common(50):
    print(str(count[1]) + "	" + str(count[0]))

logfile.close()