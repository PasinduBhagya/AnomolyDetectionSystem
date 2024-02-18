import subprocess
import json

from configparser import ConfigParser

config = ConfigParser()
config.read('./configurations.cfg')

def kaspersky_scan(hash_value):
    malware_status = False

    print(f"Kaspersky Scanning: {hash_value}")
    url = f"{config.get('KASPESKEY', 'API_URL')}={hash_value}"

    command = ["curl", "-X", "GET", f"{url}", "-H", f"x-api-key: {{config.get('KASPESKEY', 'API_KEY')}}"]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True).stdout

    response_data = json.loads(result)
    print(f"Scan Results for {hash_value} is {response_data['Zone']}")

    if response_data['Zone'] == "Red":
        malware_status = True

    return malware_status
