import os
import sys
from csv import reader

sys.path.append(os.path.abspath('modules'))
import runner

def main():

    # Instantiate the AtomicRunner class instance.
    techniques = runner.AtomicRunner()
    
    # loop through and execute linux ttps
    with open('indexes/mac.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            print("--Executing--")
            print(row[1])
            print(row[2])
            print(row[3])
            print("-------------")
            pos = int(row[3]) - 1
            print(pos)
            try:
                output = techniques.execute(row[1], position=pos, dependencies=True, cleanup=True)
            except:
                print("Error: " + row[1])
                pass
            if output:
                print("Success: " + row[1])
    
if __name__ == "__main__":
    main()