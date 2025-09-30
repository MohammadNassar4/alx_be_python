import datetime
from datetime import timedelta
import time

current_date = datetime.datetime.now()

def display_current_datetime():
    curr_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(curr_date)

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=number_of_days)
    print(f"Future date: {future_date.year}-{future_date.month}-{future_date.day}")

display_current_datetime()
calculate_future_date()