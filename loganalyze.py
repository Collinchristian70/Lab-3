import re
#open https log file
f = open('file.log','r')

lines = f.readlines()
count=0 #set count to 0
for line in lines:
    count=count+1

print('logs in file:')
print(count)