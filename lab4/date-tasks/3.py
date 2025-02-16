from datetime import datetime

now = datetime.now()

microsec = now.replace(microsecond=0)

print(now)
print(microsec)