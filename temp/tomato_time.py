import arrow
import datetime

t = arrow.get("2018-07-16 15:10")
while t < arrow.get("2018-07-16 18:00"):
    t1 = t + datetime.timedelta(minutes=5)
    t += datetime.timedelta(minutes=30)
    print("{}-{}".format(t1.format("HH:mm"), t.format("HH:mm")))
