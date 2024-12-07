import time
import random
import string

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
    
    def _hash_function(self, key):
        if isinstance(key, str):
            return sum(ord(char) for char in key) % self.size
        return key % self.size
    
    def insert(self, key, value):
        index = self._hash_function(key)
        
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = Node(key, value)
    
    def retrieve(self, key):
        index = self._hash_function(key)
        
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    def remove(self, key):
        index = self._hash_function(key)
        
        current = self.table[index]
        prev = None
        
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return
            prev = current
            current = current.next

def generate_random_key():
    """Generate a random string key"""
    return ''.join(random.choices(string.ascii_letters, k=5))

def generate_random_value():
    """Generate a random integer value"""
    return random.randint(1, 1000000)

def performance_test(n_operations):
    """Test performance with n operations"""
    ht = HashTable(size=n_operations * 2)  # Size twice the operations to avoid too many collisions
    
    # Test Insert
    start_time = time.time()
    for _ in range(n_operations):
        key = generate_random_key()
        value = generate_random_value()
        ht.insert(key, value)
    insert_time = time.time() - start_time
    
    # Generate keys for testing retrieval
    test_keys = [generate_random_key() for _ in range(n_operations)]
    
    # Test Retrieve
    start_time = time.time()
    for key in test_keys:
        ht.retrieve(key)
    retrieve_time = time.time() - start_time
    
    # Test Remove
    start_time = time.time()
    for key in test_keys:
        ht.remove(key)
    remove_time = time.time() - start_time
    
    return insert_time, retrieve_time, remove_time

def run_performance_tests():
    test_sizes = [100, 1000, 10000]
    print("Performance Test Results:")
    print("-" * 50)
    print(f"{'Size':<10} {'Insert(s)':<12} {'Retrieve(s)':<12} {'Remove(s)':<12}")
    print("-" * 50)
    
    for size in test_sizes:
        insert_time, retrieve_time, remove_time = performance_test(size)
        print(f"{size:<10} {insert_time:<12.6f} {retrieve_time:<12.6f} {remove_time:<12.6f}")

if __name__ == "__main__":
    # Basic functionality test
    ht = HashTable()
    print("Testing basic functionality:")
    ht.insert("name", "John")
    ht.insert("age", 25)
    ht.insert("city", "New York")
    
    print("Testing retrieval:")
    print(f"name: {ht.retrieve('name')}")
    print(f"age: {ht.retrieve('age')}")
    print(f"city: {ht.retrieve('city')}")
    
    ht.insert("name", "Jane")
    print(f"Updated name: {ht.retrieve('name')}")
    
    ht.remove("age")
    print(f"After removing age: {ht.retrieve('age')}")
    print(f"Non-existent key: {ht.retrieve('country')}")
    
    print("\nRunning performance tests...")
    run_performance_tests()