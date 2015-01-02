import unittest
from cranberry.distances import *
from math import hypot

class TestDistances(unittest.TestCase):
    def setUp(self):
        self.point_1 = [1,0]
        self.point_2 = [5,4]
        self.point_3 = [6,3]
        self.point_4 = [7,6]

    def test_euclidean_distance(self):
        self.assertEqual(euclidean_distance(self.point_1, self.point_2), 
                        hypot(self.point_1[0] - self.point_2[0], 
                                self.point_1[1] - self.point_2[1]))

        self.assertEqual(euclidean_distance(self.point_3, self.point_4), 
                        hypot(self.point_3[0] - self.point_4[0], 
                                self.point_3[1] - self.point_4[1]))
    
    def test_jaccard_distance(self):
        self.assertEqual(jaccard_distance(self.point_1, self.point_2), 0)
        self.assertEqual(jaccard_distance(self.point_3, self.point_4), 1/3)
