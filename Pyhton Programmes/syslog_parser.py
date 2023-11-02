#!/usr/bon/env python3
import csv
import operator
import re
error_count = {}
per_user = {}
with open("/home/student-03-cbab6cc98775/syslog.log") as file:
    for line in file:
        info_match = re.search(r'ticky: INFO (.*) \[#.*\] \((.*)\)', line)
        error_match = re.search(r'ticky: ERROR (.*) \((.*)\)', line)
        
        if error_match:
            if not error_match[1] in error_count:
                error_count[error_match[1]] = 1
            else:
                error_count[error_match[1]]+=1
            if not error_match[2] in per_user:
                per_user[error_match[2]] = [0,1]
            else:
                per_user[error_match[2]][1]+=1
        if info_match:
            if not info_match[2] in per_user:
                per_user[info_match[2]] = [1,0]
            else:
                per_user[info_match[2]][0] += 1
sorted_error = sorted(error_count.items(), key=operator.itemgetter(1), reverse = True)
sorted_error.insert(0, ("Error", "Count"))
sorted_per_user  = dict(sorted(per_user.items(), key=operator.itemgetter(0)))
with open("error_message.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sorted_error)
with open("user_statistics.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Username", "INFO", "ERROR"])
    for key, values in sorted_per_user.items():
        writer.writerow([key, values[0], values[1]])