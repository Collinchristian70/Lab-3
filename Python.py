from http.client import CONFLICT, EXPECTATION_FAILED, FAILED_DEPENDENCY, FORBIDDEN, GONE, LENGTH_REQUIRED, LOCKED, METHOD_NOT_ALLOWED, NOT_ACCEPTABLE, NOT_FOUND, PAYMENT_REQUIRED, PRECONDITION_FAILED, PROXY_AUTHENTICATION_REQUIRED, REQUEST_HEADER_FIELDS_TOO_LARGE, REQUEST_TIMEOUT, REQUESTED_RANGE_NOT_SATISFIABLE, TOO_MANY_REQUESTS, UNAUTHORIZED, UNPROCESSABLE_ENTITY, UNSUPPORTED_MEDIA_TYPE, UPGRADE_REQUIRED
from typing import Counter
from urllib import request
remote_url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local_file = 'Log_file_download.txt'
request.urlretrieve(remote_url, local_file)

total_log = 0
for line in open('Log_file_download.txt'): total_log += 1
print()
print('There were', total_log, 'requests made in the time period represented by the log.')

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

print('There Were', april+april2+april3+april4+april5+april6+april7+april8+april9+april10+april11+april12+april13+april14
+april15+april16+april17+april18+april19+april20+may+june+july+august+september+october+
october2+october3+october4+october5+october6+october7+october8+october9+october10+october11,
'requests within the last 6 months')

# Start Question part 3 (4xx status codes)
a = open("Log_file_download.txt", "r")
b = a.read()

badrequest = b.count('400')
UNAUTHORIZED = b.count('401')
PAYMENT_REQUIRED = b.count('402')
FORBIDDEN = b.count('403')
NOT_FOUND = b.count('404')
METHOD_NOT_ALLOWED = b.count('405')
NOT_ACCEPTABLE = b.count('406')
PROXY_AUTHENTICATION_REQUIRED = b.count('407')
REQUEST_TIMEOUT = b.count('408')
CONFLICT = b.count('409')
GONE = b.count('410')
LENGTH_REQUIRED = b.count('411')
PRECONDITION_FAILED = b.count('412')
payloadlarge = b.count('413')
URItooLong = b.count('414')
UNSUPPORTED_MEDIA_TYPE = b.count('415')
REQUESTED_RANGE_NOT_SATISFIABLE = b.count('416')
EXPECTATION_FAILED = b.count('417')
teapot = b.count('418')
misdirected_request = b.count('421')
UNPROCESSABLE_ENTITY = b.count('422')
LOCKED = b.count('423')
FAILED_DEPENDENCY = b.count('424')
too_early = b.count('425')
UPGRADE_REQUIRED = b.count('426')
PRECONDITION_FAILED = b.count('428')
TOO_MANY_REQUESTS = b.count('429')
REQUEST_HEADER_FIELDS_TOO_LARGE = b.count('431')
unavailable_legal = b.count('451')

four_error = (badrequest+UNAUTHORIZED+PAYMENT_REQUIRED+FORBIDDEN+NOT_FOUND+METHOD_NOT_ALLOWED+NOT_ACCEPTABLE+
PROXY_AUTHENTICATION_REQUIRED+REQUEST_TIMEOUT+CONFLICT+GONE+LENGTH_REQUIRED+PRECONDITION_FAILED+payloadlarge+URItooLong+
UNSUPPORTED_MEDIA_TYPE+REQUESTED_RANGE_NOT_SATISFIABLE+EXPECTATION_FAILED+teapot+misdirected_request+UNPROCESSABLE_ENTITY+
LOCKED+FAILED_DEPENDENCY+too_early+UPGRADE_REQUIRED+PRECONDITION_FAILED+TOO_MANY_REQUESTS+REQUEST_HEADER_FIELDS_TOO_LARGE+
unavailable_legal)

print('There are',four_error,'4xx status codes in the log file')
# End Question part 3 (4xx status codes)
