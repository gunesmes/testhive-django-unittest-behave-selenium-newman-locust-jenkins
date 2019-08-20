import re
import sys
import os

MIN_RESPONSE_TIME = int(os.environ['min_response_time'])
MAX_RESPONSE_TIME = int(os.environ['max_response_time'])
AVG_RESPONSE_TIME = int(os.environ['avg_response_time'])

print("\n---- Test Parameters -----\n")
print("MIN_RESPONSE_TIME: %d" % MIN_RESPONSE_TIME)
print("MAX_RESPONSE_TIME: %d" % MAX_RESPONSE_TIME)
print("AVG_RESPONSE_TIME: %d" % AVG_RESPONSE_TIME)
print("\n\n---- Test Result ----\n")

f = open("load_test_result_requests.csv", "r")
lines = f.readlines()
stats = []
for l in lines:
    match = re.search('\"(GET|POST)\",\"\/.*\"((,\d*){6})', l)
    try:
        stats.append(match.group(2)[1:].split(","))
    except:
        pass

(num_requests, num_failures, med_response_time, avg_response_time, min_response_time, max_response_time) = (list(x) for x in zip(*stats))
total_num_requests = sum(map(int, num_requests))

[total_num_requests, total_num_failures, total_med_response_time, total_avg_response_time, total_min_response_time, total_max_response_time] = lines[-1].split(",")[2:8]

fw = open("total_result1.csv", "w")
fw.write("Median,AVG,MIN,MAX\n")
fw.write("%s,%s,%s,%s\n" % (total_med_response_time, total_avg_response_time, total_min_response_time, total_max_response_time))
fw.close()

fw = open("total_result2.csv", "w")
fw.write("Total,Fails\n")
fw.write("%s,%s\n" % (total_num_requests, total_num_failures))
fw.close()



if total_num_requests == 0:
    sys.exit("There is no reqest, something goes wrong!")
else:
    print("num_requests: PASSED")

if not all(int(i) == 0 for i in num_failures):
    sys.exit("There are some requests failed")
else:
    print("num_failures: PASSED")

if not all(int(i) <= MIN_RESPONSE_TIME for i in min_response_time):
    sys.exit("There are some min_response_time bigger than %d ms\n MIN_RESPONSE_TIME: %s" % (MIN_RESPONSE_TIME, min_response_time))
else:
    print("min_response_time: PASSED")

if not all(int(i) <= MAX_RESPONSE_TIME for i in max_response_time):
    sys.exit("There are some max_response_time bigger than %d ms\n MAX_RESPONSE_TIME: %s" % (MAX_RESPONSE_TIME, max_response_time))
else:
    print("max_response_time: PASSED")

if not all(int(i) <= AVG_RESPONSE_TIME for i in avg_response_time):
    sys.exit("There are some avg_response_time bigger than %d ms\n AVG_RESPONSE_TIME: %s" % (AVG_RESPONSE_TIME, avg_response_time))
else:
    print("avg_response_time: PASSED")