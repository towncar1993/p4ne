from pysnmp.hlapi import *

community_name = "public"

ipaddr_string = "10.31.70.107"
port_int = 161

#GET IOS VERSION
result1 = getCmd(SnmpEngine(),
                CommunityData(community_name, mpModel=0),
                UdpTransportTarget((ipaddr_string, port_int)),
                ContextData(),
                ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

for str in result1:
    errorIndication, errorStatus, errorIndex, varBinds = str
    for str2 in varBinds:
        print(str2)

print("")
#GET INTERFACES
result2 = nextCmd(SnmpEngine(),
                CommunityData(community_name, mpModel=0),
                UdpTransportTarget((ipaddr_string, port_int)),
                ContextData(),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')),
                lexicographicMode = False)

for str in result2:
    varBinds = str[3]
    for str2 in varBinds:
        print(str2)