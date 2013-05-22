#!/usr/bin/python
#------------------------------------------------------------------------------
#Jonathan Roberts, Nathaniel Nguyen, and John Ho
#Computer Science 497B
#Spring Quarter 2013
#Network Intrusion Project
#------------------------------------------------------------------------------
#Utility Functions

def filter_by_type(data_set, class_name):
    return [obj for obj in data_set if obj.attack_type == class_name]


