from http.client import CONFLICT, EXPECTATION_FAILED, FAILED_DEPENDENCY, FORBIDDEN, GONE, LENGTH_REQUIRED, LOCKED, METHOD_NOT_ALLOWED, NOT_ACCEPTABLE, NOT_FOUND, PAYMENT_REQUIRED, PRECONDITION_FAILED, PROXY_AUTHENTICATION_REQUIRED, REQUEST_HEADER_FIELDS_TOO_LARGE, REQUEST_TIMEOUT, REQUESTED_RANGE_NOT_SATISFIABLE, TOO_MANY_REQUESTS, UNAUTHORIZED, UNPROCESSABLE_ENTITY, UNSUPPORTED_MEDIA_TYPE, UPGRADE_REQUIRED
from typing import Counter
from urllib import request
import re
remote_url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local_file = 'Log_file_download.txt'
request.urlretrieve(remote_url, local_file)


textfile = open('Log_file_download.txt', 'r')
filetext = textfile.read()
textfile.close()
matches = re.findall("\" 4\d\d", filetext)
matches2 = re.findall("\" 3\d\d", filetext)
list = len(matches)
list2 = len(matches2)
print("There were", list, "4xx errors in the log file")
print("There were", list2, "3xx errors in the log file")

