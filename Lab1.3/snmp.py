from pysnmp.hlapi import *

community_name = "public"
ipaddr_string = "10.31.70.107"
port_int = 161


def getSNMP(obj):
    return getCmd(SnmpEngine(),
                  CommunityData(community_name, mpModel=0),
                  UdpTransportTarget((ipaddr_string, port_int)),
                  ContextData(),
                  ObjectType(obj))


def getNextSnmp(obj):
    return nextCmd(SnmpEngine(),
                   CommunityData(community_name, mpModel=0),
                   UdpTransportTarget((ipaddr_string, port_int)),
                   ContextData(),
                   ObjectType(obj),
                   lexicographicMode=False)

# GET IOS VERSION
result1 = getSNMP(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))

for str in result1:
    errorIndication, errorStatus, errorIndex, varBinds = str
    for str2 in varBinds: print(str2[1])

print("")

# GET INTERFACES
result2 = getNextSnmp(ObjectIdentity('1.3.6.1.2.1.2.2.1.2'))

for str_res2 in result2:
    varBinds = str_res2[3]
    for str2_res2 in varBinds: print(str2_res2[1])
























