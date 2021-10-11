import collections

logfile = open("file.log", "r")

clean_log=[]

for line in logfile:
    try:
        
        clean_log.append(line[line.index("GET")+4:line.index("HTTP")])
    except:
        pass

counter = collections.Counter(clean_log)

print("Most Common File Request:")
# get the Top 50 most popular URLs
for count in counter.most_common(3):
    print(str(count[1]) + "	" + str(count[0]))

print("Least Common File Request:")
for count in counter.most_common() [-3:]:
    print(str(count[1]) + "	" + str(count[0]))



logfile.close()