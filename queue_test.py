#!python

from pprint import pprint
from queue import Queue
import unittest


class QueueTest(unittest.TestCase):

    def test_init(self):
        q = Queue()
        # print(dir(q))
        assert q.front() is None
        assert q.length() == 0
        assert q.is_empty() is True

    def test_init_with_list(self):
        q = Queue(['A', 'B', 'C'])
        # print(dir(q))
        assert q.front() == 'A'
        assert q.length() == 3
        assert q.is_empty() is False

    def test_length(self):
        q = Queue()
        # print(dir(q))
        assert q.length() == 0
        q.enqueue('A')
        assert q.length() == 1
        q.enqueue('B')
        assert q.length() == 2
        q.dequeue()
        assert q.length() == 1
        q.dequeue()
        assert q.length() == 0
        print('passed all length assertions')

    def test_enqueue(self):
        q = Queue()
        # print(dir(q))
        q.enqueue('A')
        assert q.front() == 'A'
        assert q.length() == 1
        q.enqueue('B')
        assert q.front() == 'A'
        assert q.length() == 2
        q.enqueue('C')
        assert q.front() == 'A'
        assert q.length() == 3
        assert q.is_empty() is False

    def test_front(self):
        q = Queue()
        # print(dir(q))
        assert q.front() is None
        q.enqueue('A')
        assert q.front() == 'A'
        q.enqueue('B')
        assert q.front() == 'A'
        q.dequeue()
        assert q.front() == 'B'
        q.dequeue()
        assert q.front() is None

    def test_dequeue(self):
        q = Queue(['A', 'B', 'C'])
        # print(dir(q))
        assert q.dequeue() == 'A'
        assert q.length() == 2
        assert q.dequeue() == 'B'
        assert q.length() == 1
        assert q.dequeue() == 'C'
        assert q.length() == 0
        assert q.is_empty() is True
        with self.assertRaises(ValueError):
            q.dequeue()


def test_length():
    print(Queue)
    # pprint(dir(Queue))
    q = Queue()
    # q.enqueue('A')
    print(q)
    # pprint(dir(q))
    assert q.length() == 0
    q.enqueue('A')
    assert q.length() == 1
    q.enqueue('B')
    assert q.length() == 2
    q.dequeue()
    assert q.length() == 1
    q.dequeue()
    assert q.length() == 0
    print('passed all length assertions')


if __name__ == '__main__':
    unittest.main()
    # test_length()
    # q= Queue(['a', 'b', 'c'])
    # print(q)
    # print(q.length())
    # print(dir(q))
