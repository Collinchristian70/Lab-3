from urllib import request
import re

remote_url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local_file = 'Log_file_download.txt'
request.urlretrieve(remote_url, local_file)
file = open('Log_file_download.txt', 'r')
text = file.read()

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


