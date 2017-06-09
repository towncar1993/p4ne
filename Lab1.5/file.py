from glob import *

f=glob("/Users/aleksandrgarshin/Seafile/p4ne_training/config_files/*.txt")

mylist=list("")

for file in f:
    with open(file) as curfile:
        for curline in curfile:
            if curline.find("ip address") != -1 and curline.find("no ip address") == -1:mylist.append(curline)


i=sorted(list(set(list(mylist))))


for str2 in i:
    str3=str2.strip()
    print(str3.replace("ip address", ""))