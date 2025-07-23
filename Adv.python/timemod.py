from datetime import *
from time import *
from calendar import *




# d1=datetime.today()
# d2=datetime(2012,12,31,10,10,10)
# print(d2)

# year=d1-d2

# dat=date(2012,12,31)
# tim=time(hour=10,minute=10,second=10)
# print(dat)
# print(tim)

# credat=datetime.combine(dat,tim)
# print(credat)

# td=timedelta(days=730)
# exp=credat+td
# print(exp)

# d=datetime.now()
# str1=datetime.strftime(d,"%a/%B/%y, %H:%M:%S")
# print(str1)

# str2='2005 July 5 12:28:10'
# dat1=datetime.strptime(str2,'%Y %B %d %H:%M:%S')
# print(type(dat1))



c=calendar(2025)
print(c)

m=month(2025,7)
print(m)

d=Day(6)
print(d)

l=leapdays(2000,2025)
print(l)

