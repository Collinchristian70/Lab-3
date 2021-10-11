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
print(april127, 'Requests were made on April 27,1995')

april28 = y.count('28/Apr/1995')
print(april28, 'Requests were made on April 28,1995')

april29 = y.count('29/Apr/1995')
print(april29, 'Requests were made on April 29,1995')

april30 = y.count('30/Apr/1995')
print(april30, 'Requests were made on April 30,1995')

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
