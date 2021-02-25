from playsound import playsound
from datetime import datetime

print('        Welcome to Alarm Clock')
print('*****Set the time for the Alarm*****')
print('    *****Example 15:21:30******')
alarm_time = input('Enter the Time  : ')
print(f'Alarm has Been set for {alarm_time}')
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if alarm_time == current_time:
        print('Its Time to Wake up!!')
        playsound('./sound/Alarm-Clock Sound!!!.mp3')
        break