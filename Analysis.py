#!/usr/bin/python
#------------------------------------------------------------------------------
#Jonathan Roberts, Nathaniel Nguyen, and John Ho
#Computer Science 497B
#Spring Quarter 2013
#Network Intrusion Project
#------------------------------------------------------------------------------
#Write different analysis methods in here
import Cluster, Point
import numpy as np
from sklearn.naive_bayes import GaussianNB

#-------------------------------------------------------------------------------
class Trainer:
    def __init__(self, training_set, expected_set):
        self.training_set = np.array(training_set)
        self.expected_set = np.array(expected_set)

    def train(self):
        self.clf = GaussianNB()
        self.clf.fit(self.training_set, self.expected_set)

    def predict(self, point):
        return self.clf.predict(point)[0]

#-------------------------------------------------------------------------------
def average_value(data_set, attribute, normalize=False):
    data = [getattr(x, attribute, 0) for x in data_set]
    if normalize:
        mx, mn = (max(data), min(data))
        if mx == 0:
            return 0
        data = [(x - mn) / mx for x in data]
    return float(sum(data)) / len(data)

#------------------------------------------------------------------------------
def attribute_clustering(data_set, attribute, normalize=False):
    avg = average_value(data_set, attribute, normalize)
    if normalize:
        pre_data = [getattr(x, attribute, 0) for x in data_set]
        mx, mn = (max(pre_data), min(pre_data))
        if mx == 0:
            return None
        data = [abs((x - mn) / mx - avg) for x in pre_data]
    else:
        data = [abs((getattr(x, attribute, 0) - avg)) for x in data_set]
    return float(sum(data)) / len(data)

#-------------------------------------------------------------------------------
def support(data_set, fn):
    #Support is defined as S(x -> y) count(x) / count(all)
    return len([obj for obj in data_set if fn(data_set)])/len(data_set)

#-------------------------------------------------------------------------------
def confidence(data_set_x, data_set_y):
    #Confidence is defined as C(x -> Y) = count(X) / count(Y)
    return len(data_set1) / len(data_set2)

#-------------------------------------------------------------------------------
def kmeans(points, k, cutoff, distanceFormula):
    """
        points  -- a set of coordinates
        k       -- k value for k mean
        cutoff  -- value to cutoff poitns
        distanceFormula     -- Distance function to find distance
    """
    initial = random.sample(points, k)
    clusters = [Cluster.Cluster([p]) for p in initial]

    while True:
        lists = [ [] for c in clusters]
        for p in points:
            smallest_distance = distanceFormula(p, clusters[0].centroid)
            index = 0
            for i in range(len(clusters[1:])):
                distance = distanceFormula(p, clusters[i + 1].centroid)
                if ( distance < smallest_distance ):
                    smallest_distance = distance
                    index = i + 1
            lists[index].append(p)
        
        biggest_shift = 0.0
        for i in range(len(clusters)):
            shift = clusters[i].update(lists[i], distanceFormula)
            biggest_shift = max(biggest_shift, shift)

        if ( biggest_shift < cutoff ):
            break

    return clusters

if __name__ =='__main__':
    a = [[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]]
    b = [1, 1, 1, 2, 2, 2]
    trainer = Trainer(a, b)
    trainer.train()
    print trainer.predict([[-.8,-1]])
    






