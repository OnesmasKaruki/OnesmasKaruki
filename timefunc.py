from datetime import datetime, timedelta
time_s = datetime.today()
print(time_s)

#add 2 hour in current time
add_time_s = time_s + timedelta(hours = 2, minutes = 34)
print(add_time_s)