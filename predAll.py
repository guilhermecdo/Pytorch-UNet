import os
import csv



m=4
auv=33

with open(f"/home/guilherme/Documents/Holoocean-imaging-sonar/mission{m}.csv", newline='') as f:
    reader = csv.reader(f)
    mission_metadata = list(reader)
    mission_metadata.pop(0)

mission=mission_metadata[auv]

for i in range((int(mission[-1])-1)):
     
    comand=(f"python3 predict.py -m elevatenet.pth -c 20 --i /home/guilherme/Documents/SEE-Dataset/Sonar-Dataset-mission-{m}-P900/auv-{auv}/Cartesian-images/{i}.png --o /home/guilherme/Documents/Holoocean-imaging-sonar/experiments-elevatenet/{m}-{auv}/{i}.png")
    os.system(comand)