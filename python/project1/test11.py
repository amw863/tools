from datetime import datetime
now = datetime.now()
print(now)
print(type(now))
t = now.timestamp()
print(datetime.fromtimestamp(t))
