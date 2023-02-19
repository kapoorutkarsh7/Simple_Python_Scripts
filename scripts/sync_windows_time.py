# Script to sync windows system time
# Can run it as a exe file if needed by making an executable

# Importing libraries

import ntplib
import socket
import os
from datetime import datetime

# NTP server to be used
ntp_server = 'pool.ntp.org'

# Timeout in seconds for NTP server response
timeout_in_seconds = 7

# Get current system time
current_system_time = datetime.now()

try:
    # Create NTP client
    ntp_client = ntplib.NTPClient()

    # Get NTP server response
    ntp_client_response = ntp_client.request(host=ntp_server, timeout=timeout_in_seconds)

    # Get NTP server time
    ntp_server_time = datetime.fromtimestamp(ntp_client_response.tx_time)

    # Set system time to NTP server time
    if ntp_server_time > current_system_time:
        print('Setting system time to NTP server time...')
        
        cmd = f'time {ntp_server_time.strftime("%H:%M:%S")}'
        
        cmd_output = os.system(cmd)
        
        if cmd_output == 0:
            print(f'System time has been set to {ntp_server_time}.')
        else:
            print('Unable to set system time.')
    else:
        print('NTP server time is older than system time. No changes made.')
        
except ntplib.NTPException:
    print('NTP server did not respond within timeout.')
    
except socket.gaierror:
    print('Unable to connect to NTP server. Please check internet connection.')
