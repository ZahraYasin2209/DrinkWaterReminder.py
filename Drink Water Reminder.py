# Exercise#11: Drink Water Reminder

# Write a python program which reminds you of drinking water every hour or two. 
# Your program can either beep or send desktop notifications for a specific operating system

# Method#1: (Produces sound after every hour)
import win32com.client as wincom    # Importing API win32

# you can insert gaps in the narration by adding sleep calls
import time

speak = wincom.Dispatch("SAPI.SpVoice")

while True:
  speak.Speak("Hey Zahra! Drink Water.")
  time.sleep(3600)

# Method#2 (display notification)


from plyer import notification
import time

while True:
    notification.notify(
        title = "Reminder",    # The large header text at the top of a notification.
        message = "Hey Zahra! Drink Water.",  # The longer, smaller text for detailed information.
        app_icon = None,       # The image that appears next to the title and message.
        timeout = 5,           # How long the message should show on screen.
    )
    time.sleep(3600)   # an hour has 3600 seconds


