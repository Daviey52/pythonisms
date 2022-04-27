class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next



class LinkedList:

    def __init__(self, collection=None):
        self.head = None
        if collection:

            for item in reversed(collection):
                self.insert(item)

    def insert(self, value):
        self.head = Node(value, self.head)
