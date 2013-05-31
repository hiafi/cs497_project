#!/usr/bin/python
#------------------------------------------------------------------------------
#Jonathan Roberts, Nathaniel Nguyen, and John Ho
#Computer Science 497B
#Spring Quarter 2013
#Network Intrusion Project
#------------------------------------------------------------------------------
#Utility Functions

#------------------------------------------------------------------------------
def filter_by_type(data_set, class_name):
    return [obj for obj in data_set if obj.attack_type == class_name]

def normal_discrete_coordinates(data_set):
    final_data = []
    for attr in data_set[0].__dict__.iterkeys():
        if attr == "attack_type":
            continue
        data = [getattr(x, attr, 0) for x in data_set]
        if (isinstance(getattr(data_set[0], attr, 0), float) or
            isinstance(getattr(data_set[0], attr, 0), int)):    
            mx, mn = (max(data), min(data))
            if mx == 0:
                mx, mn = (1, 0)
        for point_index, value in enumerate(data_set):
            if isinstance(data[point_index], str):
                value = data_set[point_index].get_discrete_value(attr)
            elif isinstance(data[point_index], bool):
                value = 1 if data[point_index] else 0
            else:
                value = 1 if (data[point_index] - mn) / mx > .5 else 0

            if len(final_data) <= point_index:
                final_data.append( [value] )
            else:
                final_data[point_index].append(value)

    return final_data
