import serial
import json
import httplib2
import datetime
import time

import lookup
import oven

device = "/dev/ttyACM0"
scanner = serial.Serial(device)

while(1):
    product = scanner.readline()
    print "Scanned UPC: " + product
    for step in lookup.cook_data(lookup.form_upc_url(product)):
        print "Starting cook step " + step
        (cook_json, cook_path), (check_data, check_path) = oven.parse_instruction(step)
        oven.oven_set(cook_path, cook_json)
        while (oven.oven_get(check_path) != check_data):
            print "Waiting for " + str(check_path) + " == " + str(check_data)
            time.sleep(10)

scanner.close()
    
