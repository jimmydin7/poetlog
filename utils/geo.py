import requests

def request_geo(ip):

    url = f"https://ipinfo.io/{ip}/json"

    try:
        response = requests.get(url, timeout=5)
        print(url)
        response.raise_for_status()
        data = response.json()

        geo_data = {
            "city": data.get('city'),
            "region": data.get('region'),
            "country": data.get('country'),
            "location": data.get('loc'),
            "isp": data.get('org'),
            "timezone": data.get('timezone'),
            "ip": ip

        }

        return geo_data

    except requests.exceptions.RequestException as e:
        print(f"Error requesting IP info: {e}")
        return None
