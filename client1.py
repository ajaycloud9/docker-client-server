import socket
import sys
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost',60000))

####Send the problem
my_input=sys.argv[1]
print(my_input)
byte_my_input=my_input.encode("ascii")
print(type(byte_my_input))
s.sendall(byte_my_input)
r=s.recv(1024)
