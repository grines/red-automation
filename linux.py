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
    techniques.execute("T1546.004", position=0, cleanup=True) # Add command to .bash_profile
    techniques.execute("T1546.004", position=1, cleanup=True) # Add command to .bashrc
    techniques.execute("T1053.003", position=0, cleanup=True) # Cron - Replace crontab with referenced file
    techniques.execute("T1053.003", position=1, cleanup=True) # Cron - Add script to cron folder
    techniques.execute("T1547.006", position=0, cleanup=True) # Linux - Load Kernel Module via insmod
    techniques.execute("T1574.006", position=0, cleanup=True) # Shared Library Injection via /etc/ld.so.preload
    techniques.execute("T1574.006", position=1, cleanup=True) # Shared Library Injection via LD_PRELOAD
    techniques.execute("T1548.001", position=0, cleanup=True) # Make and modify binary from C source
    techniques.execute("T1548.001", position=1, cleanup=True) # Set a SetUID flag on file
    techniques.execute("T1548.001", position=2, cleanup=True) # Set a SetGID flag on file
    techniques.execute("T1548.003", position=0, cleanup=True) # Sudo usage
    techniques.execute("T1548.003", position=1, cleanup=True) # Unlimited sudo cache timeout
    techniques.execute("T1548.003", position=2, cleanup=True) # Disable tty_tickets for sudo caching
    techniques.execute("T1543.002", position=0, cleanup=True) # Create Systemd Service
    techniques.execute("T1546.005", position=0, cleanup=True) # Trap


    ## Persistence


    
if __name__ == "__main__":
    main()