#!/usr/bin/python
#------------------------------------------------------------------------------
#Jonathan Roberts, Nathaniel Nguyen, and John Ho
#Computer Science 497B
#Spring Quarter 2013
#Network Intrusion Project
#------------------------------------------------------------------------------
#Utility Functions

#------------------------------------------------------------------------------
from sklearn.decomposition import PCA

def filter_by_type(data_set, class_name):
    return [obj for obj in data_set if obj.attack_type == class_name]

def normal_discrete_coordinates(data_set):
    final_data = []
    for attr in data_set[0].__dict__.iterkeys():
        if attr == "attack_type":
            attack_data = [getattr(x, attr, 0) for x in data_set]
            continue
        data = [getattr(x, attr, 0) for x in data_set]
        for point_index, value in enumerate(data_set):
            if isinstance(data[point_index], str):
                value = data_set[point_index].get_discrete_value(attr)
            elif isinstance(data[point_index], bool):
                value = 1 if data[point_index] else 0
            else:
                value = data[point_index]
                #These are float values, this may need to be placed in buckets

            if len(final_data) <= point_index:
                final_data.append( [value] )
            else:
                final_data[point_index].append(value)
    
    pca = PCA(n_components=10, whiten=True).fit(final_data) #This may need to change
    final_data = pca.transform(final_data) 

    return final_data, attack_data
