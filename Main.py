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
        completed = 0
        for row in dataFromFile:
            if row:
                listOfData.append(Log(row))
                completed = completed + 1
                sys.stdout.write("\r%d points loaded" %completed)
                sys.stdout.flush()
        print ""
        return listOfData 

#------------------------------------------------------------------------------
def main():
    if len(sys.argv) < 2:
        print "Expects Main.py file_name"
        sys.exit()

    file_name = str(sys.argv[1])
    print "Loading file..."
    data = parse_file(file_name)

    print "Training..."
    training_set, expected_set = normal_discrete_coordinates(data)
    trainer = Trainer(training_set, expected_set)
    trainer.train()

    #Get our predicted set
    predict_set = []
    completed = 0
    print "Predicting..."
    for item in training_set:
        predict_set.append(trainer.predict(item))
        completed = completed + 1
        sys.stdout.write("\r%d points predicted" %completed)
        sys.stdout.flush()

    
    correct = 0
    completed = 0
    print "\nComparing results..."
    for i in range(0, len(predict_set)):
        completed = completed + 1
        sys.stdout.write("\r%d points checked" %completed)
        if predict_set[i] == expected_set[i]:
            correct = correct + 1
        sys.stdout.flush()

    print "\nPrediction rate: " 
    print str(correct) + " / " + str(completed)

#------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
