from urllib import request
remote_url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local_file = 'Log_file_download.txt'
request.urlretrieve(remote_url, local_file)

with open('Log_file_download.txt') as f:
    contents = f.read()
    print(contents)