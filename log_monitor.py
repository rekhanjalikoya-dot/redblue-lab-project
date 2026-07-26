import time

LOG_FILE = "/var/log/apache2/access.log"
SUSPICIOUS = ["union", "select", "1=1", "script"]

f = open(LOG_FILE, "r")
f.seek(0, 2)
print("Monitoring started...")

while True:
    line = f.readline()
    if not line:
        time.sleep(1)
        continue
    for word in SUSPICIOUS:
        if word in line.lower():
            print("ALERT:", line.strip())
