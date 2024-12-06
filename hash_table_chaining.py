class Node:
    """
    Node class for storing key-value pairs in the hash table chain
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    """
    Hash Table implementation using chaining for collision resolution
    """
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
    
    def _hash_function(self, key):
        """
        Simple hash function that converts a key into an index
        """
        if isinstance(key, str):
            # Sum of ASCII values for strings
            return sum(ord(char) for char in key) % self.size
        # For numbers, use modulo
        return key % self.size
    
    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash table
        """
        index = self._hash_function(key)
        
        if self.table[index] is None:
            # If the slot is empty, create new node
            self.table[index] = Node(key, value)
        else:
            # Handle collision by chaining
            current = self.table[index]
            
            # Check if key already exists
            while current:
                if current.key == key:
                    current.value = value  # Update value if key exists
                    return
                if current.next is None:
                    break
                current = current.next
            
            # Add new node to the end of the chain
            current.next = Node(key, value)
    
    def retrieve(self, key):
        """
        Retrieves the value associated with the given key
        Returns None if key is not found
        """
        index = self._hash_function(key)
        
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
            
        return None
    
    def remove(self, key):
        """
        Removes the key-value pair with the specified key
        """
        index = self._hash_function(key)
        
        current = self.table[index]
        prev = None
        
        # Find the node to remove
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return
            prev = current
            current = current.next

# Test cases
def test_hash_table():
    ht = HashTable()
    
    # Test insertion
    ht.insert("name", "John")
    ht.insert("age", 25)
    ht.insert("city", "New York")
    
    # Test retrieval
    print("Testing retrieval:")
    print(f"name: {ht.retrieve('name')}")  # Should print: John
    print(f"age: {ht.retrieve('age')}")    # Should print: 25
    print(f"city: {ht.retrieve('city')}")  # Should print: New York
    
    # Test collision handling
    ht.insert("name", "Jane")  # Should update existing key
    print(f"Updated name: {ht.retrieve('name')}")  # Should print: Jane
    
    # Test removal
    ht.remove("age")
    print(f"After removing age: {ht.retrieve('age')}")  # Should print: None
    
    # Test non-existent key
    print(f"Non-existent key: {ht.retrieve('country')}")  # Should print: None

if __name__ == "__main__":
    test_hash_table()