import time
import random
import string
from abc import ABC, abstractmethod

class HashTableBase(ABC):
    """
    Abstract base class defining the interface for hash table implementations.
    This provides the common hash function and defines required methods that
    subclasses have to implement
    """
    def __init__(self, size=10):
        self.size = size
    
    def _hash_function(self, key):
        """
        Common hash function - shared by both implementations
        For string keys: sums ASCII values of characters
        For integer keys: uses direct modulo
        """
        if isinstance(key, str):
            return sum(ord(char) for char in key) % self.size
        return key % self.size
    
    @abstractmethod
    def insert(self, key, value):
        pass
    
    @abstractmethod
    def retrieve(self, key):
        pass
    
    @abstractmethod
    def remove(self, key):
        pass

class Node:
    """
    Node class for the chaining implementation.
    Each node represents a key-value pair in the chain and
    includes a reference to the next node in the sequence
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # Reference to next node in the chain

class HashTableChaining(HashTableBase):
    """
    Hash table implementation using chaining for collision resolution.
    Each bucket contains a linked list of nodes, allowing multiple
    items to exist at the same hash index
    """
    def __init__(self, size=10):
        super().__init__(size)
        # Initialize array of empty buckets
        self.table = [None] * size
    
    def insert(self, key, value):
        # Get the bucket index for this key
        index = self._hash_function(key)
        
        # If bucket is empty, create first node
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            # Bucket has existing nodes - traverse the chain
            current = self.table[index]
            while current:
                # Update value if key exists
                if current.key == key:
                    current.value = value
                    return
                # Move to end of chain
                if current.next is None:
                    break
                current = current.next
            # Add new node at end of chain
            current.next = Node(key, value)
    
    def retrieve(self, key):
        # Find the correct bucket
        index = self._hash_function(key)
        current = self.table[index]
        
        # Traverse the chain looking for the key
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    def remove(self, key):
        # Find the correct bucket
        index = self._hash_function(key)
        current = self.table[index]
        prev = None
        
        # Traverse the chain looking for the key
        while current:
            if current.key == key:
                # Handle removal of first node
                if prev is None:
                    self.table[index] = current.next
                # Handle removal of other nodes
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next

class HashTableLinearProbing(HashTableBase):
    """
    Hash table implementation using linear probing for collision resolution.
    When a collision occurs, linearly searches for the next available slot.
    Uses parallel arrays to store keys and values.
    """
    def __init__(self, size=10):
        super().__init__(size)
        # Parallel arrays for keys and values
        self.table = [None] * size  # Stores values
        self.keys = [None] * size   # Stores keys
        self.count = 0              # Tracks number of items in table
    
    def _find_slot(self, key):
        """
        Find next available slot using linear probing.
        Continues checking slots until finding an empty one
        or the same key (for updates).
        """
        index = self._hash_function(key)
        original_index = index
        
        # Keep probing until we find a slot
        while True:
            # Found an empty slot or matching key
            if self.keys[index] is None or self.keys[index] == key:
                return index
            # Move to next slot, wrapping around if necessary
            index = (index + 1) % self.size
            # We've checked all slots - table is full
            if index == original_index:
                raise Exception("Hash table is full")
    
    def insert(self, key, value):
        # Check if table is full
        if self.count >= self.size:
            raise Exception("Hash table is full")
        
        # Find the next available slot
        index = self._find_slot(key)
        
        # Only increment count for new keys
        if self.keys[index] != key:
            self.count += 1
            
        # Store key and value
        self.keys[index] = key
        self.table[index] = value
    
    def retrieve(self, key):
        # Start at the hash index
        index = self._hash_function(key)
        original_index = index

        # Keep checking until we find the key or an empty slot
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.table[index]
            index = (index + 1) % self.size
            # We've checked all slots
            if index == original_index:
                break
        return None
    
    def remove(self, key):
        # Start at the hash index
        index = self._hash_function(key)
        original_index = index

        # Keep checking until we find the key or an empty slot
        while self.keys[index] is not None:
            if self.keys[index] == key:
                # Clear the slot
                self.keys[index] = None
                self.table[index] = None
                self.count -= 1
                return
            index = (index + 1) % self.size
            if index == original_index:
                break

def generate_test_data(n_operations):
    """
    Generate random test data for benchmarking.
    Creates pairs of random string keys and integer values.
    """
    keys = [''.join(random.choices(string.ascii_letters, k=5)) for _ in range(n_operations)]
    values = [random.randint(1, 1000000) for _ in range(n_operations)]
    return list(zip(keys, values))

def benchmark_hash_table(hash_table_class, test_data):
    """
    Run performance benchmarks on a hash table implementation.
    Tests insert, retrieve, and remove operations using the same data.
    """
    # Create table with size double the data to avoid excessive collisions
    ht = hash_table_class(size=len(test_data) * 2)
    
    # Measure insert performance
    start_time = time.time()
    for key, value in test_data:
        ht.insert(key, value)
    insert_time = time.time() - start_time
    
    # Measure retrieval performance
    start_time = time.time()
    for key, _ in test_data:
        ht.retrieve(key)
    retrieve_time = time.time() - start_time
    
    # Measure removal performance
    start_time = time.time()
    for key, _ in test_data:
        ht.remove(key)
    remove_time = time.time() - start_time
    
    return insert_time, retrieve_time, remove_time

def compare_implementations():
    """
    Compare performance of both hash table implementations.
    Runs benchmarks with different data sizes and displays results.
    """
    test_sizes = [100, 1000, 10000]
    implementations = {
        "Chaining": HashTableChaining,
        "Linear Probing": HashTableLinearProbing
    }
    
    # Test each data size
    for size in test_sizes:
        print(f"\nTest size: {size}")
        print("-" * 50)
        print(f"{'Implementation':<15} {'Insert(s)':<12} {'Retrieve(s)':<12} {'Remove(s)':<12}")
        print("-" * 50)
        
        # Generate consistent test data for both implementations
        test_data = generate_test_data(size)
        
        # Run benchmarks for each implementation
        for name, implementation in implementations.items():
            times = benchmark_hash_table(implementation, test_data)
            print(f"{name:<15} {times[0]:<12.6f} {times[1]:<12.6f} {times[2]:<12.6f}")

def run_basic_tests():
    """
    Run basic functionality tests on both implementations.
    Tests basic operations with simple data to verify correct behavior.
    """
    implementations = {
        "Chaining": HashTableChaining(),
        "Linear Probing": HashTableLinearProbing()
    }
    
    # Test data for basic operations
    test_data = [
        ("name", "John"),
        ("age", 25),
        ("city", "New York")
    ]
    
    # Test each implementation
    for name, ht in implementations.items():
        print(f"\nTesting {name} implementation:")
        print("-" * 30)
        
        # Insert test data
        for key, value in test_data:
            ht.insert(key, value)
        
        # Verify retrieval
        for key, expected in test_data:
            result = ht.retrieve(key)
            print(f"Retrieved {key}: {result}")
        
        # Test update operation
        ht.insert("name", "Jane")
        print(f"Updated name: {ht.retrieve('name')}")
        
        # Test removal operation
        ht.remove("age")
        print(f"After removing age: {ht.retrieve('age')}")

if __name__ == "__main__":
    print("Running basic functionality tests...")
    run_basic_tests()
    
    print("\nRunning performance comparison...")
    compare_implementations()