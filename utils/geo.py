import requests

API_ENDPOINT = 'https://ipinfo.io/'

def request_geo(ip):
    
    response = requests.get(API_ENDPOINT+f'{ip}/json').json() 

    geo_data = {

        "city": response.get('city'),
        "region": response.get('region'),
        "country": response.get('country'),
        "location": response.get('loc'),
        "isp": response.get('org'),
        "timezone":response.get('timezone')
        
        
    }

    return geo_data