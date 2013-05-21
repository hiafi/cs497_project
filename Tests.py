#!/usr/bin/python
#------------------------------------------------------------------------------
#Jonathan Roberts, Nathaniel Nguyen, and John Ho
#Computer Science 497B
#Spring Quarter 2013
#Network Intrusion Project
#------------------------------------------------------------------------------
import unittest
from csv import reader
from Log import Log
from Main import parse_file
from Util import filter_by_type

#Place Tests in here
item_list = [] #Making this global so we only have to load it once 
                #and save 10 seconds from each test

#------------------------------------------------------------------------------
class TestParser(unittest.TestCase):
    
    def setUp(self):
        pass
        #probably shouldn't put a parse_file in here because this will
        #run for each test

    def test_parser(self):
        fname = "network_dataset.csv" 
        rows = 0
        with open(fname, 'rb') as f:
            dataFromFile = reader(f)
            for row in dataFromFile:
                rows += 1
        self.assertEqual(rows, len(parse_file(fname)))

#------------------------------------------------------------------------------
class TestUtil(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def test_filter(self):
        class_name = "back"
        amount = 2203
        self.assertEqual(amount, len(filter_by_type(item_list, class_name)))

#------------------------------------------------------------------------------
class TestAnalysis(unittest.TestCase):
    def setUp(self):
        pass

    def test_average(self):
        pass

    def test_support(self):
        pass

    def test_confidence(self):
        pass

#-------------------------------------------------------------------------------
class TestPoint(unittest.TestPoint):
    def setUp(self):
        pass

    def test_creation(self):
        pass

#-------------------------------------------------------------------------------
class TestCluster(unittest.TestCluster):
    def setUp(self):
        pass
    
    def test_init(self):
        pass

#-------------------------------------------------------------------------------
class TestKMeans(unittest.TestKMeans):
    def setUp(self):
        pass

    def test_kmean(self):
        pass
#------------------------------------------------------------------------------
def run_suite(suite):
    tests = unittest.TestLoader().loadTestsFromTestCase(suite)
    return unittest.TextTestRunner(verbosity=2).run(tests)

#------------------------------------------------------------------------------
if __name__ == '__main__':
    result = run_suite(TestParser)
    if !result.wasSuccessful():
        print ""
        print "Now loading data..."
        item_list = parse_file("network_dataset.csv")
        print "Data loaded"
        print ""
        run_suite(TestUtil)
        print "Now testing Analysis..."
        run_suite(TestAnalysis)

