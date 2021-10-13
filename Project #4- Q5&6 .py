import collections

from urllib import request
import re

remote_url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local_file = 'Log_file_download.txt'
request.urlretrieve(remote_url, local_file)
logfile = open('Log_file_download.txt', 'r')

clean_log=[]

for line in logfile:
    try:
        
        clean_log.append(line[line.index("GET")+4:line.index("HTTP")])
    except:
        pass

counter = collections.Counter(clean_log)

print("Most Common File Request:")
# get the Top 50 most popular URLs
for count in counter.most_common(3):
    print(str(count[1]) + "	" + str(count[0]))

print("Least Common File Request:")
for count in counter.most_common() [-3:]:
    print(str(count[1]) + "	" + str(count[0]))



logfile.close()