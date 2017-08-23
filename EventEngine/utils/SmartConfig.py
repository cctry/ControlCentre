import socket
from time import sleep

#constant definition
C = 213
L = 28
SSIDTAG = 100
KEYTAG = 120
SEPARATOR = 23

def encode(data):
    """
    encode the ssid or keyphrase into a doubled-length integer list
    :type data: str
    :rtype: List[int]
    """
    res = []
    res.append(getHnibble(data[0])+C)
    res.append(((getHnibble(data[0])^1)<<4)+getLnibble(data[0])+C)
    for i in xrange(1, len(data)): 
        res.append(((getLnibble(data[0])^((2*i)%16))<<4)+getHnibble(data[i])+C)
        res.append(((getHnibble(data[i])^((2*i+1)%16))<<4)+getHnibble(data[i])+C)
    
    return res

def getHnibble(c):
    return ord(c) >> 4

def getLnibble(c):
    return ord(c) & 15

def fabricate(length):
    res = 'F' * length
    return res.encode('ASCII')

def register(ssid, key):
    """
    the entrance function of SmartConfig(tmd)
    :type ssid: str
    :type key: str
    """
    port = 8514
    data = {'key':encode(key), 'ssid':encode(ssid)}
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    for i in xrange(10):
        send(s, port, data, ssid, key)
        sleep(100)      
    
def send(s, port, data, ssid, key):
    #send 1,2,3 for check the bias
    for i in xrange(2):
        s.sendto(fabricate(1), ('<broadcast>', port))
        s.sendto(fabricate(2), ('<broadcast>', port))
        s.sendto(fabricate(3), ('<broadcast>', port))
    #send the tag of ssid
    s.sendto(fabricate(SSIDTAG), ('<broadcast>', port))
    #send the length of ssid
    s.sendto(fabricate(len(ssid)+L), ('<broadcast>', port))
    #send the separator for five times
    for i in xrange(5):
        s.sendto(fabricate(SEPARATOR), ('<broadcast>', port))
    #send the ssid
    for ele in data['ssid']:
        s.sendto(fabricate(ele), ('<broadcast>', port))
    
    #send the tag of key
    s.sendto(fabricate(KEYTAG), ('<broadcast>', port))
    #send the length of key
    s.sendto(fabricate(len(key)), ('<broadcast>', port))
    #send the separator for five times
    for i in xrange(5):
        s.sendto(fabricate(SEPARATOR), ('<broadcast>', port))
    #send the key
    for ele in data['key']:
        s.sendto(fabricate(ele), ('<broadcast>', port))

if __name__ == '__main__':
    register('MYWIFI', '12345678')
