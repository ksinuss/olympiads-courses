import sys
import json
import argparse
from csv import reader

def service(filename, service_):
    a = {}
    with open(filename, mode='r') as file:
        f = list(reader(file, delimiter=';'))
        for device in f:
            sign, service, sector, place = device
            if service_ in service:
                a[sign] = [sector, int(place)]
    with open("control.json", mode='w') as new_file:
        json.dump(a, new_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename')
    parser.add_argument('--service', default='course')
    data = parser.parse_args(sys.argv[1:])
    print(data, data.filename, data.service)
    service(filename=data.filename, service_=data.service)

# Разбор параметров командной строки в Python:
# https://jenyay.net/Programming/Argparse?ysclid=lwe01yp5ts665475356
