import datetime
from datetime import timedelta

current_date = datetime.datetime.now()

def display_current_datetime():
    print(f"Current date and time: {current_date.year}-{current_date.month}-{current_date.day} {current_date.hour}:{current_date.minute}:{current_date.second}")

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=number_of_days)
    print(f"Future date: {future_date.year}-{future_date.month}-{future_date.day}")

display_current_datetime()
calculate_future_date()