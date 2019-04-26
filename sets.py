"""Help credit: Steve"""
from hashtable import HashTable

class Set(object):
    #init method adds elements in sequence
    def __init__(self, elements=None):
        # init as hash HashTable
        self.hash_set = HashTable
        if elements != None:
            for item in elements:
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
        """Returns a new set that is the union of two sets"""
        temp = HashTable()
        for item in self.hash_set.keys():
            temp.set(item, None)
        for item in set_b.hash_set.keys():
            temp.set(item, None)
        self.hash_set = temp
        return self


    def intersection(self, set_b):
        """Returns a new set as intersetction of two sets"""
        temp = HashTable()
        for item in self.hash_set.keys():
            if set_b.hash_set.contains(item):
                temp.set(item, None)
        self.hash_set = temp
        return self

    def difference(self, set_b):
        """Returns a new set that is the difference between the two sets"""
        for item in self.hash_set.keys():
            if set_b.hash_set.contains(item) == False:
                temp.set(item, None)
        self.hash_set = temp
        return self

    def is_subset(self, set_b):
        """Returns a boolian indicating if one set has all the elements
        of the other in it"""
        #if the first set is larger then it cannot be a sub
        if self.hash_set.size > set_b.hash_set.size:
            return false
        #itterate over set to see if elemets are contined in set_b
        for item in self.hash_set:
            if set_b.hash_set.contains(item) == False:
                return False
            else:
                return True


if __name__ == '__main__':
    set = Set(['a', 'b', 'c'])
    print(set)
