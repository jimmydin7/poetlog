import requests

API_ENDPOINT = 'https://ipinfo.io/2a02:586:451a:d600:6dba:b26:9ba9:879b/json'

def request_geo(ip):
    
    initial_response = requests.get(API_ENDPOINT+f'{"[" + str(ip) + "]"}/json', timeout=5)
    response = initial_response.json()

    geo_data = {

        "city": response.get('city'),
        "region": response.get('region'),
        "country": response.get('country'),
        "location": response.get('loc'),
        "isp": response.get('org'),
        "timezone":response.get('timezone')
        
        
    }

    return geo_data