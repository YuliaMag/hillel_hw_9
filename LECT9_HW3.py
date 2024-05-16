from datetime import date, timedelta, datetime

sdate = date(2024, 4, 11)
edate = date(2024, 7, 29)

timestamp = 1715703300
dt_object = datetime.fromtimestamp(timestamp)
evtime = dt_object.strftime("%H:%M")

count = 0

for d in range(0, (edate - sdate).days + 1):
    if (sdate + timedelta(days=d)).weekday() == 0 or (sdate + timedelta(days=d)).weekday() == 3:
        if count in range(0, (edate - sdate).days + 1):
            count += 1
        print((sdate + timedelta(days=d)).strftime(f"Lecture {count.__str__().rjust(2)}: %d %h %Y {evtime}"))
