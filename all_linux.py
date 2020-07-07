import os
import sys
from csv import reader

sys.path.append(os.path.abspath('modules'))
import runner

def main():

    # Instantiate the AtomicRunner class instance.
    techniques = runner.AtomicRunner()
    
    # Boot or Logon Initialization Scripts: Rc.common
    #techniques.execute("T1037.004", position=0)

    # open file in read mode
    with open('indexes/linux.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            print("---")
            print(row[1])
            print(row[2])
            print(row[3])
            print("---")
            pos = int(row[3]) - 1
            print(pos)
            try:
                techniques.execute(row[1], position=pos, dependencies=True, cleanup=True)
            except:
                pass
    
if __name__ == "__main__":
    main()