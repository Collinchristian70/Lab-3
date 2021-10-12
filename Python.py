from http.client import CONFLICT, EXPECTATION_FAILED, FAILED_DEPENDENCY, FORBIDDEN, GONE, LENGTH_REQUIRED, LOCKED, METHOD_NOT_ALLOWED, NOT_ACCEPTABLE, NOT_FOUND, PAYMENT_REQUIRED, PRECONDITION_FAILED, PROXY_AUTHENTICATION_REQUIRED, REQUEST_HEADER_FIELDS_TOO_LARGE, REQUEST_TIMEOUT, REQUESTED_RANGE_NOT_SATISFIABLE, TOO_MANY_REQUESTS, UNAUTHORIZED, UNPROCESSABLE_ENTITY, UNSUPPORTED_MEDIA_TYPE, UPGRADE_REQUIRED
from typing import Counter
from urllib import request
import re
remote_url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local_file = 'Log_file_download.txt'
request.urlretrieve(remote_url, local_file)

total_log = 0
for line in open('Log_file_download.txt'): total_log += 1
print()
print('There were', total_log, 'requests made in the time period represented by the log.')

x = open("Log_file_download.txt", "r")
y = x.read()
april-1 = y.count('11/Apr/1995')
april-2 = y.count('12/Apr/1995')
april-3 = y.count('13/Apr/1995')
april-4 = y.count('14/Apr/1995')
april-5 = y.count('15/Apr/1995')
april-6 = y.count('16/Apr/1995')
april-7 = y.count('17/Apr/1995')
april-8 = y.count('18/Apr/1995')
april-9 = y.count('19/Apr/1995')
april-10 = y.count('20/Apr/1995')
april-11 = y.count('21/Apr/1995')
april-12 = y.count('22/Apr/1995')
april-13 = y.count('23/Apr/1995')
april-14 = y.count('24/Apr/1995')
april-15 = y.count('25/Apr/1995')
april-16 = y.count('26/Apr/1995')
april-17 = y.count('27/Apr/1995')
april-18 = y.count('28/Apr/1995')
april-19 = y.count('29/Apr/1995')
april-20 = y.count('30/Apr/1995')
may-1 = y.count('May/1995')
june-1 = y.count('Jun/1995')
july-1 = y.count('Jul/1995')
august-1 = y.count('Aug/1995')
september-1 = y.count('Sep/1995')
may-1 = y.count('May/1995')
june-1 = y.count('Jun/1995')
july-1 = y.count('Jul/1995')
august-1 = y.count('Aug/1995')
september-1 = y.count('Sep/1995')
october-1 = y.count('1/Oct/1995')
october-2 = y.count('2/Oct/1995')
october-3 = y.count('3/Oct/1995')
october-4 = y.count('4/Oct/1995')
october-5 = y.count('5/Oct/1995')
october-6 = y.count('6/Oct/1995')
october-7 = y.count('7/Oct/1995')
october-8 = y.count('8/Oct/1995')
october-9 = y.count('9/Oct/1995')
october-10 = y.count('10/Oct/1995')
october-11 = y.count('11/Oct/1995')

print('There Were', april-1+april-2+april-3+april-4+april-5+april-6+april-7+april-8+april-9+april-10+april-11+april-12+april-13+april-14
+april-15+april-16+april-17+april-18+april-19+april-20+may-1+june-1+july-1+august-1+september-1+october-1+
october-2+october-3+october-4+october-5+october-6+october-7+october-8+october-9+october-10+october-11,
'requests within the last 6 months')
#END OF LAB 2

#START of Question 1
x = open("Log_file_download.txt", "r")
y = x.read()
october_1 = y.count('24/Oct/1994')
print(october_1, 'Requests were made on the 24th of October in 1994')

october_2 = y.count('25/Oct/1994')
print(october_2, 'Requests were made on October 25, 1994')

october_3 = y.count('26/Oct/1994')
print(october_3, 'Requests were made on October 26, 1994')

october_4 = y.count('27/Oct/1994')
print(october_4, 'Requests were made on October 27, 1994')

october_5 = y.count('28/Oct/1994')
print(october_5, 'Requests were made on October 28, 1994')

october_6 = y.count('29/Oct/1994')
print(october_6, 'Requests were made on October 29, 1994')

october_7 = y.count('30/Oct/1994')
print(october_7, 'Requests were made on October 30, 1994')

october_8 = y.count('31/Oct/1994')
print(october_8, 'Requests were made on October 31, 1994')

november = y.count('1/Nov/1994')
print(november, 'Requests were made on November 1, 1994')

november2 = y.count('2/Nov/1994')
print(november2, 'Requests were made on November 2, 1994')

november3 = y.count('3/Nov/1994')
print(november3, 'Requests were made on November 3, 1994')

november4 = y.count('4/Nov/1994')
print(november4, 'Requests were made on November 4, 1994')

november5 = y.count('5/Nov/1994')
print(november5, 'Requests were made on November 5, 1994')

november6 = y.count('6/Nov/1994')
print(november6, 'Requests were made on November 6, 1994')

november7 = y.count('7/Nov/1994')
print(november7, 'Requests were made on November 7, 1994')

november8 = y.count('8/Nov/1994')
print(november8, 'Requests were made on November 8, 1994')

november9 = y.count('9/Nov/1994')
print(november9, 'Requests were made on November 9, 1994')

november10 = y.count('10/Nov/1994')
print(november10, 'Requests were made on November 10, 1994')

november11 = y.count('11/Nov/1994')
print(november11, 'Requests were made on November 11, 1994')

november12 = y.count('12/Nov/1994')
print(november12, 'Requests were made on November 12, 1994')

november13 = y.count('13/Nov/1994')
print(november13, 'Requests were made on November 13, 1994')

november14 = y.count('14/Nov/1994')
print(november14, 'Requests were made on November 14, 1994')

november15 = y.count('15/Nov/1994')
print(november15, 'Requests were made on November 15, 1994')

november16 = y.count('16/Nov/1994')
print(november16, 'Requests were made on November 16, 1994')

november17 = y.count('17/Nov/1994')
print(november17, 'Requests were made on November 17, 1994')

november18 = y.count('18/Nov/1994')
print(november18, 'Requests were made on November 18, 1994')

november19 = y.count('19/Nov/1994')
print(november19, 'Requests were made on November 19, 1994')

november20 = y.count('20/Nov/1994')
print(november20, 'Requests were made on November 20, 1994')

november21 = y.count('21/Nov/1994')
print(november21, 'Requests were made on November 21, 1994')

november22 = y.count('22/Nov/1994')
print(november22, 'Requests were made on November 22, 1994')

november23 = y.count('23/Nov/1994')
print(november23, 'Requests were made on November 23, 1994')

november24 = y.count('24/Nov/1994')
print(november24, 'Requests were made on November 24, 1994')

november25 = y.count('25/Nov/1994')
print(november25, 'Requests were made on November 25, 1994')

november26 = y.count('26/Nov/1994')
print(november26, 'Requests were made on November 26, 1994')

november27 = y.count('27/Nov/1994')
print(november27, 'Requests were made on November 27, 1994')

november28 = y.count('28/Nov/1994')
print(november28, 'Requests were made on November 28, 1994')

november29 = y.count('29/Nov/1994')
print(november29, 'Requests were made on November 29, 1994')

november30 = y.count('30/Nov/1994')
print(november30, 'Requests were made on November 30, 1994')

december = y.count('1/Dec/1994')
print(december, 'Requests were made on December 1, 1994')

december2 = y.count('2/Dec/1994')
print(december2, 'Requests were made on December 2, 1994')

december3 = y.count('3/Dec/1994')
print(december3, 'Requests were made on December 3, 1994')

december4 = y.count('4/Dec/1994')
print(december4, 'Requests were made on December 4, 1994')

december5 = y.count('5/Dec/1994')
print(december5, 'Requests were made on December 5, 1994')

december6 = y.count('6/Dec/1994')
print(december6, 'Requests were made on December 6, 1994')

december7 = y.count('7/Dec/1994')
print(december7, 'Requests were made on December 7, 1994')

december8 = y.count('8/Dec/1994')
print(december8, 'Requests were made on December 8, 1994')

december9 = y.count('9/Dec/1994')
print(december9, 'Requests were made on December 9, 1994')

december10 = y.count('10/Dec/1994')
print(december10, 'Requests were made on December 10, 1994')

december11 = y.count('11/Dec/1994')
print(december11, 'Requests were made on December 11, 1994')

december12 = y.count('12/Dec/1994')
print(december12, 'Requests were made on December 12, 1994')

december13 = y.count('13/Dec/1994')
print(december13, 'Requests were made on December 13, 1994')

december14 = y.count('14/Dec/1994')
print(december14, 'Requests were made on December 14, 1994')

december15 = y.count('15/Dec/1994')
print(december15, 'Requests were made on December 15, 1994')

december16 = y.count('16/Dec/1994')
print(december16, 'Requests were made on December 16, 1994')

december17 = y.count('17/Dec/1994')
print(december17, 'Requests were made on December 17, 1994')

december18 = y.count('18/Dec/1994')
print(december18, 'Requests were made on December 18, 1994')

december19 = y.count('19/Dec/1994')
print(december19, 'Requests were made on December 19, 1994')

december20 = y.count('20/Dec/1994')
print(december20, 'Requests were made on December 20, 1994')

december21 = y.count('21/Dec/1994')
print(december21, 'Requests were made on December 21, 1994')

december22 = y.count('22/Dec/1994')
print(december22, 'Requests were made on December 22, 1994')

december23 = y.count('23/Dec/1994')
print(december23, 'Requests were made on December 23, 1994')

december24 = y.count('24/Dec/1994')
print(december24, 'Requests were made on December 24, 1994')

december25 = y.count('25/Dec/1994')
print(december25, 'Requests were made on December 25, 1994')

december26 = y.count('26/Dec/1994')
print(december26, 'Requests were made on December 26, 1994')

december27 = y.count('27/Dec/1994')
print(december27, 'Requests were made on December 27, 1994')

december28 = y.count('28/Dec/1994')
print(december28, 'Requests were made on December 28, 1994')

december29 = y.count('29/Dec/1994')
print(december29, 'Requests were made on December 29, 1994')

december30 = y.count('30/Dec/1994')
print(december30, 'Requests were made on December 30, 1994')

december31 = y.count('31/Dec/1994')
print(december31, 'Requests were made on December 31, 1994')

january = y.count('1/Jan/1995')
print(january, 'Requests were made on January 1, 1995')

january2 = y.count('2/Jan/1995')
print(january2, 'Requests were made on January 2, 1995')

january3 = y.count('3/Jan/1995')
print(january3, 'Requests were made on January 3, 1995')

january4 = y.count('4/Jan/1995')
print(january4, 'Requests were made on January 4, 1995')

january5 = y.count('5/Jan/1995')
print(january5, 'Requests were made on January 5, 1995')

january6 = y.count('6/Jan/1995')
print(january6, 'Requests were made on January 6, 1995')

january7 = y.count('7/Jan/1995')
print(january7, 'Requests were made on January 7, 1995')

january8 = y.count('8/Jan/1995')
print(january8, 'Requests were made on January 8, 1995')

january9 = y.count('9/Jan/1995')
print(january9, 'Requests were made on January 9, 1995')

january10 = y.count('10/Jan/1995')
print(january10, 'Requests were made on January 10, 1995')

january11 = y.count('11/Jan/1995')
print(january11, 'Requests were made on January 11, 1995')

january12 = y.count('12/Jan/1995')
print(january12, 'Requests were made on January 12, 1995')

january13 = y.count('13/Jan/1995')
print(january13, 'Requests were made on January 13, 1995')

january14 = y.count('14/Jan/1995')
print(january14, 'Requests were made on January 14, 1995')

january15 = y.count('15/Jan/1995')
print(january15, 'Requests were made on January 15, 1995')

january16 = y.count('16/Jan/1995')
print(january16, 'Requests were made on January 16, 1995')

january17 = y.count('17/Jan/1995')
print(january17, 'Requests were made on January 17, 1995')

january18 = y.count('18/Jan/1995')
print(january18, 'Requests were made on January 18, 1995')

january19 = y.count('19/Jan/1995')
print(january19, 'Requests were made on January 19, 1995')

january20 = y.count('20/Jan/1995')
print(january20, 'Requests were made on January 20, 1995')

january21 = y.count('21/Jan/1995')
print(january21, 'Requests were made on January 21, 1995')

january22 = y.count('22/Jan/1995')
print(january22, 'Requests were made on January 22, 1995')

january23 = y.count('23/Jan/1995')
print(january23, 'Requests were made on January 23, 1995')

january24 = y.count('24/Jan/1995')
print(january24, 'Requests were made on January 24, 1995')

january25 = y.count('25/Jan/1995')
print(january25, 'Requests were made on January 25, 1995')

january26 = y.count('26/Jan/1995')
print(january26, 'Requests were made on January 26, 1995')

january27 = y.count('27/Jan/1995')
print(january27, 'Requests were made on January 27, 1995')

january28 = y.count('28/Jan/1995')
print(january28, 'Requests were made on January 28, 1995')

january29 = y.count('29/Jan/1995')
print(january29, 'Requests were made on January 29, 1995')

january30 = y.count('30/Jan/19945')
print(january30, 'Requests were made on January 30, 1995')

january31 = y.count('31/Jan/1995')
print(january31, 'Requests were made on January 31, 1995')

feb = y.count('1/Feb/1995')
print(feb, 'Requests were made on February 1, 1995')

feb2 = y.count('2/Feb/1995')
print(feb2, 'Requests were made on February 2, 1995')

feb3 = y.count('3/Feb/1995')
print(feb3, 'Requests were made on February 3, 1995')

feb4 = y.count('4/Feb/1995')
print(feb4, 'Requests were made on February 4, 1995')

feb5 = y.count('5/Feb/1995')
print(feb5, 'Requests were made on February 5, 1995')

feb6 = y.count('6/Feb/1995')
print(feb6, 'Requests were made on February 6, 1995')

feb7 = y.count('7/Feb/1995')
print(feb7, 'Requests were made on February 7, 1995')

feb8 = y.count('8/Feb/1995')
print(feb8, 'Requests were made on February 8, 1995')

feb9 = y.count('9/Feb/1995')
print(feb9, 'Requests were made on February 9, 1995')

feb10 = y.count('10/Feb/1995')
print(feb10, 'Requests were made on February 10, 1995')

feb11 = y.count('11/Feb/1995')
print(feb11, 'Requests were made on February 11, 1995')

feb12 = y.count('12/Feb/1995')
print(feb12, 'Requests were made on February 12, 1995')

feb13 = y.count('13/Feb/1995')
print(feb13, 'Requests were made on February 13, 1995')

feb14 = y.count('14/Feb/1995')
print(feb14, 'Requests were made on February 14, 1995')

feb15 = y.count('15/Feb/1995')
print(feb15, 'Requests were made on February 15, 1995')

feb16 = y.count('16/Feb/1995')
print(feb16, 'Requests were made on February 16, 1995')

feb17 = y.count('17/Feb/1995')
print(feb17, 'Requests were made on February 17, 1995')

feb18 = y.count('18/Feb/1995')
print(feb18, 'Requests were made on February 18, 1995')

feb19 = y.count('19/Feb/1995')
print(feb19, 'Requests were made on February 19, 1995')

feb20 = y.count('20/Feb/1995')
print(feb20, 'Requests were made on February 20, 1995')

feb21 = y.count('21/Feb/1995')
print(feb21, 'Requests were made on February 21, 1995')

feb22 = y.count('22/Feb/1995')
print(feb22, 'Requests were made on February 22, 1995')

feb23 = y.count('23/Feb/1995')
print(feb23, 'Requests were made on February 23, 1995')

feb24 = y.count('24/Feb/1995')
print(feb24, 'Requests were made on February 24, 1995')

feb25 = y.count('25/Feb/1995')
print(feb25, 'Requests were made on February 25, 1995')

feb26 = y.count('26/Feb/1995')
print(feb26, 'Requests were made on February 26, 1995')

feb27 = y.count('27/Feb/1995')
print(feb27, 'Requests were made on February 27, 1995')

feb28 = y.count('28/Feb/1995')
print(feb28, 'Requests were made on February 28, 1995')

march = y.count('1/Mar/1995')
print(march, 'Requests were made on March 1, 1995')

march2 = y.count('2/Mar/1995')
print(march2, 'Requests were made on March 2, 1995')

march3 = y.count('3/Mar/1995')
print(march3, 'Requests were made on March 3, 1995')

march4 = y.count('4/Mar/1995')
print(march4, 'Requests were made on March 4, 1995')

march5 = y.count('5/Mar/1995')
print(march5, 'Requests were made on March 5, 1995')

march6 = y.count('6/Mar/1995')
print(march6, 'Requests were made on March 6, 1995')

march7 = y.count('7/Mar/1995')
print(march7, 'Requests were made on March 7, 1995')

march8 = y.count('8/Mar/1995')
print(march8, 'Requests were made on March 8, 1995')

march9 = y.count('9/Mar/1995')
print(march9, 'Requests were made on March 9, 1995')

march10 = y.count('10/Mar/1995')
print(march10, 'Requests were made on March 10, 1995')

march11 = y.count('11/Mar/1995')
print(march11, 'Requests were made on March 11, 1995')

march12 = y.count('12/Mar/1995')
print(march12, 'Requests were made on March 12, 1995')

march13 = y.count('13/Mar/1995')
print(march13, 'Requests were made on March 13, 1995')

march14 = y.count('14/Mar/1995')
print(march14, 'Requests were made on March 14, 1995')

march15 = y.count('15/Mar/1995')
print(march15, 'Requests were made on March 15, 1995')

march16 = y.count('16/Mar/1995')
print(march16, 'Requests were made on March 16, 1995')

march17 = y.count('17/Mar/1995')
print(march17, 'Requests were made on March 17, 1995')

march18 = y.count('18/Mar/1995')
print(march18, 'Requests were made on March 18, 1995')

march19 = y.count('19/Mar/1995')
print(march19, 'Requests were made on March 19, 1995')

march20 = y.count('20/Mar/1995')
print(march20, 'Requests were made on March 20, 1995')

march21 = y.count('21/Mar/1995')
print(march21, 'Requests were made on March 21, 1995')

march22 = y.count('22/Mar/1995')
print(march22, 'Requests were made on March 22, 1995')

march23 = y.count('23/Mar/1995')
print(march23, 'Requests were made on March 23, 1995')

march24 = y.count('24/Mar/1995')
print(march24, 'Requests were made on March 24, 1995')

march25 = y.count('25/Mar/1995')
print(march25, 'Requests were made on March 25, 1995')

march26 = y.count('26/Mar/1995')
print(march26, 'Requests were made on March 26, 1995')

march27 = y.count('27/Mar/1995')
print(march27, 'Requests were made on March 27, 1995')

march28 = y.count('28/Mar/1995')
print(march28, 'Requests were made on March 28, 1995')

march29 = y.count('29/Mar/1995')
print(march29, 'Requests were made on March 29, 1995')

march30 = y.count('30/Mar/1995')
print(march30, 'Requests were made on March 30, 1995')

march31 = y.count('31/Mar/1995')
print(march31, 'Requests were made on March 31, 1995')

april1 = y.count('1/Apr/1995')
print(april, 'Requests were made on April 1, 1995')

april2 = y.count('2/Apr/1995')
print(april2, 'Requests were made on April 2, 1995')

april3 = y.count('3/Apr/1995')
print(april3, 'Requests were made on April 3, 1995')

april4 = y.count('4/Apr/1995')
print(april4, 'Requests were made on April 4, 1995')

april5 = y.count('5/Apr/1995')
print(april5, 'Requests were made on April 5, 1995')

april6 = y.count('6/Apr/1995')
print(april6, 'Requests were made on April 6, 1995')

april7 = y.count('7/Apr/1995')
print(april7, 'Requests were made on April 7, 1995')

april8 = y.count('8/Apr/1995')
print(april8, 'Requests were made on April 8, 1995')

april9 = y.count('9/Apr/1995')
print(april9, 'Requests were made on April 9, 1995')

april10 = y.count('10/Apr/1995')
print(april10, 'Requests were made on April 10, 1995')

april11 = y.count('11/Apr/1995')
print(april11, 'Requests were made on April 11, 1995')

april12 = y.count('12/Apr/1995')
print(april12, 'Requests were made on April 12, 1995')

april13 = y.count('13/Apr/1995')
print(april13, 'Requests were made on April 13, 1995')

april14 = y.count('14/Apr/1995')
print(april14, 'Requests were made on April 14, 1995')

april15 = y.count('15/Apr/1995')
print(april15, 'Requests were made on April 15,1995')

april16 = y.count('16/Apr/1995')
print(april16, 'Requests were made on April 16,1995')

april17 = y.count('17/Apr/1995')
print(april17, 'Requests were made on April 17,1995')

april18 = y.count('18/Apr/1995')
print(april18, 'Requests were made on April 18,1995')

april19 = y.count('19/Apr/1995')
print(april19, 'Requests were made on April 19,1995')

april20 = y.count('20/Apr/1995')
print(april20, 'Requests were made on April 20,1995')

april21 = y.count('21/Apr/1995')
print(april21, 'Requests were made on April 21,1995')

april22 = y.count('22/Apr/1995')
print(april22, 'Requests were made on April 22,1995')

april23 = y.count('23/Apr/1995')
print(april23, 'Requests were made on April 23,1995')

april24 = y.count('24/Apr/1995')
print(april24, 'Requests were made on April 24,1995')

april25 = y.count('25/Apr/1995')
print(april25, 'Requests were made on April 25,1995')

april26 = y.count('26/Apr/1995')
print(april26, 'Requests were made on April 26,1995')

april27 = y.count('27/Apr/1995')
print(april27, 'Requests were made on April 27,1995')

april28 = y.count('28/Apr/1995')
print(april28, 'Requests were made on April 28,1995')

april29 = y.count('29/Apr/1995')
print(april29, 'Requests were made on April 29,1995')

april30 = y.count('30/Apr/1995')
print(april30, 'Requests were made on April 30,1995')

may = y.count('1/May/1995')
print(may, 'Requests were made in May 1, 1995')

may2 = y.count('2/May/1995')
print(may2, 'Requests were made in May 2, 1995')

may3 = y.count('3/May/1995')
print(may3, 'Requests were made in May 3, 1995')

may4 = y.count('4/May/1995')
print(may4, 'Requests were made in May 4, 1995')

may5 = y.count('5/May/1995')
print(may5, 'Requests were made in May 5, 1995')

may6 = y.count('6/May/1995')
print(may6, 'Requests were made in May 6, 1995')

may7 = y.count('7/May/1995')
print(may7, 'Requests were made in May 7, 1995')

may8 = y.count('8/May/1995')
print(may8, 'Requests were made in May 8, 1995')

may9 = y.count('9/May/1995')
print(may9, 'Requests were made in May 9, 1995')

may10 = y.count('10/May/1995')
print(may10, 'Requests were made in May 10, 1995')

may11 = y.count('11/May/1995')
print(may11, 'Requests were made in May 11, 1995')

may12 = y.count('12/May/1995')
print(may12, 'Requests were made in May 12, 1995')

may13 = y.count('13/May/1995')
print(may13, 'Requests were made in May 13, 1995')

may14 = y.count('14/May/1995')
print(may14, 'Requests were made in May 14, 1995')

may15 = y.count('15/May/1995')
print(may15, 'Requests were made in May 15, 1995')

may16 = y.count('16/May/1995')
print(may16, 'Requests were made in May 16, 1995')

may17 = y.count('17/May/1995')
print(may17, 'Requests were made in May 17, 1995')

may18 = y.count('18/May/1995')
print(may18, 'Requests were made in May 18, 1995')

may19 = y.count('19/May/1995')
print(may19, 'Requests were made in May 19, 1995')

may20 = y.count('20/May/1995')
print(may20, 'Requests were made in May 20, 1995')

may21 = y.count('21/May/1995')
print(may21, 'Requests were made in May 21, 1995')

may22 = y.count('22/May/1995')
print(may22, 'Requests were made in May 22, 1995')

may23 = y.count('23/May/1995')
print(may23, 'Requests were made in May 23, 1995')

may24 = y.count('24/May/1995')
print(may24, 'Requests were made in May 24, 1995')

may25 = y.count('25/May/1995')
print(may25, 'Requests were made in May 25, 1995')

may26 = y.count('26/May/1995')
print(may26, 'Requests were made in May 26, 1995')

may27 = y.count('27/May/1995')
print(may27, 'Requests were made in May 27, 1995')

may28 = y.count('28/May/1995')
print(may28, 'Requests were made in May 28, 1995')

may29 = y.count('29/May/1995')
print(may29, 'Requests were made in May 29, 1995')

may30 = y.count('30/May/1995')
print(may30, 'Requests were made in May 30, 1995')

may31 = y.count('31/May/1995')
print(may31, 'Requests were made in May 31, 1995')

june = y.count('1/Jun/1995')
print(june, 'Requests were made in June 1, 1995')

june2 = y.count('2/Jun/1995')
print(june2, 'Requests were made in June 2, 1995')

june3 = y.count('3/Jun/1995')
print(june3, 'Requests were made in June 3, 1995')

june4 = y.count('4/Jun/1995')
print(june4, 'Requests were made in June 4, 1995')

june5 = y.count('5/Jun/1995')
print(june5, 'Requests were made in June 5, 1995')

june6 = y.count('6/Jun/1995')
print(june6, 'Requests were made in June 6, 1995')

june7 = y.count('7/Jun/1995')
print(june7, 'Requests were made in June 7, 1995')

june8 = y.count('8/Jun/1995')
print(june8, 'Requests were made in June 8, 1995')

june9 = y.count('9/Jun/1995')
print(june9, 'Requests were made in June 9, 1995')

june10 = y.count('10/Jun/1995')
print(june10, 'Requests were made in June 10, 1995')

june11 = y.count('11/Jun/1995')
print(june11, 'Requests were made in June 11, 1995')

june12 = y.count('12/Jun/1995')
print(june12, 'Requests were made in June 12, 1995')

june13 = y.count('13/Jun/1995')
print(june13, 'Requests were made in June 13, 1995')

june14 = y.count('14/Jun/1995')
print(june14, 'Requests were made in June 14, 1995')

june15 = y.count('15/Jun/1995')
print(june15, 'Requests were made in June 15, 1995')

june16 = y.count('16/Jun/1995')
print(june16, 'Requests were made in June 16, 1995')

june17 = y.count('17/Jun/1995')
print(june17, 'Requests were made in June 17, 1995')

june18 = y.count('18/Jun/1995')
print(june18, 'Requests were made in June 18, 1995')

june19 = y.count('19/Jun/1995')
print(june19, 'Requests were made in June 19, 1995')

june20 = y.count('20/Jun/1995')
print(june20, 'Requests were made in June 20, 1995')

june21 = y.count('21/Jun/1995')
print(june21, 'Requests were made in June 21, 1995')

june22 = y.count('22/Jun/1995')
print(june22, 'Requests were made in June 22, 1995')

june23 = y.count('23/Jun/1995')
print(june23, 'Requests were made in June 23, 1995')

june24 = y.count('24/Jun/1995')
print(june24, 'Requests were made in June 24, 1995')

june25 = y.count('25/Jun/1995')
print(june25, 'Requests were made in June 25, 1995')

june26 = y.count('26/Jun/1995')
print(june26, 'Requests were made in June 26, 1995')

june27 = y.count('27/Jun/1995')
print(june27, 'Requests were made in June 27, 1995')

june28 = y.count('28/Jun/1995')
print(june28, 'Requests were made in June 28, 1995')

june29 = y.count('29/Jun/1995')
print(june29, 'Requests were made in June 29, 1995')

june30 = y.count('30/Jun/1995')
print(june30, 'Requests were made in June 30, 1995')

july = y.count('Jul/1995')
print(july, 'Requests were made in July 1, 1995')

july = y.count('1/Jul/1995')
print(july, 'Requests were made in July 1, 1995')

july2 = y.count('2/Jul/1995')
print(july2, 'Requests were made in July 2, 1995')

july3 = y.count('3/Jul/1995')
print(july3, 'Requests were made in July 3, 1995')

july4 = y.count('4/Jul/1995')
print(july4, 'Requests were made in July 4, 1995')

july5 = y.count('5/Jul/1995')
print(july5, 'Requests were made in July 5, 1995')

july6 = y.count('6/Jul/1995')
print(july6, 'Requests were made in July 6, 1995')

july7 = y.count('7/Jul/1995')
print(july7, 'Requests were made in July 7, 1995')

july8 = y.count('8/Jul/1995')
print(july8, 'Requests were made in July 8, 1995')

july9 = y.count('9/Jul/1995')
print(july9, 'Requests were made in July 9, 1995')

july10 = y.count('10/Jul/1995')
print(july10, 'Requests were made in July 10, 1995')

july11 = y.count('11/Jul/1995')
print(july11, 'Requests were made in July 11, 1995')

july12 = y.count('12/Jul/1995')
print(july12, 'Requests were made in July 12, 1995')

july13 = y.count('13/Jul/1995')
print(july13, 'Requests were made in July 13, 1995')

july14 = y.count('14/Jul/1995')
print(july14, 'Requests were made in July 14, 1995')

july15 = y.count('15/Jul/1995')
print(july15, 'Requests were made in July 15, 1995')

july16 = y.count('16/Jul/1995')
print(july16, 'Requests were made in July 16, 1995')

july17 = y.count('17/Jul/1995')
print(july17, 'Requests were made in July 17, 1995')

july18 = y.count('18/Jul/1995')
print(july18, 'Requests were made in July 18, 1995')

july19 = y.count('19/Jul/1995')
print(july19, 'Requests were made in July 19, 1995')

july20 = y.count('20/Jul/1995')
print(july20, 'Requests were made in July 20, 1995')

july21 = y.count('21/Jul/1995')
print(july21, 'Requests were made in July 21, 1995')

july22 = y.count('22/Jul/1995')
print(july22, 'Requests were made in July 22, 1995')

july23 = y.count('23/Jul/1995')
print(july23, 'Requests were made in July 23, 1995')

july24 = y.count('24/Jul/1995')
print(july24, 'Requests were made in July 24, 1995')

july25 = y.count('25/Jul/1995')
print(july25, 'Requests were made in July 25, 1995')

july26 = y.count('26/Jul/1995')
print(july26, 'Requests were made in July 26, 1995')

july27 = y.count('27/Jul/1995')
print(july27, 'Requests were made in July 27, 1995')

july28 = y.count('28/Jul/1995')
print(july28, 'Requests were made in July 28, 1995')

july29 = y.count('29/Jul/1995')
print(july29, 'Requests were made in July 29, 1995')

july30 = y.count('30/Jul/1995')
print(july30, 'Requests were made in July 30, 1995')

july31 = y.count('31/Jul/1995')
print(july31, 'Requests were made in July 31, 1995')

august = y.count('1/Aug/1995')
print(august, 'Requests were made in August 1, 1995')

august2 = y.count('2/Aug/1995')
print(august2, 'Requests were made in August 2, 1995')

august3 = y.count('3/Aug/1995')
print(august3, 'Requests were made in August 3, 1995')

august4 = y.count('4/Aug/1995')
print(august4, 'Requests were made in August 4, 1995')

august5 = y.count('5/Aug/1995')
print(august5, 'Requests were made in August 5, 1995')

august6 = y.count('6/Aug/1995')
print(august6, 'Requests were made in August 6, 1995')

august7 = y.count('7/Aug/1995')
print(august7, 'Requests were made in August 7, 1995')

august8 = y.count('8/Aug/1995')
print(august8, 'Requests were made in August 8, 1995')

august9 = y.count('9/Aug/1995')
print(august9, 'Requests were made in August 9, 1995')

august10 = y.count('10/Aug/1995')
print(august10, 'Requests were made in August 10, 1995')

august11 = y.count('11/Aug/1995')
print(august11, 'Requests were made in August 11, 1995')

august12 = y.count('12/Aug/1995')
print(august12, 'Requests were made in August 12, 1995')

august13 = y.count('13/Aug/1995')
print(august13, 'Requests were made in August 13, 1995')

august14 = y.count('14/Aug/1995')
print(august14, 'Requests were made in August 14, 1995')

august15 = y.count('15/Aug/1995')
print(august15, 'Requests were made in August 15, 1995')

august16 = y.count('16/Aug/1995')
print(august16, 'Requests were made in August 16, 1995')

august17 = y.count('17/Aug/1995')
print(august17, 'Requests were made in August 17, 1995')

august18 = y.count('18/Aug/1995')
print(august18, 'Requests were made in August 18, 1995')

august19 = y.count('19/Aug/1995')
print(august19, 'Requests were made in August 19, 1995')

august20 = y.count('20/Aug/1995')
print(august20, 'Requests were made in August 20, 1995')

august21 = y.count('21/Aug/1995')
print(august21, 'Requests were made in August 21, 1995')

august22 = y.count('22/Aug/1995')
print(august22, 'Requests were made in August 22, 1995')

august23 = y.count('23/Aug/1995')
print(august23, 'Requests were made in August 23, 1995')

august24 = y.count('24/Aug/1995')
print(august24, 'Requests were made in August 24, 1995')

august25 = y.count('25/Aug/1995')
print(august25, 'Requests were made in August 25, 1995')

august26 = y.count('26/Aug/1995')
print(august26, 'Requests were made in August 26, 1995')

august27 = y.count('27/Aug/1995')
print(august27, 'Requests were made in August 27, 1995')

august28 = y.count('28/Aug/1995')
print(august28, 'Requests were made in August 28, 1995')

august29 = y.count('29/Aug/1995')
print(august29, 'Requests were made in August 29, 1995')

august30 = y.count('30/Aug/1995')
print(august30, 'Requests were made in August 30, 1995')

august31 = y.count('31/Aug/1995')
print(august31, 'Requests were made in August 31, 1995')

september = y.count('1/Sep/1995')
print(september, 'Requests were made in September 1, 1995')

september2 = y.count('2/Sep/1995')
print(september2, 'Requests were made in September 2, 1995')

september3 = y.count('3/Sep/1995')
print(september3, 'Requests were made in September 3, 1995')

september4 = y.count('4/Sep/1995')
print(september4, 'Requests were made in September 4, 1995')

september5 = y.count('5/Sep/1995')
print(september5, 'Requests were made in September 5, 1995')

september6 = y.count('6/Sep/1995')
print(september6, 'Requests were made in September 6, 1995')

september7 = y.count('7/Sep/1995')
print(september7, 'Requests were made in September 7, 1995')

september8 = y.count('8/Sep/1995')
print(september8, 'Requests were made in September 8, 1995')

september9 = y.count('9/Sep/1995')
print(september9, 'Requests were made in September 9, 1995')

september10 = y.count('10/Sep/1995')
print(september10, 'Requests were made in September 10, 1995')

september11 = y.count('11/Sep/1995')
print(september11, 'Requests were made in September 11, 1995')

september12 = y.count('12/Sep/1995')
print(september12, 'Requests were made in September 12, 1995')

september13 = y.count('13/Sep/1995')
print(september13, 'Requests were made in September 13, 1995')

september14 = y.count('14/Sep/1995')
print(september14, 'Requests were made in September 14, 1995')

september15 = y.count('15/Sep/1995')
print(september15, 'Requests were made in September 15, 1995')

september16 = y.count('16/Sep/1995')
print(september16, 'Requests were made in September 16, 1995')

september17 = y.count('17/Sep/1995')
print(september17, 'Requests were made in September 17, 1995')

september18 = y.count('18/Sep/1995')
print(september18, 'Requests were made in September 18, 1995')

september19 = y.count('19/Sep/1995')
print(september19, 'Requests were made in September 19, 1995')

september20 = y.count('20/Sep/1995')
print(september20, 'Requests were made in September 20, 1995')

september21 = y.count('21/Sep/1995')
print(september21, 'Requests were made in September 21, 1995')

september22 = y.count('22/Sep/1995')
print(september22, 'Requests were made in September 22, 1995')

september23 = y.count('23/Sep/1995')
print(september23, 'Requests were made in September 23, 1995')

september24 = y.count('24/Sep/1995')
print(september24, 'Requests were made in September 24, 1995')

september25 = y.count('25/Sep/1995')
print(september25, 'Requests were made in September 25, 1995')

september26 = y.count('26/Sep/1995')
print(september26, 'Requests were made in September 26, 1995')

september27 = y.count('27/Sep/1995')
print(september27, 'Requests were made in September 27, 1995')

september28 = y.count('28/Sep/1995')
print(september28, 'Requests were made in September 28, 1995')

september29 = y.count('29/Sep/1995')
print(september29, 'Requests were made in September 29, 1995')

september30 = y.count('30/Sep/1995')
print(september30, 'Requests were made in September 30, 1995')

october = y.count('1/Oct/1995')
print(october, 'Requests were made in October 1, 1995')

october2 = y.count('2/Oct/1995')
print(october2, 'Requests were made in October 2, 1995')

october3 = y.count('3/Oct/1995')
print(october3, 'Requests were made in October 3, 1995')

october4 = y.count('4/Oct/1995')
print(october4, 'Requests were made in October 4, 1995')

october5 = y.count('5/Oct/1995')
print(october5, 'Requests were made in October 5, 1995')

october6 = y.count('6/Oct/1995')
print(october6, 'Requests were made in October 6, 1995')

october7 = y.count('7/Oct/1995')
print(october7, 'Requests were made in October 7, 1995')

october8 = y.count('8/Oct/1995')
print(october8, 'Requests were made in October 8, 1995')

october9 = y.count('9/Oct/1995')
print(october9, 'Requests were made in October 9, 1995')

october10 = y.count('10/Oct/1995')
print(october10, 'Requests were made in October 10, 1995')

october11 = y.count('11/Oct/1995')
print(october11, 'Requests were made in October 11, 1995')

#END of question/part 1

# Start Question part 3 and 4 (4xx,3xx status codes)
textfile = open('Log_file_download.txt', 'r')
filetext = textfile.read()
textfile.close()
matches = re.findall("\" 4\d\d", filetext)
matches2 = re.findall("\" 3\d\d", filetext)
list = (len(matches)/total_log)
list2 = (len(matches2)/total_log)
rounded_x = format(list, '.3f')
rounded_y = format(list2, '.3f')
print("The percentage of 4xx errors is", rounded_x, '%')
print("The percentage of 3xx errors is", rounded_y, '%')
# End Question part 3 and 4 (4xx,3xx status codes)
