import ipaddress.IPv4Network as IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self, addr, true):
        IPv4Network.__init__(self, addr, true)
        self.address=random.
