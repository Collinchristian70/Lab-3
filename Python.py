from typing import Counter
from urllib import request
remote_url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local_file = 'Log_file_download.txt'
request.urlretrieve(remote_url, local_file)

count = 0
for line in open('Log_file_download.txt'): count += 1 
print ('There were ', count, ' requests made in the time period represented by the log.') 

x = open("Log_file_download.txt", "r")
y = x.read()
april = y.count('11/Apr/1995')
april2 = y.count('12/Apr/1995')
#print(april)
#print(april2)
may = y.count('May/1995')
#print(may)
june = y.count('Jun/1995')
#print(june)
july = y.count('Jul/1995')
#print(july)
august = y.count('Aug/1995')
#print(august)
september = y.count('Sep/1995')
#print(september)

sum = april + april2 + may + june + july + august + september
print('There were ', sum, 'requests made within the past 6 months.')