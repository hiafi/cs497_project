#Write different analysis methods in here

def average_value(data_set, attribute):
    data = []
    for item in data_set:
        data.append(getattr(item, attribute, 0))
    return sum(data) / len(data)

def support(data_set, fn):
    """Support is defined as S(x -> y) count(x) / count(all)"""
    return len([obj for obj in data_set if fn(data_set)])/len(data_set)

def confidence(data_set_x, data_set_y):
    """Confidence is defined as C(x -> Y) = count(X) / count(Y)"""
    return len(data_set1) / len(data_set2)
