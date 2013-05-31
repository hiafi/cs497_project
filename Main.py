#!/usr/bin/python
#------------------------------------------------------------------------------
#Jonathan Roberts, Nathaniel Nguyen, and John Ho
#Computer Science 497B
#Spring Quarter 2013
#Network Intrusion Project
#------------------------------------------------------------------------------

from csv import reader
from Log import Log
from Log import attack_types
from Analysis import attribute_clustering, average_value, Trainer
from Util import filter_by_type
import sys


#------------------------------------------------------------------------------
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

#------------------------------------------------------------------------------
def main():
    if len(sys.argv) < 2:
        print "Expects Main.py file_name"
        sys.exit()

    file_name = str(sys.argv[1])
    data = parse_file(file_name)

    training_set = [] #A list of all coordinates from data as a list 
    expected_set = [] #A list of all expected results  of training_set
    trainer = Trainer(training_set, expected_set)
    trainer.train()

    testing_set = [] #A list of all coordinates as a list we're going to predict
    for item in testing_set:
        print trainer.predict(item) # note return value from predict is an int



    for attrName, attrValue in data[0].__dict__.iteritems():
        if isinstance(attrValue, bool):
            continue
        if isinstance(attrValue, str):
            continue

        print attrName
        for attack_type in attack_types:
            type_data = filter_by_type(data, attack_type)
            if len(type_data) > 0:
                print "{0} - Avg Distance (normal): {1}, Average: {2}".format(
                attack_type, 
                attribute_clustering(type_data, attrName, True),
                average_value(type_data, attrName, False))
        print ""
        

#------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
