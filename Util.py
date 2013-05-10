#Utility Functions

def filter_by_type(data_set, class_name):
    return [obj for obj in data_set if obj.attack_type == class_name]


