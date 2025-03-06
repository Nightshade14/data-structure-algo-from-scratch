class Node:

    def __init__(self, value=None):
        self.value = value
        self.next: Node = None


class MyHashSet:

    def __init__(self):
        # print(sys.maxsize)
        # print(abs(hash(str(sys.maxsize))))
        # print(abs(hash(str(sys.maxsize)))%(10**4))
        # print(9223372036854775807%(10**4))

        # prime numbered buckets further reduce collisions
        # self.hash_table_size = self._next_prime(n=10**4) # 10007
        self.hash_table_size = 10007
        self.hash_table = [Node() for _ in range(self.hash_table_size)]     


    def add(self, key: int) -> None:
        hashed_key = abs(hash(key))
        bucket_idx = hashed_key % self.hash_table_size
        current_node = self.hash_table[bucket_idx]

        while current_node.next:
            if current_node.value == key:
                print(f"debug: collision detected for key: {key}")
                return
            current_node = current_node.next

        current_node.next = Node(key)


    def remove(self, key: int) -> None:
        hashed_key = abs(hash(key))
        bucket_idx = hashed_key % self.hash_table_size
        previous_node = self.hash_table[bucket_idx]
        # check if there is a next node
        if previous_node.next:
            # case: There are multiple nodes i.e. linked list and the first node is to be deleted
            if previous_node.value == key:
                previous_node.value = None
                self.hash_table[bucket_idx] = previous_node.next
            else:
                # case: There are multiple nodes i.e. linked list and the middle node is to be deleted
                # we need to take care of connecting the prev and next nodes
                current_node = previous_node.next
                while current_node.next:
                    if current_node.value == key:
                        current_node.value = None
                        previous_node.next = current_node.next
                        break
                    
                    previous_node = current_node
                    current_node = current_node.next
                
                # case: There are multiple nodes i.e. linked list and the last node is to be deleted
                # only prev node's next is made to point to None
                if current_node.next == None and current_node.value == key:
                    current_node.value = None
                    previous_node.next = None
                else:
                    print(f"debug Error: Error! Code executed a logically unreachable code.\nFlawed logic detected")

        elif previous_node.value == key:
            previous_node.value = None
        else:
            print(f"debug Error: Error! Code executed a logically unreachable code.\nFlawed logic detected")

            
        

    def contains(self, key: int) -> bool:
        hashed_key = abs(hash(key))
        bucket_idx = hashed_key % self.hash_table_size
        current_node = self.hash_table[bucket_idx]
        while current_node.next:
            if current_node.value == key:
                return True
            current_node.next = current_node
        
        if current_node.value == key:
            return True
        else:
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