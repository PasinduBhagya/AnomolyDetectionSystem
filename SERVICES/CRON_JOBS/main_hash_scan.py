from .virustotal_data_analysis import virus_total_scan
from .kaspesky_data_analysis import kaspersky_scan
from ..FUNCTIONS.send_emails import send_email


def notifying(hash_to_scan, agent_ip, hash_file_path):
    print("----------------------------------------------------------------------------")
    print(f"Malicious File Detected")
    print(f"Hash Value:\t{hash_to_scan}")
    print(f"File Path:\t{hash_to_scan} ")
    print("Sending the Email.....")

    email_content = f'''<h1>Malicious File was Detected on the Server ({agent_ip})</h1></br></br>
                        <h2>Information About the Malicious File</h2></br></br>
                        <h3>File Hash: {hash_to_scan}</h3>
                        <h3>File Path: {hash_file_path}</h3>
                        '''
    send_email(agent_ip, email_content)
    print("Email has been sent.....")


def main_hash_scan(base_dir, agent_ip):
    with open(base_dir + "AGENT_DATA/" + agent_ip.strip() + "/received_data/hashes.txt", 'r') as hash_file:
        for single_hash_line in hash_file:
            if len(single_hash_line.split()) >= 4 and single_hash_line.split()[2] == 'Hash:':
                hash_to_scan = single_hash_line.split()[3]
                hash_file_path = single_hash_line.split()[1]

                if virus_total_scan(single_hash_line) or kaspersky_scan(hash_to_scan):
                    notifying(hash_to_scan, agent_ip, hash_file_path)
