import unittest
import collections
from homework import QueueContainer

class TestQueueContainer(unittest.TestCase):

    def _init_(self):
        self.test_queue = collections.deque()

    def test_area(self):
        self.assertEqual(queue.my_append(10), self.test_queue.append(10))
        self.assertEqual(queue.my_append(0), self.test_queue.append(0))
        self.assertEqual(queue.my_append(1210), self.test_queue.append(1210))
