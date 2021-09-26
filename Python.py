from typing import Counter
from urllib import request
remote_url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local_file = 'Log_file_download.txt'
request.urlretrieve(remote_url, local_file)

count = 0
for line in open('Log_file_download.txt'): count += 1 
print ('There were ', count, ' requests made in the time period represented by the log.') 

f = open("Log_file_download.txt", "r")
content = f.read()
content_list = content.splitlines()
print (content_list)
