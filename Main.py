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
from Util import filter_by_type, normal_discrete_coordinates
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

    training_set, expected_set = normal_discrete_coordinates(data)
    trainer = Trainer(training_set, expected_set)
    trainer.train()

    #Get our predicted set
    predict_set = [trainer.predict(item) for item in training_set]
    
    correct = 0
    for i in range(0, len(predict_set)):
        if predict_set[i] == expected_set[i]:
            correct = correct + 1
            print str(predict_set[i]) + " == " + str(expected_set[i])
        else: 
            print str(predict_set[i]) + " != " + str(expected_set[i])

    print "Prediction rate: " 
    print str(correct / len(predict_set) * 100 ) + "%"
        

#------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
