from hashtable import HashTable

class Set(object):
    #init method adds elements in sequence
    def __init__(self, elements=None):
        # init as hash HashTable
        self.hash_set = HashTable()
        #Size properity within the set
        self.size = 0
        if elements != None:
            for item in elements:
                self.add(item)

    def __iter__(self):
        """Itterate over elements in the set"""
        for element in self.hash_set.keys():
            yield element

    def __len__(self):
        """gives the class a len properity"""
        return self.size

#Operations on single element:
  #commented out due to the impliminentation of the __len__
    # def size(self):
    #     """Best/worst case: O(1)"""
    #     return self.size

    def contains(self, element):
        """Best/worst case: O(n)"""
        #return a boolian if element is in set
        return self.hash_set.contains(element)

    def add(self, element):
        """Best/worst case: O(n)"""
        #adds an element to the set
        if self.contains(element) == False:
            self.hash_set.set(element, value = None)
            self.size += 1

    def remove(self, element):
        """Best/worst case: O(n)"""
        if self.contains(element) == True:
            self.hash_set.delete(element)
            self.size -= 1

# Your union, intersection, and difference methods
# should create and return a new set, without altering
# your set or the given set. Currently, you are initializing
 # a HashTable instead of a new Set, and altering your
  # original set to hold the new values. Change this to
  # add values to and return a new set!

#Operations on another set
    def union(self, set_b):
        """Returns a new set that is the union of two sets
        Best/worst case: O(n)"""
        union_set = Set()
        for item in self:
        # for item in iter(self):
        # for item in self.__iter__():
        # for item in self.hash_set.keys():
            union_set.add(item)
        for item in set_b.hash_set.keys():
            union_set.add(item)
        return union_set

    def intersection(self, set_b):
        """Returns a new set as intersetction of two sets
                Best/worst case: O(n)
                Yes, Anisha I drew inspiration from your code"""
        i_set = Set()
        smaller = self
        bigger = set_b
        if len(self) > len(set_b):
            bigger = self
            smaller = set_b
        for item in smaller:
            if item in bigger:
                i_set.add(item)
        return i_set

    def difference(self, set_b):
        """Returns a new set that is the difference between the two sets
            Best/worst case: O(n)"""
        diff_set = Set()
        #for self
        for item in self:
            if not set_b.contains(item):
                diff_set.add(item)
        #for set_b
        for item in set_b:
            if not self.contains(item):
                diff_set.add(item)
        return diff_set

    def is_subset(self, set_b):
        """Returns a boolian indicating if one set has all the elements
        of the other in it. Best/worst case: O(n)"""
        #if the first set is larger then it cannot be a sub
        if len(self) != len(set_b):
            return False
        #itterate over set to see if elemets are contined in set_b
        for item in self:
            if not set_b.contains(item):
                return False
            else:
                return True


if __name__ == '__main__':
    set_a = Set(['a', 'b', 'c'])
    set_b = Set(['a','b', 'c', 'x', 'y'])
    diff_set = set_a.is_subset(set_b)
    # for x in diff_set:
    print(diff_set)
