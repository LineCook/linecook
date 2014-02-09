import socket
import httplib2
import datetime as dt

oven_ip = 'localhost'
oven_port = 8000
base_url = "http://192.168.50.132:8000/upc/"

if __name__ = "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((oven_ip, oven_port))

def form_upc_url(upc):
    url = base_url + upc
    return url

def lookup_cook(lookup_url):
    h=httplib2.Http(".cache")
    # Pull cook content
    (resp_headers, content) = h.request(lookup_url, "GET")
    if (resp_headers.status == 200):
        return content
    else:
        return False

def oven_cmd(url, cmd):
    h = httplib2.Http(".cache")
    #h.add_credentials('name', 'password')
    # Send HTTP command to Green Bean
    (resp, content) = h.request(url, "PUT", body=cmd, headers={'content-type':'text/plain'} )
    if (resp_headers.status == 200):
        return True
    else:
        return False

def parse_cook_instructions(content):
    return content.split(":")

def run(cook_inst):
    flood_time = dt.datetime.now()
    cook_steps = parse_cook_instructions(cook_inst)
    while cook_inst:
        # time elapse check to not flood oven
        if ((dt.datetime.now() - flood_time).seconds > 10):
            # check_state
            flood_time = dt.datetime.now()
            state = send_oven_cmd()
            # If not cancelled
            if state:
                instruction = cook_inst.pop(0)
                send_oven_cmd(instruction)
    return True
