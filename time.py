import time
timestamp=int(time.strftime('%H'))
print(timestamp)
if timestamp<12:
    print("Good Morning")
elif timestamp>12 and timestamp<14: 
    print("Good Afternoon")
elif timestamp>14:
    print("Good Evening")
else:
    print("Good Night")
