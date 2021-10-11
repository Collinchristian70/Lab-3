from urllib import request
import re
remote_url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local_file = 'Log_file_download.txt'
request.urlretrieve(remote_url, local_file)

textfile = open('Log_file_download.txt', 'r')
filetext = textfile.read()
textfile.close()

print("The most requested file was")
print("The least requested file was")
