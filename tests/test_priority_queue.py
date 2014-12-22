import unittest
from cranberry.queue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
	def setUp(self):
		self.empty_queue = PriorityQueue()
		self.full_queue = PriorityQueue()
		self.full_queue.put(1)
		self.full_queue.put(2)
		self.full_queue.put(3)

	def testPutWithoutPriority(self):
		self.empty_queue.put(3)
		self.assertEqual(self.empty_queue.data[1], 3)
		self.empty_queue.put(4)
		self.assertEqual(self.empty_queue.data[2], 4)

	def testPutWithPriority(self):
		self.empty_queue.put(2, priority = 3)
		self.assertEqual(self.empty_queue.data[3], 2)
		self.empty_queue.put(3)
		self.assertEqual(self.empty_queue.data[4], 3)

	def testPopWithoutPriority(self):
		with self.assertRaises(Exception):
			self.empty_queue.pop()
		self.assertEqual(self.full_queue.pop(), 3)

	def testPopWithPriority(self):
		with self.assertRaises(Exception):
			self.empty_queue.pop(priority = 1)
		with self.assertRaises(Exception):
			self.full_queue.pop(priority = 4)
		self.assertEqual(self.full_queue.pop(priority = 1), 1)

	def testHighestPriority(self):
		self.assertEqual(self.full_queue.highest_priority(), 3)
		self.assertEqual(self.empty_queue.highest_priority(), 0)

	def testPrioritize(self):
		with self.assertRaises(Exception):
			self.full_queue.prioritize(5)
		self.full_queue.prioritize(3)
		self.assertEqual(self.full_queue.highest_priority(), 4)
