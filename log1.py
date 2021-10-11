import re
#open https log file
file = open('file.log','r')

lines = file.readlines()
count=0 #set count to 0
for line in lines:
    count=count+1
    print(count)
