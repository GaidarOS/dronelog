import json
from pprint import pprint

with open('final_log.json') as f:
    data = json.load(f)

# pprint(data)

a_t = []
v_t = []
for dt in data:
    for d in dt:
        if d["pilot"] == "Anders":
            try:
                a_t.append(d['duration'])
                # print(d['duration'][:-1])
            except Exception as x:
                pass
        elif d["pilot"] == "Vasilis":
            try:
                v_t.append(d['duration'])
            except Exception as x:
                pass


# timeList = ['0:00:00', '0:00:15', '9:30:56']
timeList = a_t
print(timeList)
totalSecs = 0
for tm in timeList:
    timeParts = [int(s) for s in tm.split(':')]
    totalSecs += (timeParts[0] * 60 + timeParts[1]) * 60 + timeParts[2]
totalSecs, sec = divmod(totalSecs, 60)
hr, min = divmod(totalSecs, 60)
print("%d:%02d:%02d" % (hr, min, sec))


timeList = v_t
print(timeList)
totalSecs = 0
for tm in timeList:
    timeParts = [int(s) for s in tm.split(':')]
    totalSecs += (timeParts[0] * 60 + timeParts[1]) * 60 + timeParts[2]
totalSecs, sec = divmod(totalSecs, 60)
hr, min = divmod(totalSecs, 60)
print("%d:%02d:%02d" % (hr, min, sec))
