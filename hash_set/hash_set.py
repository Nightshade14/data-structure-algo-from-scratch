class Node:
    def __init__(self, value=None):
        self.value = value
        self.next: Node | None = None


class MyHashSet:
    def __init__(self):
        # prime numbered buckets further reduce collisions
        # self.hash_table_size = self._next_prime(n=10**4) # 10007
        self.hash_table_size = self._next_prime(n=10**4)
        self.hash_table = [Node() for _ in range(self.hash_table_size)]

    def add(self, key: int) -> None:
        hashed_key = abs(hash(key))
        bucket_idx = hashed_key % self.hash_table_size
        current_node = self.hash_table[bucket_idx]

        while current_node.next:
            if current_node.next.value == key:
                return None
            current_node = current_node.next
        current_node.next = Node(value=key)

    def remove(self, key: int) -> None:
        hashed_key = abs(hash(key))
        bucket_idx = hashed_key % self.hash_table_size
        current_node = self.hash_table[bucket_idx]

        while current_node.next:
            if current_node.next.value == key:
                current_node.next = current_node.next.next
                return None

    def contains(self, key: int) -> bool:
        hashed_key = abs(hash(key))
        bucket_idx = hashed_key % self.hash_table_size
        current_node = self.hash_table[bucket_idx]

        while current_node.next:
            if current_node.next.value == key:
                return True
            current_node = current_node.next
        return False

    def _next_prime(self, n: int) -> int:
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        n = max(n, 2)
        while not is_prime(n):
            n += 1
        return n



# class ListNode:
#     def __init__(self, value=None):
#         self.value = value
#         self.next: ListNode | None = None


# class MyHashSet:
#     def __init__(self):
#         self.hash_table_size = 10007
#         self.hash_table = [ListNode() for i in range(self.hash_table_size)]


#     def add(self, key: int) -> None:
#         cur = self.hash_table[abs(hash(key)) % len(self.hash_table)]
#         while cur.next:
#             if cur.next.value == key:
#                 return None
#             cur = cur.next
#         cur.next = ListNode(key)

#     def remove(self, key: int) -> None:
#         cur = self.hash_table[abs(hash(key)) % len(self.hash_table)]
#         while cur.next:
#             if cur.next.value == key:
#                 cur.next = cur.next.next
#                 return None
#             cur = cur.next

#     def contains(self, key: int) -> bool:
#         cur = self.hash_table[abs(hash(key)) % len(self.hash_table)]
#         while cur.next:
#             if cur.next.value == key:
#                 return True
#         cur = cur.next
#         return False