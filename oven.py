import json
import httplib2

oven_ip = '127.0.0.1'
oven_port = '8080'
oven_state = {0: "No Mode", 1: "Preheat", 2: "Convection Bake Preheat"}

json_headers = "Content-Type: application/json"
default_data = {"cookHours": 0, "cookMinutes": 0, "mode": 0, "cookTemperature": 100}

def oven_get(path):
    url = "http://" + oven_ip + ":" + oven_port + "/" + path
    h = httplib2.Http(".cache")
    # Send HTTP command to Green Bean node.js app
    (resp, content) = h.request(url, "GET" )
    if (resp.status == 200):
        return content
    else:
        return False

def oven_set(path, json_data):
    url = "http://" + oven_ip + ":" + oven_port + "/" + path
    h = httplib2.Http(".cache")
    if json_data == None:
        json_data = json.dumps(default_data)
    # Send HTTP command to Green Bean node.js app
    (resp, content) = h.request(url, "PUT", body=json_data, headers=json_headers )
    if (resp.status == 200):
        return True
    else:
        return False

