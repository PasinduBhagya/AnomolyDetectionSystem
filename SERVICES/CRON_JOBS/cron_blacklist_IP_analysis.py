import requests
from ..FUNCTIONS.send_emails import send_email

from configparser import ConfigParser

config = ConfigParser()
config.read('./configurations.cfg')

API_KEY = config.get('BLACKLIST_IP_API', 'API_KEY')
API_URL = config.get('BLACKLIST_IP_API', 'API_URL')


def notifying(ip_address, agent_ip):
    email_content = f'''<h1>Malicious incident Detected on the Server ({agent_ip})</h1></br></br>
    <h2>Information About the Malicious File</h2></br></br>
    <h3>Server has established a connection with a blacklisted IP: {ip_address}</h3>'''
    send_email(agent_ip, email_content)
    print(f"Email Sent For - \t\t{ip_address}")


def abuseIPDB_check_ip_blacklist(ip_address):
    black_listed_status = False

    url = f'{API_URL}={ip_address}'
    headers = {'Key': API_KEY, 'Accept': 'application/json'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # print(data)
        if not data['data']['isWhitelisted']:
            if data['data']['totalReports'] > 0:
                print("AbuseIPDB Detected a Blacklisted IP: - " + str(ip_address))

                black_listed_status = True

    else:
        print('Error occurred')

    return black_listed_status


# Main function
def check_ip_blacklist_main(base_dir, agent_ip):
    with open(base_dir + "AGENT_DATA/" + agent_ip + "/received_data/ip_info.txt", "r") as ip_info:
        for ip in ip_info:
            ip = ip.strip()
            if abuseIPDB_check_ip_blacklist(ip):
                notifying(ip, agent_ip)
