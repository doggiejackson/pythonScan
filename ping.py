#!/usr/bin/python3

import subprocess
DB=[]
theFile=open("IP_Found.txt","a")
for brier_creek in range(200,210):
  address="192.168.1."+str(brier_creek)
  res=subprocess.call(['ping','-c','3',address])
  if res==0:
    print("ping to",address,"ok")
    DB.append(address)
    theFile.write(address)
  elif res==2:
    print("no response from",address)
  else:
    print("print to",address,"failed!")
print("booger",address)
print("IP adresses currently in use include:")
print("**********")
for result in range(0,len(DB)):
  print(DB[result])
theFile.close()


