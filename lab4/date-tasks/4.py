from datetime import datetime

date1 = datetime(2025, 6, 23, 17, 30, 0)
date2 = datetime(2025, 6, 23, 17, 30, 5)

diff = (date2 - date1).total_seconds()

print(diff)