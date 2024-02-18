from SERVICES.CRON_JOBS.cron_blacklist_IP_analysis import check_ip_blacklist_main
from SERVICES.CRON_JOBS.main_hash_scan import main_hash_scan

BASE_DIR = "/home/bhagya/research/code/Log_Analyzer_Application/"

with open(BASE_DIR + "AGENT_INFO/agent_info.txt", 'r') as agent_info:
    for agent_ip in agent_info:
        
        check_ip_blacklist_main(BASE_DIR, agent_ip.strip())
        main_hash_scan(BASE_DIR, agent_ip)








        
    


