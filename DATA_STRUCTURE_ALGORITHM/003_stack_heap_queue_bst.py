stack = []

# Push
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)  # Output: [1, 2, 3]

# Pop
print(stack.pop())  # Output: 3
print(stack)        # Output: [1, 2]

# Peek
print(stack[-1])    # Output: 2

# Queue

from collections import deque

queue = deque()

# Enqueue
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  # Output: deque([1, 2, 3])

# Dequeue
print(queue.popleft())  # Output: 1
print(queue)            # Output: deque([2, 3])

# heap

import heapq

heap = []

# Push elemen ke heap
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)
print(heap)  # Output: [5, 10, 20] (Min-Heap)

# Pop elemen terkecil
print(heapq.heappop(heap))  # Output: 5
print(heap)                 # Output: [10, 20]

# hash table

hash_table = {}

# Menambah data
hash_table["nama"] = "Ahmad"
hash_table["umur"] = 25

# Akses data
print(hash_table["nama"])  # Output: Ahmad

# Update data
hash_table["umur"] = 26
print(hash_table)  # Output: {'nama': 'Ahmad', 'umur': 26}

# Hapus data
del hash_table["nama"]
print(hash_table)  # Output: {'umur': 26}

# binary search

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        current = self.root
        while True:
            if value < current.value:
                if not current.left:
                    current.left = Node(value)
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = Node(value)
                    return
                current = current.right

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        print(node.value, end="~>")
        self.inorder(node.right)
    def search(self, node, target):
        if not node:
            print(False)
            return False
        if node.value == target:
            print(True)
            return True
        if target < node.value:
            self.search(node.left, target)
        else:
            self.search(node.right, target)
# Contoh penggunaan
tree = BST()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)

tree.inorder(tree.root)  # Output: 3 5 10 15
print('\n')
tree.search(tree.root, 2)
print(tree.root.right)