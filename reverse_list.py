import sys
import copy


class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp != None):
            print(temp.data)
            temp = temp.next


def main():
    llist = LinkedList()
    llist.push(43)
    llist.push(4)
    llist.push(75)
    llist.push(22)
    llist.push(2)

    llist.printList()
    llist.reverse()
    print("\nReversed Linked List")
    llist.printList()

if __name__ == '__main__':
    main()