import requests

API_ENDPOINT = 'https://ipinfo.io/'

def request_geo(ip):
    
    initial_response = requests.get(API_ENDPOINT+f'{str(ip)}/json', timeout=5)
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