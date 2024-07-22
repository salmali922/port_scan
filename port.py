import sys
import socket
import threading
import time

use = "python port.py target start end"
print("-"*50)
print("Simple Port Scanner")
print("-"*50)

if len(sys.argv) != 4:
    print(use)
    sys.exit()

try:
    t = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Error: Unable to resolve hostname")
    sys.exit()

start = int(sys.argv[2])
end = int(sys.argv[3])

print("Scanning target:", t)

def scan(p):
    #print("Scanning port: ", p)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(15)
    con = s.connect_ex((t, p))
    if not con:
        print("Port {} is Open".format(p))
    s.close()

threads = []
for p in range(start, end + 1):
    th = threading.Thread(target=scan, args=(p,))
    th.start()
    threads.append(th)

for th in threads:
    th.join()

et = time.time()
print("Time taken:", et - time.time())