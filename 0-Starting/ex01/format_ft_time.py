from time import strftime, gmtime, time
from datetime import datetime

formatted_date = (strftime("%B %d, %Y",gmtime(0)))
formatted_date = formatted_date.replace(" 0", " ")
print(f"Seconds since{formatted_date}: ",end='')


seconds_since_epoch = time()
print(f"{seconds_since_epoch:,.3f}","or ",end='')
print(f"{seconds_since_epoch:.2e}" " in scientific notation")

current_date = datetime.now()
day = current_date.day
current_date = current_date.now().strftime(f"%B {day}, %Y")

print(current_date,end='')