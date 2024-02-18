import os
from datetime import date,datetime

def create_dirs_IP_Scan(base_dir, agent_ip):
    # Create the Folder to store current date Data
    agent_IP_Scan_directory = os.path.join(base_dir + "AGENT_DATA/" + agent_ip + "/analyzed_IP_data/" + str(date.today()))

    if not os.path.exists(agent_IP_Scan_directory):
        os.makedirs(agent_IP_Scan_directory)

    current_time = datetime.now()
    # There was issue that time being a minus value. Therefore, an if condition added
    if current_time.hour != 0:
        start_time = datetime(current_time.year, current_time.month, current_time.day, current_time.hour - 1, 0, 0)
    else:
        start_time = datetime(current_time.year, current_time.month, current_time.day, 23, 0, 0)

    end_time = datetime(current_time.year, current_time.month, current_time.day, current_time.hour, 0, 0)

    # Create the file path which saves the data on a single scan file and creates it. For example: 00:00:00-01:00:00.txt
    agent_IP_scan_results_path = base_dir + "AGENT_DATA/" + agent_ip.strip() + "/analyzed_IP_data/" + str(date.today()) + "/" + start_time.strftime("%H:%M:%S") + "-" + end_time.strftime("%H:%M:%S") + ".txt"

    with open(agent_IP_scan_results_path, 'w'):
        pass
    # Return the value to pass to check_ip_blacklist function
    return agent_IP_scan_results_path

def create_dirs_VT_Scan(base_dir, agent_ip):
    # Create the Folder to store current date Data
    agent_VT_Scan_directory = os.path.join(base_dir + "AGENT_DATA/" + agent_ip + "/analyzed_VT_data/" + str(date.today()))

    if not os.path.exists(agent_VT_Scan_directory):
        os.makedirs(agent_VT_Scan_directory)

    current_time = datetime.now()
    # There was issue that time being a minus value. Therefore, an if condition added
    if current_time.hour != 0:
        start_time = datetime(current_time.year, current_time.month, current_time.day, current_time.hour - 1, 0, 0)
    else:
        start_time = datetime(current_time.year, current_time.month, current_time.day, 23, 0, 0)

    end_time = datetime(current_time.year, current_time.month, current_time.day, current_time.hour, 0, 0)

    # Create the file path which saves the data on a single scan file and creates it. For example: 00:00:00-01:00:00.txt
    agent_VT_scan_results_path = base_dir + "AGENT_DATA/" + agent_ip.strip() + "/analyzed_VT_data/" + str(date.today()) + "/" + start_time.strftime("%H:%M:%S") + "-" + end_time.strftime("%H:%M:%S") + ".txt"

    with open(agent_VT_scan_results_path, 'w'):
        pass
    # Return the value to pass to check_ip_blacklist function
    return agent_VT_scan_results_path