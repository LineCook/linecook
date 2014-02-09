import httplib2

web_url = "http://192.168.50.132:8000"
device_id = "2"
cloud_url = "/".join([web_url, "linecook", device_id, "upc"])

def form_upc_url(upc):
    url = "/".join([cloud_url, upc])
    return url

def cook_data(lookup_url):
    h=httplib2.Http(".cache")
    # Request cook data 
    (resp, content) = h.request(lookup_url, "GET")
    if (resp.status == 200):
        return parse_cook(content)
    else:
        return False

def parse_cook(content):
    return content.split(":")

