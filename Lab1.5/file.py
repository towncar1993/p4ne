from glob import *
import re

f=glob("/Users/aleksandrgarshin/Seafile/p4ne_training/config_files/*.txt")

mylist=list("")

for file in f:
    with open(file) as curfile:
        for curline in curfile:
            if blob(re.match("ip address ([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9])", curline)):mylist.append(curline)


i=sorted(list(set(list(mylist))))


for str2 in i:
    print(str2.replace("ip address", "").strip())