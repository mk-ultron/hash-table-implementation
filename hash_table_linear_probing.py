import time
import random
import string

class HashTableLinearProbing:
    """
    Hash Table implementation using Linear Probing for collision resolution
    """
    def __init__(self, size=10000):
        self.size = size
        self.table = [None] * size
        self.keys = [None] * size
        self.count = 0

    def _hash_function(self, key):
        if isinstance(key, str):
            return sum(ord(char) for char in key) % self.size
        return key % self.size

    def _find_slot(self, key):
        """Linear probing to find the next available slot"""
        index = self._hash_function(key)
        original_index = index
        
        while True:
            if self.keys[index] is None or self.keys[index] == key:
                return index
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("Hash table is full")

    def insert(self, key, value):
        if self.count >= self.size:
            raise Exception("Hash table is full")
        
        index = self._find_slot(key)
        if self.keys[index] != key:
            self.count += 1
        self.keys[index] = key
        self.table[index] = value

    def retrieve(self, key):
        index = self._hash_function(key)
        original_index = index

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.table[index]
            index = (index + 1) % self.size
            if index == original_index:
                break
        return None

    def remove(self, key):
        index = self._hash_function(key)
        original_index = index

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.table[index] = None
                self.count -= 1
                return
            index = (index + 1) % self.size
            if index == original_index:
                break

def generate_random_key():
    """Generate a random string key"""
    return ''.join(random.choices(string.ascii_letters, k=5))

def generate_random_value():
    """Generate a random integer value"""
    return random.randint(1, 1000000)

def performance_test(n_operations):
    """Test performance with n operations"""
    ht = HashTableLinearProbing(size=n_operations * 2)  # Size twice the operations to avoid too many collisions
    
    # Test Insert
    start_time = time.time()
    for _ in range(n_operations):
        key = generate_random_key()
        value = generate_random_value()
        ht.insert(key, value)
    insert_time = time.time() - start_time
    
    # Generate keys for testing retrieval (mix of existing and non-existing)
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
    # Run basic functionality test
    ht = HashTableLinearProbing(size=10)
    ht.insert("test", 123)
    print("Basic Test:")
    print(f"Retrieved value: {ht.retrieve('test')}")  # Should print 123
    
    # Run performance tests
    print("\nRunning performance tests...")
    run_performance_tests()