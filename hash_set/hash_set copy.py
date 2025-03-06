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
            if current_node.value == key:
                return None
            current_node = current_node.next
        current_node.next = Node(value=key)





        # # case: Adding the first key to an existing empty node, encountered at the first time
        # if current_node.value is None and current_node.next is None:
        #     current_node.value = key
        #     return None

        # while current_node.value != key:
        #     if current_node.next:
        #         current_node = current_node.next
        #     else:
        #         break
        # else:
        #     # print(f"\n****debug: collision detected for key: {key}****")
        #     return None

        # assert current_node.next is None
        # current_node.next = Node(value=key)

    def remove(self, key: int) -> None:
        hashed_key = abs(hash(key))
        bucket_idx = hashed_key % self.hash_table_size
        current_node = self.hash_table[bucket_idx]

        while current_node.next:
            if current_node.next.value == key:
                current_node.next = current_node.next.next
                return None



        # # check if there is a next node
        # if previous_node.next:
        #     # case: There are multiple nodes i.e. linked list and the first node is to be deleted and other nodes are present
        #     # we need to take care of connecting the next node with the hash table index
        #     if previous_node.value == key:
        #         previous_node.value = None
        #         self.hash_table[bucket_idx] = previous_node.next
        #     else:
        #         # case: There are multiple nodes i.e. linked list and the middle node is to be deleted
        #         current_node = previous_node.next
        #         while current_node.value != key and current_node.next:
        #             previous_node = current_node
        #             current_node = current_node.next

        #         if current_node.value == key:
        #             current_node.value = None
        #             if current_node.next:
        #                 # we need to take care of connecting the prev and next nodes
        #                 previous_node.next = current_node.next
        #             else:
        #                 # case: There are multiple nodes i.e. linked list and the last node is to be deleted
        #                 # only prev node's next is made to point to None
        #                 previous_node.next = None

        #         else:
        #             # print(
        #             #     "debug Error: Error! Code executed a logically unreachable code.\nFlawed logic detected"
        #             # )
        #             pass

        # elif previous_node.value == key:
        #     previous_node.value = None
        # else:
        #     # print(f"debug Error: Table is empty for key: {key}")
        #     pass


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


# # MyHashSet object will be instantiated and called as such:
# # obj = MyHashSet()
# # obj.add(key)
# # obj.remove(key)
# # param_3 = obj.contains(key)


# class MyHashSet:

#     def __init__(self):
#         self.hash_table_size = 1000001
#         self.hash_table = [False for _ in range(self.hash_table_size)]


#     def add(self, key: int) -> None:
#         self.hash_table[key] = True


#     def remove(self, key: int) -> None:
#         self.hash_table[key] = False


#     def contains(self, key: int) -> bool:
#         return self.hash_table[key]


# class ListNode:
#     def __init__(self, value=None):
#         self.value = value
#         self.next: Node | None = None


# class MyHashSet:
#     def __init__(self):
#         self.set = [ListNode(-1) for i in range(10**4)]

#     def add(self, key: int) -> None:
#         cur = self.set[key % len(self.set)]
#         while cur.next:
#             if cur.next.key == key:
#                 return None
#             cur = cur.next
#         cur.next = ListNode(key)

#     def remove(self, key: int) -> None:
#         cur = self.set[key % len(self.set)]
#         while cur.next:
#             if cur.next.key == key:
#                 cur.next = cur.next.next
#                 return None
#             cur = cur.next

#     def contains(self, key: int) -> bool:
#         cur = self.set[key % len(self.set)]
#         while cur.next:
#             if cur.next.key == key:
#                 return True
#         cur = cur.next
#         return False