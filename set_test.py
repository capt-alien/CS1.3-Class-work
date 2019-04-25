import unittest
from sets import Set


class SetTest(unittest.TestCase):
    #test each part of the function
    def test_init(self):
        set_test = Set()
        assert set_test.hash_set.size == 0

    def test_size(self):
        set_test = Set()
        assert set_test.hash_set.size == 0
        set_test.add('a')
        assert set_test.hash_set.size == 1
        set_test.add('b')
        assert set_test.hash_set.size == 2
        set_test.add('c')
        assert set_test.hash_set.size == 3
        set_test.add('d')
        assert set_test.hash_set.size == 4
        set_test.add('e')
        assert set_test.hash_set.size == 5
        #Edge Cases
        set_test.add('')
        assert set_test.hash_set.size == 6
        set_test.add(1)
        assert set_test.hash_set.size == 7
        set_test.add('word')
        assert set_test.hash_set.size == 8
        set_test.add('!')
        assert set_test.hash_set.size == 9
        set_test.add('this is a  larger string test')
        assert set_test.hash_set.size == 10
        set_test.add(55)
        assert set_test.hash_set.size == 11
        set_test.add(1.56)
        assert set_test.hash_set.size == 12
        #test to make sure it doesnt add duplicates
        set_test.add('a')
        assert set_test.hash_set.size == 12
        set_test.add(1)
        assert set_test.hash_set.size == 12
        set_test.add(1.56)
        assert set_test.hash_set.size == 12
        set_test.add('word')
        assert set_test.hash_set.size == 12 

    def test_contains(self):
        pass

    def test_add(self):
        pass

    def test_remove(self):
        pass

    def test_union(self):
        pass

    def test_intersection(self):
        pass

    def test_difference(self):
        pass

    def test_is_subset(self):
        pass
