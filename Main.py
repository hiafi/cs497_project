#!/usr/bin/python
#------------------------------------------------------------------------------
#Jonathan Roberts, Nathaniel Nguyen, and John Ho
#Computer Science 497B
#Spring Quarter 2013
#Network Intrusion Project
#------------------------------------------------------------------------------

from csv import reader
from Log import Log
from Analysis import attribute_clustering, average_value
from Util import filter_by_type

attack_types = ['normal', 'buffer_overflow', 'ftp_write', 'back', 
'guess_passwd', 'imap', 'ipsweep', 'land', 'loadmodule', 'multihop',
'neptune', 'nmap', 'perl' 'phf', 'pod', 'portsweep', 'rootkit', 'satan', 
'smurf', 'spy', 'teardrop', 'warezclient', 'warezmaster']

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
    data = parse_file("network_dataset.csv") 
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
        


if __name__ == "__main__":
    main()
