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
        test_set = Set(['a','b','c'])
        assert test_set.hash_set.size == 3
        test_set.remove('b')
        assert test_set.hash_set.size == 2


# TEst for multiple sets
    def test_union(self):
        set_a = Set(['a', 'b', 'c'])
        set_b = Set(['x', 'y'])
        union_set = set_a.union(set_b)
        self.assertCountEqual(union_set.hash_set.keys(), ['a', 'b', 'c', 'x', 'y'])
        set_c = Set(['word', 'to', 'your'])
        set_d = Set(['mother'])
        union_set_2 = set_c.union(set_d)
        self.assertCountEqual(union_set_2.hash_set.keys(), ['word', 'to', 'your', 'mother'])
        set_e = Set([1, 2, 3])
        set_f = Set([4, 5])
        union_set_3 = set_e.union(set_f)
        self.assertCountEqual(union_set_3.hash_set.keys(), [1,2,3,4,5])

    def test_intersection(self):
        set_a = Set(['a', 'b', 'c'])
        set_b = Set(['b', 'c', 'x', 'y'])
        intersect_set = set_a.intersection(set_b)
        self.assertCountEqual(union_set.hash_set.keys(), ['b', 'c'])
        set_c = Set([1,2,3,4,5])
        set_d = Set([4,5,6,7])
        intersect_set_2 = set_c.intersection(set_d)
        self.assertCountEqual(union_set.hash_set.keys(), [4,5])

    def test_difference(self):
        set_a = Set(['a', 'b', 'c'])
        set_b = Set(['b', 'c', 'x', 'y'])
        diff_set = set_a.difference(set_b)
        self.assertCountEqual(union_set.hash_set.keys(), ['a', 'x', 'y'])
        set_c = Set([1,2,3,4,5])
        set_d = Set([4,5,6,7])
        intersect_set_2 = set_c.intersection(set_d)
        self.assertCountEqual(union_set.hash_set.keys(), [1,2,3,6,7])

    def test_is_subset(self):
        set_a = Set(['a', 'b', 'c'])
        set_b = Set(['x', 'y'])
        subset = set_a.is_subset(set_b) == False
        set_c = Set(['a', 'b', 'c', 'd', 'e'])
        set_d = Set(['c', 'd'])
        subset = set_c.is_subset(set_d) == True
