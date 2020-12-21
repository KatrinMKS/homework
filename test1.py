import unittest
import collections
from homework import QueueContainer

class TestQueueContainer(unittest.TestCase):

    def _init_(self):
        
        self.test_queue = collections.deque()
        newQueue = QueueContainer

        newQueue.append(10)
        newQueue.append(0)
        newQueue.append(1202)
        self.test_queue.append(10)
        self.test_queue.append(0)
        self.test_queue.append(1202)

    def test_append(self):
        self.assertEqual(newQueue.queue[0], self.test_queue[0])
        self.assertEqual(newQueue.queue[1], self.test_queue[1])
        self.assertEqual(newQueue.queue[2], self.test_queue[2])

    def test_showQueue(self):
        self.asserEqual(newQueue.showQueue(), self.test_queue)

    def test_popleft(self):

        newQueue.popleft()
        self.test_queue.popleft()
        self.asserEqual(newQueue.showQueue(), self.test_queue)

        newQueue.popleft()
        self.test_queue.popleft()
        self.asserEqual(newQueue.showQueue(), self.test_queue)

        newQueue.popleft()
        self.test_queue.popleft()
        self.asserEqual(newQueue.showQueue(), self.test_queue)
