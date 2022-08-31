import pyfiglet
import sys
import socket
from datetime import datetime
import errno


ascii_banner = pyfiglet.figlet_format("MY PORT SCANNER")
print(ascii_banner)

target = input(str("Target IP:  "))

#banner
print("_" * 50)
print("Scanning Target::" + target)
print("Scanning started at: " + str(datetime.now()))
print("_" * 50)

try:

#scan every port on target ip
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

#return open port
    result = s.connect_ex((target,port))
    if result == 0:
        print("[*] Port {} is open!".format(port))
    if result == 1:
        print("No Available Ports Open")
    

except socket.gaierror:
    print ("Hostname could not be resolved. Exiting")
    sys.exit()
except socket.error:
    print ("Couldnt connect to server")
    sys.exit()



