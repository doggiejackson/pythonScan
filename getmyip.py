import socket
# get the name of my computer we set up
print (socket.gethostname())
# get the IP address of this computer
print (socket.gethostbyname(socket.gethostname()))

