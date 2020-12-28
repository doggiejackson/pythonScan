#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

#clear the screen
subprocess.call('clear',shell=True)

#ask for imput
remoteServer = input("Enter a remote host to  scan:")
remoteServerIP = socket.gethostbyname(remoteServer)

#Print a nice banner wity imformation on which host we are a bout to scan
print("-" * 60)
print("please wait, scanning host",remoteServerIP)
print("-" * 60)

# check what time the scan started
t1=datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)

# We also put in some error handing for catching errors

try:
  for port in range(1,100):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result=sock.connect_ex((remoteServerIP,port))
  #  print("We are in the loop")
    if result==0:
      print("port{}:   Open".format(port))
    sock.close()

except KeyboardInterrupt:
  print("You pressed Ctrl+C")
  sys.exit()

except socket.gaierror:
  print('Hostname could not be resolved. Exiting')
  sys.exit()

except socket.error:
  print("Couldn't connect to sever")
  sys.exit()

# Checking the time again
t2=datetime.now()

# Calculates the diffrence of time, to seehow long it took to run the script
total=t2-t1

# Printing the information to screen 
print('Scanning Completed in:',total)
