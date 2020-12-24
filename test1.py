import unittest
from task_1 import Queue


class TestQueue(unittest.TestCase):

    def test_size(self):
        q.enQueue(15)
        q.enQueue(23)
        self.assertEqual(q.size, 1)
        q.deQueue()
        q.deQueue()
        self.assertEqual(q.size, 0)

    def test_deQueue(self):
        q.enQueue(15)
        q.enQueue(23)
        self.assertEqual(q.front.info, 15)

    def test_enQueue(self):
        q.enQueue(15)
        q.enQueue(23)
        self.assertEqual(q.rear.info, 23)

