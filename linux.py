# Run Red Atomic Tests (Linux)
## Hashicorp

import os
import sys

sys.path.append(os.path.abspath('modules'))
import runner

def main():

    # Instantiate the AtomicRunner class instance.
    techniques = runner.AtomicRunner()

    ## Privilege Escalation
    techniques.execute("T1546.004", position=0, parameters=, True, True)
    techniques.execute("T1546.004", position=1) # Add command to .bashrc
    techniques.execute("T1053.003", position=0) # Cron - Replace crontab with referenced file
    techniques.execute("T1053.003", position=1) # Cron - Add script to cron folder
    techniques.execute("T1547.006", position=0) # Linux - Load Kernel Module via insmod
    techniques.execute("T1574.006", position=0) # Shared Library Injection via /etc/ld.so.preload
    techniques.execute("T1574.006", position=1) # Shared Library Injection via LD_PRELOAD
    techniques.execute("T1548.001", position=0) # Make and modify binary from C source
    techniques.execute("T1548.001", position=1) # Set a SetUID flag on file
    techniques.execute("T1548.001", position=2) # Set a SetGID flag on file
    techniques.execute("T1548.003", position=0) # Sudo usage
    techniques.execute("T1548.003", position=1) # Unlimited sudo cache timeout
    techniques.execute("T1548.003", position=2) # Disable tty_tickets for sudo caching
    techniques.execute("T1543.002", position=0) # Create Systemd Service
    techniques.execute("T1546.005", position=0) # Trap


    ## Persistence


    
if __name__ == "__main__":
    main()