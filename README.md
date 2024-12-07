# Hash Table Implementation

This repository contains two different implementations of a Hash Table data structure in Python, demonstrating different collision resolution strategies: Linear Probing and Chaining.

## Overview

The repository provides two hash table implementations:
- `HashTableLinearProbing`: Uses linear probing for collision resolution
- `HashTable`: Uses chaining (linked lists) for collision resolution

Both implementations support basic hash table operations:
- Insertion
- Retrieval
- Removal

## Features

- Simple and efficient hash function implementation
- Support for both string and integer keys
- Automatic resizing to prevent excessive collisions
- Performance testing suite included
- Comprehensive error handling

## Implementation Details

### Linear Probing Implementation
The `HashTableLinearProbing` class implements open addressing with linear probing:
- Uses a single array for storage
- Handles collisions by checking subsequent array positions
- Maintains load factor tracking
- Includes separate key storage for efficient lookups

### Chaining Implementation
The `HashTable` class implements separate chaining:
- Uses linked lists to handle collisions
- Each bucket contains a chain of key-value pairs
- Supports dynamic growth of chains
- Memory efficient for high load factors

## Usage

```python
# Using Linear Probing Implementation
ht_linear = HashTableLinearProbing(size=10)
ht_linear.insert("test", 123)
value = ht_linear.retrieve("test")  # Returns 123

# Using Chaining Implementation
ht_chaining = HashTable(size=10)
ht_chaining.insert("name", "John")
ht_chaining.insert("age", 25)
name = ht_chaining.retrieve("name")  # Returns "John"
```

## Performance Testing

Both implementations include a performance testing suite that measures:
- Insertion time
- Retrieval time
- Removal time

The tests are run with different dataset sizes (100, 1000, 10000 operations) to demonstrate scalability.

To run the performance tests:

```python
python hash_table_linear_probing.py  # For linear probing implementation
python hash_table_chaining.py        # For chaining implementation
```

