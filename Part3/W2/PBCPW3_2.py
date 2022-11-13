import matplotlib.pyplot as py
import csv, datetime

# open the file
f = open("ubike.csv", "r")
bike = {}
capacity = {}
count = {}

# processing the data
for row in csv.DictReader(f):
    if row["station"] == "Roosevelt & Xinsheng S. Intersection":
        time = datetime.datetime.strptime(row["time"], "%Y/%m/%d %H:%M")
        hour = time.hour
        if hour not in bike:
            bike[hour] = int(row["bike"])
            capacity[hour] = int(row["lot"])
            count[hour] = 1
        else:
            bike[hour] += int(row["bike"])
            capacity[hour] += int(row["lot"])
            count[hour] += 1 
f.close()

# preparing for plotting
time_seq = bike.keys()
time_seq = sorted(time_seq)
avg = []
lot = []
for k in time_seq:
    avg.append(float(bike[k]) / count[k])
    lot.append(float(capacity[k]) / count[k])
    
# plotting the data in avg and lot
py.plot(time_seq, lot, label = "Average")
py.plot(time_seq, avg, label = "Capacity")
py.title("Bikes at Roosevelt & Xinsheng S. Intersection")
py.xlabel("Time(hr)")
py.ylabel("Bike")
py.ylim(0, max(lot)*1.2)
#py.ylim(0, max(lot)+30) will also do the work
py.legend(loc="upper right")
#py.legned(loc) default also set to upper right
py.show()