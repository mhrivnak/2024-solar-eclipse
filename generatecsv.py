#!/usr/bin/env python

import csv
import subprocess

codes = set()
airports = {}

with open('airports.txt') as f:
    for line in f.readlines():
        codes.add(line.strip())

with open('airport-codes.csv') as csvfile:
    r = csv.DictReader(csvfile)
    for row in r:
        if row['iso_country'] == 'US' and row['local_code'] in codes:
            airports[row['local_code']] = row

with open('airports.txt') as f:
    for line in f.readlines():
        airport = airports[line.strip()]
        # for some reason the data has lat/lon reversed
        lonlat = airport['coordinates'].split(', ')
        lonlat.reverse()
        latlon = ','.join(lonlat)
        
        result = subprocess.run(['./duration.sh', latlon], stdout=subprocess.PIPE)
        duration = result.stdout.decode().strip()
        print(','.join([airport['local_code'], airport['name'], duration, latlon]))
