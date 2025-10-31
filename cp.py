from datetime import datetime
import time

date_time = datetime(2025, 11, 21, 10, 5)
we_out = datetime(2028, 5, 10, 10,5)

def countdown(target_dt):
    while True:
        # CORRECTED: Use datetime.now() to get the current time
        now = datetime.now()
        time_left = target_dt - now

        if time_left.total_seconds() <= 0:
            print("YOUUUU DONEEEEE")
            break

        days = time_left.days
        hours = time_left.seconds // 3600
        minutes = (time_left.seconds % 3600) // 60
        seconds = time_left.seconds % 60

        # Print the countdown, overwriting the previous line
        print(f"Time remaining: {days} days, {hours:02d} hours, {minutes:02d} minutes, {seconds:02d} seconds", end='\r')

        # Pause for 1 second
        time.sleep(1)

countdown(date_time) 
countdown(we_out)