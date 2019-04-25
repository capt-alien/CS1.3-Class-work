"""Help credit: Steve"""
from hashtable import HashTable

class Set(object):
    #init method adds elements in sequence
    def __init__(self, elements= None):
        # init as hash HashTable
        self.hash_set = HashTable
        if elements != None:
            self.add(item)


#Operations on single element:
    def size(self, element):
        return self.hash_set.size

    def contains(self, element):
        #return a boolian if element is in set
        return self.hash_set.contains(element)

    def add(self, element):
        #adds an element to the set
        if self.contains(element) == False:
            self.hash_set.set(element, value = None)

    def remove(self, element):
        if self.contains(element) == True:
            self.hash_set.delete(element)


#Operations on another set
    def union(self, set_b):
        pass

    def intersection(self, set_b):
        pass

    def difference(self, set_b):
        pass

    def is_subset(self, set_b):
        pass
