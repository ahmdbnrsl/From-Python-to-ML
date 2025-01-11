class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node # data, next
            return
        current = self.head # data: data, next: None
        
        while current.next:
            current = current.next
        current.next = new_node # data, next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
linked_list = LinkedList()
linked_list.append(2)
linked_list.append(35)
linked_list.append(1)
linked_list.append(7)
print(f'''Node pertama ({id(linked_list.head)})
Data ({linked_list.head.data})\nPointer ({id(linked_list.head.next)})
Node kedua ({id(linked_list.head.next)})
Data ({linked_list.head.next.data})\nPointer ({id(linked_list.head.next.next)})
Node ketiga ({id(linked_list.head.next.next)})
Data ({linked_list.head.next.next.data})\nPointer ({id(linked_list.head.next.next.next)})
Node keempat ({id(linked_list.head.next)})
Data ({linked_list.head.next.next.next.data})\nPointer ({linked_list.head.next.next.next.next})''')
linked_list.display()