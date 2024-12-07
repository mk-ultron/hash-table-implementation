# Hash Table Implementations Comparison

This project implements and compares two common hash table collision resolution strategies: Chaining and Linear Probing. The implementation includes comprehensive testing and benchmarking capabilities to demonstrate the performance characteristics of each approach.

## Project Structure

```
hash-tables.py
├── HashTableBase (Abstract Base Class)
├── Node (for Chaining implementation)
├── HashTableChaining
├── HashTableLinearProbing
└── Testing/Benchmarking Utilities
```

## Core Components

### 1. Hash Table Base Class
- Defines common interface for both implementations
- Provides shared hash function for string and integer keys
- Abstract methods: insert, retrieve, remove

### 2. Implementation-Specific Classes

#### Chaining Implementation
```
[→(key1,val1)→(key4,val4), →(key2,val2), →(key3,val3), ...]
```
- Uses linked lists to handle collisions
- Each bucket can hold multiple key-value pairs
- No table size limitations

Flow:
1. Hash key to get bucket index
2. If bucket empty: create new node
3. If bucket occupied: traverse chain to insert/update
4. For retrieval/removal: traverse chain to find key

#### Linear Probing Implementation
```
[None, (key1,val1), None, (key2,val2), ...]
```
- Uses open addressing with linear scanning
- Parallel arrays for keys and values
- Tracks number of stored items

Flow:
1. Hash key to get initial position
2. If slot occupied: probe linearly until empty slot
3. For retrieval: probe until key found or empty slot
4. For removal: mark slot as empty

### 3. Testing and Benchmarking

#### Basic Functionality Tests
- Insert/retrieve/remove operations
- Key updates
- Non-existent key handling

#### Performance Benchmarking
- Tests with varying data sizes (100, 1000, 10000 items)
- Measures operation times:
  - Insertion
  - Retrieval
  - Removal
- Compares both implementations

## Usage

```python
# Basic usage
ht = HashTableChaining()  # or HashTableLinearProbing()
ht.insert("key", "value")
value = ht.retrieve("key")
ht.remove("key")

# Run all tests
python hash_tables.py
```

## Performance Characteristics

### Chaining
- Consistent performance with increasing size
- Better for high load factors
- More memory overhead per element
- Excellent for non-uniform data

### Linear Probing
- Better cache performance
- Lower memory overhead
- Fast with low load factors
- Performance degrades with table size

Example benchmark results:
```
Test size: 10000
--------------------------------------------------
Implementation Insert(s)   Retrieve(s) Remove(s)  
--------------------------------------------------
Chaining      0.022000    0.013502    0.003498
Linear Probing 2.708328    2.643218    0.004999
```

## Implementation Notes

1. **Hash Function**
   - Sums ASCII values for strings
   - Direct modulo for integers
   - Same function used by both implementations

2. **Collision Handling**
   - Chaining: Builds linked lists
   - Linear Probing: Scans for next empty slot

3. **Memory Management**
   - Chaining: Dynamic allocation for nodes
   - Linear Probing: Fixed-size arrays


