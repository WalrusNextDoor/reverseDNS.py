import socket
import sys

try:
    #print('looking up %s' % line.rstrip())
    name = socket.gethostbyaddr(sys.argv[1].rstrip())
    #print(line.rstrip(), name[0])
    print(name[0])

except socket.herror:
    print("No DNS Record Found")
except socket.gaierror:
    print("gaierror")
except :
    print("Invalid IP supplied")
