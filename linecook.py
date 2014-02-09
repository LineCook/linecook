import serial
import json
import httplib2
import datetime

import lookup

device = "/dev/ttyACM0"
scanner = serial.Serial(device)

while(1):
    product = scanner.readline()
    for step in lookup.cook_data(lookup.form_upc_url(product)):
        print step

scanner.close()
    
