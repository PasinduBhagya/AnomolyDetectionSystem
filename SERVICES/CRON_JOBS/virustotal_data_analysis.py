import requests

from configparser import ConfigParser

config = ConfigParser()
config.read('./configurations.cfg')

url = config.get('VIRUSTOTAL', 'API_URL')
api_key = config.get('VIRUSTOTAL', 'API_KEY')

def virus_total_scan(single_hash_line):
    params = {'apikey': api_key, 'resource': ''}

    malware_status = False

    hash_to_scan = single_hash_line.split()[3]
    print(f"VT Scanning - {hash_to_scan}")

    params['resource'] = hash_to_scan

    try:
        response = requests.get(url, params=params, timeout=30)

        if response.status_code == 200:
            json_response = response.json()

            if json_response['response_code'] == 1:
                positives = json_response['positives']
                if positives != 0:
                    malware_status = True
            else:

                print("Hash Not Found - " + str(single_hash_line))

        else:
            print("No Response")

    except requests.Timeout:
        print("Error Occurred")

    return malware_status


print("----------------------------------------------------------------------------\nScan has been completed.\n")
