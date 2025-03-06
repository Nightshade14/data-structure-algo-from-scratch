from hash_set.hash_set import MyHashSet

hash_set = MyHashSet()
hash_table_size = hash_set.hash_table_size

def test_init():
    assert len(hash_set.hash_table) == hash_table_size

def test_add_single():
    test_val = "Hello"
    hash_set.add(test_val)
    hashed_val = abs(hash(test_val))
    bucket_idx = hashed_val % hash_table_size
    fetched_value = hash_set.hash_table[bucket_idx].next.value
    assert fetched_value == test_val

def test_add_multiple():
    test_val_1 = "World"
    test_val_2 = "Multiple"
    hash_set.add(test_val_1)
    hash_set.add(test_val_2)
    hashed_val_1 = abs(hash(test_val_1))
    hashed_val_2 = abs(hash(test_val_2))
    bucket_idx_1 = hashed_val_1 % hash_table_size
    bucket_idx_2 = hashed_val_2 % hash_table_size
    fetched_value_1 = hash_set.hash_table[bucket_idx_1].next.value
    fetched_value_2 = hash_set.hash_table[bucket_idx_2].next.value
    assert  fetched_value_1 == test_val_1
    assert  fetched_value_2 == test_val_2

def test_contains():
    test_val_1 = "Hello"
    test_val_2 = "World"
    test_val_3 = "Intentional false value"

    assert hash_set.contains(test_val_1)
    assert hash_set.contains(test_val_2)
    assert not hash_set.contains(test_val_3)

def test_remove(capsys):
    test_val_1 = "Hello"
    test_val_2 = "World"
    test_val_3 = "Intentional false value"

    hash_set.remove(test_val_1)
    hash_set.remove(test_val_2)
    # hash_set.remove(test_val_3)

    # captured = capsys.readouterr()
    
    # Verify conditions
    # assert "debug Error" in captured.out, "Unexpected error message for non-existent removal"
    assert not hash_set.contains(test_val_1), "Value not removed"
    assert not hash_set.contains(test_val_2), "Value not removed"  


def test_leetcode_case_1():
    hash_set = MyHashSet()

    hash_set.add(1)
    hash_set.add(2)

    assert hash_set.contains(1)
    assert not hash_set.contains(3)

    hash_set.add(2)

    assert hash_set.contains(2)

    hash_set.remove(2)

    assert not hash_set.contains(2)