import time
import random

# Singly Linked List Node and Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_index(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return True
        current = self.head
        prev = None
        count = 0
        while current and count < index:
            prev = current
            current = current.next
            count += 1
        if count == index:
            prev.next = new_node
            new_node.next = current
            return True
        else:
            return False
    
    def search(self, val):
        current = self.head
        while current:
            if current.data == val:
                return True
            current = current.next
        return False
    
    def delete_value(self, val):
        current = self.head
        prev = None
        while current:
            if current.data == val:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False


# Doubly Linked List Node and Class
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_index(self, data, index):
        new_node = DNode(data)
        if index == 0:
            if self.head:
                new_node.next = self.head
                self.head.prev = new_node
            self.head = new_node
            return True
        current = self.head
        count = 0
        while current and count < index:
            prev = current
            current = current.next
            count += 1
        if count == index:
            new_node.next = current
            new_node.prev = prev
            prev.next = new_node
            if current:
                current.prev = new_node
            return True
        return False

    def search(self, val):
        current = self.head
        while current:
            if current.data == val:
                return True
            current = current.next
        return False

    def delete_value(self, val):
        current = self.head
        while current:
            if current.data == val:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return True
            current = current.next
        return False

# Timer utility
def time_operation(func, *args, repeats=5):
    times = []
    for _ in range(repeats):
        start = time.time()
        func(*args)
        end = time.time()
        times.append(end - start)
    avg = sum(times) / repeats
    return avg

# Test functions for each DS
def test_list_insert(lst, data, index):
    lst.insert(index, data)

def test_list_search(lst, val):
    return val in lst

def test_list_delete(lst, val):
    try:
        lst.remove(val)
    except ValueError:
        pass

def test_sll_insert(sll, data, index):
    sll.insert_at_index(data, index)

def test_sll_search(sll, val):
    return sll.search(val)

def test_sll_delete(sll, val):
    sll.delete_value(val)

def test_dll_insert(dll, data, index):
    dll.insert_at_index(data, index)

def test_dll_search(dll, val):
    return dll.search(val)

def test_dll_delete(dll, val):
    dll.delete_value(val)

def build_sll(data_list):
    sll = SinglyLinkedList()
    for i, val in enumerate(data_list):
        sll.insert_at_index(val, i)
    return sll

def build_dll(data_list):
    dll = DoublyLinkedList()
    for i, val in enumerate(data_list):
        dll.insert_at_index(val, i)
    return dll

#Testing

def main():
    size = 50000
    data = [random.randint(1, 10**6) for _ in range(size)]
    mid_index = size // 2
    search_val = data[mid_index]

    print(f"Testing with {size} elements, search and delete value: {search_val}")

    ### Python list tests
    pylist = data.copy()
    
    insert_time = time_operation(test_list_insert, pylist, -1, 0)
    search_time = time_operation(test_list_search, pylist, search_val)
    delete_time = time_operation(test_list_delete, pylist, search_val)

    print(f"Python list insert at beginning: {insert_time:.6f} s")
    print(f"Python list search: {search_time:.6f} s")
    print(f"Python list delete: {delete_time:.6f} s")

    ### Singly Linked List tests
    sll = build_sll(data)
    
    insert_time = time_operation(test_sll_insert, sll, -1, 0)
    search_time = time_operation(test_sll_search, sll, search_val)
    delete_time = time_operation(test_sll_delete, sll, search_val)

    print(f"Singly Linked List insert at beginning: {insert_time:.6f} s")
    print(f"Singly Linked List search: {search_time:.6f} s")
    print(f"Singly Linked List delete: {delete_time:.6f} s")

    ### Doubly Linked List tests
    dll = build_dll(data)
    
    insert_time = time_operation(test_dll_insert, dll, -1, 0)
    search_time = time_operation(test_dll_search, dll, search_val)
    delete_time = time_operation(test_dll_delete, dll, search_val)

    print(f"Doubly Linked List insert at beginning: {insert_time:.6f} s")
    print(f"Doubly Linked List search: {search_time:.6f} s")
    print(f"Doubly Linked List delete: {delete_time:.6f} s")

if __name__ == "__main__":
    main()
