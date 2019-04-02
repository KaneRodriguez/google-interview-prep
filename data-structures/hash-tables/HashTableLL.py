# this is a hash table with a linked list implementation

class HashTable:

    def __init__(self, size=100): # TODO: what is a real-world realistic size to start with? How to implement shrinking and expanding of the table?
      self.size = size
      self.map = [None] * size
    
    def _get_hash(self, key):
      hash = 0
      # support for strings only
      # TODO: support numbers, complex numbers, tuples, and other immutable datatypes
      try:
        for char in key:
          hash += ord(char)
      except:
        print("Error getting key hash")
        
      # map hash to somewhere in the array
      hash %= self.size
      
      return hash
      
    def add(self, key, value):
      # get the index in the array that we are mapping our key to
      hash = self._get_hash(key)
    
      # is the table index open?
      if self.map[hash] is None:
        # create a new "LL" from the key and set it to this index
        self.map[hash] = list([[key, value]])
        return True
      else:
        # collision occurred
        for pair in self.map[hash]:
          if pair[0] == key:
            # update value if key found
            pair[1] = value
            return True
            
        # key not found, add it
        self.map[hash].append([key, value])
        return True
    
    def get(self, key):
      hash = self._get_hash(key)

      if self.map[hash] is not None:
        for pair in self.map[hash]:
          if pair[0] == key:
            return pair[1]

      return None
    
    def delete(self, key):
      hash = self._get_hash(key)

      if self.map[hash] is not None:
        for i, pair in enumerate(self.map[hash]):
          if pair[0] == key:
            self.map[hash].pop(i)
            return True
      
      return False
      
# init table small enough to guarantee collisions
hashTable = HashTable(5)

hashTable.delete("Test Delete on Empty")
hashTable.get("Test Get on Empty")
hashTable.add("first", "Some string")
hashTable.add("second", "Some string 2")
hashTable.add("third", "Some string 3")
hashTable.add("fourth", "Some string 4")
hashTable.add("fifth", "Some string 5")
hashTable.add("sixth", "Some string 6")
print(hashTable.get("first"))
print(hashTable.get("fifth"))
print(hashTable.get("third"))
hashTable.delete("first")
print(hashTable.get("first"))
print(hashTable.get("third"))
