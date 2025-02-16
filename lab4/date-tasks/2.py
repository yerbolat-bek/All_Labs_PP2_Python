from datetime import datetime, timedelta

now = datetime.today()

yesterday = now - timedelta(days=1)
tomorrow = now + timedelta(days=1)

print(yesterday)
print(now)
print(tomorrow)