#!/usr/bin/python
#------------------------------------------------------------------------------
#Jonathan Roberts, Nathaniel Nguyen, and John Ho
#Computer Science 497B
#Spring Quarter 2013
#Network Intrusion Project
#------------------------------------------------------------------------------

from csv import reader
from Log import Log

def parse_file(fname):
    #Opens a file fname and creates a list of all
    #the network intrusion logs
    with open(fname, 'rb') as f:
        dataFromFile = reader(f)
        listOfData = []
        for row in dataFromFile:
            if row:
                listOfData.append(Log(row))
        return listOfData 

def main():
    parse_file("network_dataset.csv") 


if __name__ == "__main__":
    main()
