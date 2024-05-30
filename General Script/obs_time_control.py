from datetime import datetime, timedelta
import time
from obswebsocket import obsws, requests

# OBS WebSocket connection settings
host = "localhost"
port = 4455
password = "bahyZIXAwYfvCuME"

# Input start time (24-hour format)
start_time = input("Start Time (e.g.xx:xx):")


    # Calculate the start datetime for recording
current_datetime = datetime.now()
start_datetime = datetime(current_datetime.year, current_datetime.month, current_datetime.day,
                              int(start_time.split(":")[0]), int(start_time.split(":")[1]))

if current_datetime > start_datetime:
        # If the current time has passed the start time, calculate the same time tomorrow
        start_datetime += timedelta(days=1)

    # Calculate the waiting time (in seconds)
wait_time_sec = (start_datetime - current_datetime).total_seconds()

if wait_time_sec > 0:
        print(f"wait {wait_time_sec} s...")
        time.sleep(wait_time_sec)

    # Connect to OBS Studio
ws = obsws(host, port, password)
ws.connect()

while True:

    try:
        # Start recording
        print("Start Recording...")
        ws.call(requests.StartRecord())

        # Wait for a certain duration (e.g., record for 10 seconds)
        time.sleep(10)

        # Stop recording
        print("Stop Recording...")
        ws.call(requests.StopRecord())

    except Exception as e:
        print("Error during recording operation:")
        print(type(e))
        print(e.args)
        print(e)

    # Wait for a certain interval before restarting recording
    restart_interval = 89  
    print(f"Wait {restart_interval} s to restart...")
    time.sleep(restart_interval)

