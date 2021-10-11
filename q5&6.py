from urllib import request
import re
remote_url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local_file = 'Log_file_download.txt'
request.urlretrieve(remote_url, local_file)

textfile = open('Log_file_download.txt', 'r')
filetext = textfile.read()
textfile.close()


file = open ('Log_file_download.txt', 'r')
data = file.read ()
occurences = data.count(".jpeg")
print('Number of .jpeg files: ', occurences)

file = open ('Log_file_download.txt', 'r')
data = file.read ()
occurences = data.count(".html")
print('Number of .html files:', occurences)

file = open ('Log_file_download.txt', 'r')
data = file.read ()
occurences = data.count(".rgb")
print('Number of .rgb files:', occurences)

file = open ('Log_file_download.txt', 'r')
data = file.read ()
occurences = data.count(".gif")
print('Number of .gif files:', occurences)

file = open ('Log_file_download.txt', 'r')
data = file.read ()
occurences = data.count(".xbm")
print('Number of .xbm files:', occurences)

file = open ('Log_file_download.txt', 'r')
data = file.read ()
occurences = data.count(".qt")
print('Number of .qt files:', occurences)

file = open ('Log_file_download.txt', 'r')
data = file.read ()
occurences = data.count(".ps")
print('Number of .ps files:', occurences)

file = open ('Log_file_download.txt', 'r')
data = file.read ()
occurences = data.count(".louise")
print('Number of .louise files:', occurences)

file = open ('Log_file_download.txt', 'r')
data = file.read ()
occurences = data.count(".mpg")
print('Number of .mpg files:', occurences)

file = open ('Log_file_download.txt', 'r')
data = file.read ()
occurences = data.count(".shar")
print('Number of .shar files:', occurences)

file = open ('Log_file_download.txt', 'r')
data = file.read ()
occurences = data.count(".map")
print('Number of .map files:', occurences)

file = open ('Log_file_download.txt', 'r')
data = file.read ()
occurences = data.count(".txt")
print('Number of .txt files:', occurences)

file = open ('Log_file_download.txt', 'r')
data = file.read ()
occurences = data.count(".jpg")
print('Number of .jpg files:', occurences)

file = open ('Log_file_download.txt', 'r')
data = file.read ()
occurences = data.count(".www")
print('Number of .www files:', occurences)

file = open ('Log_file_download.txt', 'r')
data = file.read ()
occurences = data.count(".edu")
print('Number of .edu files:', occurences)

file = open ('Log_file_download.txt', 'r')
data = file.read ()
occurences = data.count(".exe")
print('Number of .exe files:', occurences)

file = open ('Log_file_download.txt', 'r')
data = file.read ()
occurences = data.count(".eps")
print('Number of .eps files:', occurences)

file = open ('Log_file_download.txt', 'r')
data = file.read ()
occurences = data.count(".pdf")
print('Number of .pdf files:', occurences)

file = open ('Log_file_download.txt', 'r')
data = file.read ()
occurences = data.count(".example")
print('Number of .example files:', occurences)

file = open ('Log_file_download.txt', 'r')
data = file.read ()
occurences = data.count(".exams")
print('Number of .exams files:', occurences)

file = open ('Log_file_download.txt', 'r')
data = file.read ()
occurences = data.count(".el")
print('Number of .el files:', occurences)

file = open ('Log_file_download.txt', 'r')
data = file.read ()
occurences = data.count(".ef")
print('Number of .ef files:', occurences)

print('')
print('')
print('The most requested file type was .html')
print('The least requested file type was .ef')
