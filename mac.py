import os
import sys

sys.path.append(os.path.abspath('modules'))
import runner

def main():

    # Instantiate the AtomicRunner class instance.
    techniques = runner.AtomicRunner()
    
    # Boot or Logon Initialization Scripts: Rc.common
    techniques.execute("T1037.004", position=0)
    
if __name__ == "__main__":
    main()