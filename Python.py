from typing import Counter
from urllib import request
remote_url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local_file = 'Log_file_download.txt'
request.urlretrieve(remote_url, local_file)

count = 0
for line in open('Log_file_download.txt'): count += 1
print()
print('There were', count, 'requests made in the time period represented by the log.')

x = open("Log_file_download.txt", "r")
y = x.read()
april = y.count('11/Apr/1995')
april2 = y.count('12/Apr/1995')
april3 = y.count('13/Apr/1995')
april4 = y.count('14/Apr/1995')
april5 = y.count('15/Apr/1995')
april6 = y.count('16/Apr/1995')
april7 = y.count('17/Apr/1995')
april8 = y.count('18/Apr/1995')
april9 = y.count('19/Apr/1995')
april10 = y.count('20/Apr/1995')
april11 = y.count('21/Apr/1995')
april12 = y.count('22/Apr/1995')
april13 = y.count('23/Apr/1995')
april14 = y.count('24/Apr/1995')
april15 = y.count('25/Apr/1995')
april16 = y.count('26/Apr/1995')
april17 = y.count('27/Apr/1995')
april18 = y.count('28/Apr/1995')
april19 = y.count('29/Apr/1995')
april20 = y.count('30/Apr/1995')
may = y.count('May/1995')
june = y.count('Jun/1995')
july = y.count('Jul/1995')
august = y.count('Aug/1995')
september = y.count('Sep/1995')
may = y.count('May/1995')
june = y.count('Jun/1995')
july = y.count('Jul/1995')
august = y.count('Aug/1995')
september = y.count('Sep/1995')
october = y.count('1/Oct/1995')
october2 = y.count('2/Oct/1995')
october3 = y.count('3/Oct/1995')
october4 = y.count('4/Oct/1995')
october5 = y.count('5/Oct/1995')
october6 = y.count('6/Oct/1995')
october7 = y.count('7/Oct/1995')
october8 = y.count('8/Oct/1995')
october9 = y.count('9/Oct/1995')
october10 = y.count('10/Oct/1995')
october11 = y.count('11/Oct/1995')

<<<<<<< HEAD
print('There Were ', april+april2+april3+april4+april5+april6+april7+april8+april9+april10+april11+april12+april13+april14+april15+april16+april17+april18+april19+april20+may+june+july+august+september+october+october2+october3+october4+october5+october6+october7+october8+october9+october10+october11, ' requests within the last 6 months')
=======
print()
print('There were', april+april2+april3+april4+april5+april6+april7+april8+april9+april10+april11+april12+april13+april14+april15+april16+april17+april18+april19+april20+may+june+july+august+september+october+october2+october3+october4+october5+october6+october7+october8+october9+october10+october11, ' requests within the last 6 months')
>>>>>>> gustavo's
