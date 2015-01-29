import unittest
from cranberry.optics import OPTICS

class TestOPTICS(unittest.TestCase):
    def testFitWithRegularDensity(self):
        clusterer = OPTICS(epsilon = 2, min_samples = 2)
        data = [(1,1), (0,1), (1,0),
                (10,10), (10, 11), (11, 10),
                (50, 50), (51,50), (50, 51), 
                (100, 100)]
        clusters = clusterer.fit(data)
        print clusters
        self.assertEqual(clusters, [[(1,1), (0,1), (1,0)], 
            [(10,10), (10, 11), (11, 10)], 
            [(50, 50), (51,50), (50, 51)], 
            [(100, 100)]])

    def testFitWithVariousDensity(self):
        clusterer = OPTICS(epsilon = 6, min_samples = 2)
        data = [(0,0),(6,0),(-1,0),(0,1),(0,-1),
                (45,45),(45.1,45.2),(45.1,45.3),(45.8,45.5),(45.2,45.3),
                (50,50),(56,50),(50,52),(50,55),(50,51)]
        clusters = clusterer.fit(data)
        print clusters
        self.assertEqual(clusters, [[(0,0),(-1,0),(0,1),(0,-1)],
                [(6,0)], 
                [(45,45),(45.1,45.2),(45.1,45.3),(45.8,45.5),(45.2,45.3)],
                [(50,50),(50,52),(50,55),(50,51)],
                [(56,50)]])
