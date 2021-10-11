from urllib import request
import re
remote_url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local_file = 'Log_file_download.txt'
request.urlretrieve(remote_url, local_file)

textfile = open('Log_file_download.txt', 'r')
filetext = textfile.read()
textfile.close()

#get file object reference to the file
file = open ('Log_file_download.txt', 'r')
#read content of file to string
data = file.read ()
#get number of occurances of the substring in the string
occurences = data.count(".jpeg")

print('Number of occurrences of the word jpeg: ', occurences)

#get file object reference to the file
file = open ('Log_file_download.txt', 'r')
#read content of file to string
data = file.read ()
#get number of occurances of the substring in the string
occurences = data.count(".html")

print('Number of occurences of the word html:', occurences)

#get file object reference to the file
file = open ('Log_file_download.txt', 'r')
#read content of file to string
data = file.read ()
#get number of occurances of the substring in the string
occurences = data.count(".rgb")

print('Number of occurences of the word rgb:', occurences)

#get file object reference to the file
file = open ('Log_file_download.txt', 'r')
#read content of file to string
data = file.read ()
#get number of occurances of the substring in the string
occurences = data.count(".gif")

print('Number of occurences of the word gif:', occurences)

#get file object reference to the file
file = open ('Log_file_download.txt', 'r')
#read content of file to string
data = file.read ()
#get number of occurances of the substring in the string
occurences = data.count(".xbm")

print('Number of occurences of the word xbm:', occurences)

#get file object reference to the file
file = open ('Log_file_download.txt', 'r')
#read content of file to string
data = file.read ()
#get number of occurances of the substring in the string
occurences = data.count(".qt")

print('Number of occurences of the word qt:', occurences)

#get file object reference to the file
file = open ('Log_file_download.txt', 'r')
#read content of file to string
data = file.read ()
#get number of occurances of the substring in the string
occurences = data.count(".ps")

print('Number of occurences of the word ps:', occurences)

#get file object reference to the file
file = open ('Log_file_download.txt', 'r')
#read content of file to string
data = file.read ()
#get number of occurances of the substring in the string
occurences = data.count(".louise")

print('Number of occurences of the word louise:', occurences)

#get file object reference to the file
file = open ('Log_file_download.txt', 'r')
#read content of file to string
data = file.read ()
#get number of occurances of the substring in the string
occurences = data.count(".mpg")

print('Number of occurences of the word mpg:', occurences)

#get file object reference to the file
file = open ('Log_file_download.txt', 'r')
#read content of file to string
data = file.read ()
#get number of occurances of the substring in the string
occurences = data.count(".shar")

print('Number of occurences of the word shar:', occurences)

#get file object reference to the file
file = open ('Log_file_download.txt', 'r')
#read content of file to string
data = file.read ()
#get number of occurances of the substring in the string
occurences = data.count(".map")

print('Number of occurences of the word map:', occurences)

#get file object reference to the file
file = open ('Log_file_download.txt', 'r')
#read content of file to string
data = file.read ()
#get number of occurances of the substring in the string
occurences = data.count(".txt")

print('Number of occurences of the word txt:', occurences)

#get file object reference to the file
file = open ('Log_file_download.txt', 'r')
#read content of file to string
data = file.read ()
#get number of occurances of the substring in the string
occurences = data.count(".jpg")

print('Number of occurences of the word jpg:', occurences)

#get file object reference to the file
file = open ('Log_file_download.txt', 'r')
#read content of file to string
data = file.read ()
#get number of occurances of the substring in the string
occurences = data.count(".www")

print('Number of occurences of the word www:', occurences)

#get file object reference to the file
file = open ('Log_file_download.txt', 'r')
#read content of file to string
data = file.read ()
#get number of occurances of the substring in the string
occurences = data.count(".edu")

print('Number of occurences of the word edu:', occurences)

#get file object reference to the file
file = open ('Log_file_download.txt', 'r')
#read content of file to string
data = file.read ()
#get number of occurances of the substring in the string
occurences = data.count(".exe")

print('Number of occurences of the word exe:', occurences)

#get file object reference to the file
file = open ('Log_file_download.txt', 'r')
#read content of file to string
data = file.read ()
#get number of occurances of the substring in the string
occurences = data.count(".eps")

print('Number of occurences of the word eps:', occurences)

#get file object reference to the file
file = open ('Log_file_download.txt', 'r')
#read content of file to string
data = file.read ()
#get number of occurances of the substring in the string
occurences = data.count(".pdf")

print('Number of occurences of the word pdf:', occurences)

#get file object reference to the file
file = open ('Log_file_download.txt', 'r')
#read content of file to string
data = file.read ()
#get number of occurances of the substring in the string
occurences = data.count(".example")

print('Number of occurences of the word example:', occurences)

#get file object reference to the file
file = open ('Log_file_download.txt', 'r')
#read content of file to string
data = file.read ()
#get number of occurances of the substring in the string
occurences = data.count(".exams")

print('Number of occurences of the word exams:', occurences)

#get file object reference to the file
file = open ('Log_file_download.txt', 'r')
#read content of file to string
data = file.read ()
#get number of occurances of the substring in the string
occurences = data.count(".el")

print('Number of occurences of the word el:', occurences)

#get file object reference to the file
file = open ('Log_file_download.txt', 'r')
#read content of file to string
data = file.read ()
#get number of occurances of the substring in the string
occurences = data.count(".ef")

print('Number of occurences of the word ef:', occurences)

print('.html is the file displayed the most times')
print('.ef is the file displayed the least amount of times')
