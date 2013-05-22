#!/usr/bin/python
#------------------------------------------------------------------------------
#Jonathan Roberts, Nathaniel Nguyen, and John Ho
#Computer Science 497B
#Spring Quarter 2013
#Network Intrusion Project
#------------------------------------------------------------------------------
#Write different analysis methods in here
import Cluster, Point


class Trainer:
    def __init__(self, points):
        self.points = points

    def train(self):
        pass

    def getExpectedType(self, point, class_type ):
        pass

#-------------------------------------------------------------------------------
def average_value(data_set, attribute):
    data = []
    for item in data_set:
        data.append(getattr(item, attribute, 0))
    return sum(data) / len(data)

#------------------------------------------------------------------------------
def attribute_clustering(data_set, attribute):
    data = []
    

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
