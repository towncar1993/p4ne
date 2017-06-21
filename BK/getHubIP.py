from Exscript import Account
from Exscript.protocols import SSH2


acc = Account('USERNAMESSHAAA', 'PASS')
con = SSH2()
con.connect('ROUTER_IP')
con.login(acc)
con.execute('terminal length 0')
con.execute('ping vrf INTERNET  8.8.8.8')
con.send('exit')
output = con.response