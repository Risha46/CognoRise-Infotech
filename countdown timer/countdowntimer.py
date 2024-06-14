# Import necessary module
import time

# Countdown function
def countdown(seconds):
    # Loop until seconds is 0
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  # Convert seconds to minutes and seconds
        hours, mins = divmod(mins, 60)  # Convert minutes to hours and minutes
        print('{:02d}:{:02d}:{:02d}'.format(hours, mins, secs), end='\r')  # Print current countdown value
        time.sleep(1)  # Wait for 1 second
        seconds -= 1  # Decrease seconds by 1
    print("The timeout has elapsed!")  # Countdown finished message

# Get user input for the countdown
seconds = int(input("Enter the number of seconds to countdown: "))
countdown(seconds)  # Start the countdown