from datetime import datetime
from datetime import date

# Nothing to commit
now = datetime.now()
current_time = now.strftime("%H:%M:%S") 
current_date = date.today()
print("Current Time =", current_time)
print("Current Date =", current_date)