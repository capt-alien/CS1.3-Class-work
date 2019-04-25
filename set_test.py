import unittest
from sets import Set


class SetTest(unittest.TestCase):
    #test each part of the function
    def test_init(self):
        test_set = Set()
        assert test_set.hash_set.size == 0

    def test_size(self):
        test_set = Set()
        assert test_set.hash_set.size == 0
        test_set.add('a')
        assert test_set.hash_set.size == 1
        test_set.add('b')
        assert test_set.hash_set.size == 2
        test_set.add('c')
        assert test_set.hash_set.size == 3
        test_set.add('d')
        assert test_set.hash_set.size == 4
        test_set.add('e')
        assert test_set.hash_set.size == 5
        #Edge Cases
        test_set.add('')
        assert test_set.hash_set.size == 6
        test_set.add(1)
        assert test_set.hash_set.size == 7
        test_set.add('word')
        assert test_set.hash_set.size == 8
        test_set.add('!')
        assert test_set.hash_set.size == 9
        test_set.add('this is a larger string test')
        assert test_set.hash_set.size == 10
        test_set.add(55)
        assert test_set.hash_set.size == 11
        test_set.add(1.56)
        assert test_set.hash_set.size == 12
        #test to make sure it doesnt add duplicates
        test_set.add('a')
        assert test_set.hash_set.size == 12
        test_set.add(1)
        assert test_set.hash_set.size == 12
        test_set.add(1.56)
        assert test_set.hash_set.size == 12
        test_set.add('word')
        assert test_set.hash_set.size == 12

    def test_contains(self):
        test_set = Set(['a', 'b', 'c', 1, 2.1, "word"])
        assert test_set.contains('a') == True
        assert test_set.contains('b') == True
        assert test_set.contains('c') == True
        # Edge Cases
        assert test_set.contains(1) == True
        assert test_set.contains(1.2) == True
        assert test_set.contains('x') == False
        assert test_set.contains('xyz') == False
        assert test_set.contains(2) == False
        assert test_set.contains(2.123) == False
        assert test_set.contains("Word") == False


    def test_add(self):
        test_set = Set()
        assert test_set.hash_set.size == 0
        test_set.add('a')
        assert test_set.hash_set.size == 1
        assert test_set.contains('a') ==True
        test_set.add('a')
        assert test_set.hash_set.size == 1
        assert test_set.contains('a') ==True
        test_set.add('b')
        assert test_set.hash_set.size == 2
        assert test_set.contains('b') ==True
        #test for int
        test_set.add(12)
        assert test_set.hash_set.size == 3
        assert test_set.contains(12) ==True
        test_set.add(12)
        assert test_set.hash_set.size == 3
        assert test_set.contains(12) ==True
        #test for float
        test_set.add(1.123)
        assert test_set.hash_set.size == 4
        assert test_set.contains(1.123) ==True
        test_set.add(1.123)
        assert test_set.hash_set.size == 4
        assert test_set.contains(12) ==True
        #test for long string
        test_set.add("word to your mother")
        assert test_set.hash_set.size == 5
        assert test_set.contains("word to your mother") ==True
        test_set.add("word to your mother")
        assert test_set.hash_set.size == 5
        assert test_set.contains("word to your mother") ==True

    def test_remove(self):
        pass


# TEst for multiple sets
    def test_union(self):
        pass

    def test_intersection(self):
        pass

    def test_difference(self):
        pass

    def test_is_subset(self):
        pass
