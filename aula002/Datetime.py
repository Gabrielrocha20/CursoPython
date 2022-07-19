# https://docs.python.org/3.10/library/datetime.html#module-datetime
from datetime import datetime, timedelta

data = datetime.strptime('20/04/2019 20:00:00', '%d/%m/%Y  %H:%M:%S')
data2 = datetime.strptime('25/04/2019 22:33:00', '%d/%m/%Y  %H:%M:%S')
dif = data2 - data

print(dif)