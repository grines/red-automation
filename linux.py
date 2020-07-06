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
    techniques.execute("T1546.004", position=1) # Add command to .bash_profile
    techniques.execute("T1546.004", position=2) # Add command to .bashrc
    techniques.execute("T1053.003", position=1) # Cron - Replace crontab with referenced file
    techniques.execute("T1053.003", position=2) # Cron - Add script to cron folder
    techniques.execute("T1547.006", position=1) # Linux - Load Kernel Module via insmod
    techniques.execute("T1574.006", position=1) # Shared Library Injection via /etc/ld.so.preload
    techniques.execute("T1574.006", position=2) # Shared Library Injection via LD_PRELOAD
    techniques.execute("T1548.001", position=1) # Make and modify binary from C source
    techniques.execute("T1548.001", position=2) # Set a SetUID flag on file
    techniques.execute("T1548.001", position=3) # Set a SetGID flag on file
    techniques.execute("T1548.003", position=1) # Sudo usage
    techniques.execute("T1548.003", position=2) # Unlimited sudo cache timeout
    techniques.execute("T1548.003", position=3) # Disable tty_tickets for sudo caching
    techniques.execute("T1543.002", position=1) # Create Systemd Service
    techniques.execute("T1546.005", position=1) # Trap


    ## Persistence


    
if __name__ == "__main__":
    main()