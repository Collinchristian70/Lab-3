
import collections

logfile = open("file.log", "r")

clean_log=[]

for line in logfile:
    try:
        
        clean_log.append(line[line.index("GET")+4:line.index("HTTP")])
    except:
        pass

counter = collections.Counter(clean_log)

# get the Top 50 most popular URLs
for count in counter.most_common(100000):
    print(str(count[1]) + "	" + str(count[0]))


logfile.close()