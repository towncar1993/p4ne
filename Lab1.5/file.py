from glob import *
import re

f=glob("/Users/aleksandrgarshin/Seafile/p4ne_training/config_files/*.txt")

mylist=list("")

def parce(str):
    if re.search("ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9])", str):
        ip_addr=re.search("ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9])", str).group(1)
        subnet = re.search("ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9])", str).group(2)
        return ("IP", ip_addr, subnet)
    if re.search("^interface ([a-zA-Z]+[0-9]+)", str):
        interface_name=re.search("^interface ([a-zA-Z]+[0-9]+)", str).group(1)
        return ("INT", interface_name, '')
    if re.search("^hostname ([a-zA-Z]+)", str):
        host_name=re.search("^hostname ([a-zA-Z]+)", str).group(1)
        return ("HOST", host_name, '')
    return ("UNCLASSIFIED",)

for file in f:
    with open(file) as curfile:
        for curline in curfile:
            t = parce(curline)
            if t[0] != "UNCLASSIFIED":
                print(t[0]+' '+t[1]+' '+t[2])
            #if parce(curline)[0] == "IP":mylist.append(parce(curline)[0]+" "+parce(curline)[1]+" "+parce(curline)[2])
            #if parce(curline)[0] == "INT":mylist.append(parce(curline)[0]+" "+parce(curline)[1])
            #if parce(curline)[0] == "HOST":mylist.append(parce(curline)[0]+" "+parce(curline)[1])

#i=sorted(list(set(list(mylist))))


for str2 in mylist:
    print(str2.strip())