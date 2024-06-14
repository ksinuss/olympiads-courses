import json
import requests
from datetime import datetime

data_ = [
    {"object": "mount", "date_time": "2023.04.02 11:54", "distance": 2400},
    {"object": "asteroid", "date_time": "2023.04.02 12:30", "distance": 4800},
    {"object": "bolid", "date_time": "2023.04.01 11:50", "distance": 15400},
    {"object": "meteorite", "date_time": "2023.04.02 12:14", "distance": 3600},
    {"object": "sandstone", "date_time": "2023.04.02 12:44", "distance": 9600}
]

def create_datetime_minutes(date_time):
    date, time = date_time.split()
    date = list(map(int, date.split('.')))
    time = list(map(int, time.split(':')))
    dt = date + time
    dt = datetime(*dt)
    dt = dt.timestamp() / 60
    return dt

def danger_object(host, port, date_time_starship, speed):
    # data = requests.get(f'https://{host}:{port}')
    data = data_
    omin = {
        'object': '',
        'difference': float('inf')
    }
    dt_starship = create_datetime_minutes(date_time_starship)
    for object in data:
        date_time = object['date_time']
        dt = create_datetime_minutes(date_time)
        minutes = object['distance'] / speed
        dt_arrival = dt_starship + minutes
        dts = (dt_arrival, dt)
        difference = max(dts) - min(dts)
        difference = int(difference)
        if difference < omin["difference"]:
            omin["object"] = object['object']
            omin["difference"] = difference
    print(omin["object"], omin["difference"])

# date_time = input()
# speed = input()
date_time_starship = '2023.04.02 12:00'
speed = '120'

with open('danger.json', mode='r') as file:
    f = json.load(file)
    danger_object(host=f['host'], port=f['port'], date_time_starship=date_time_starship, speed=int(speed))
