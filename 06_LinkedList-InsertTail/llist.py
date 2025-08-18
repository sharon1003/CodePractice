#!/bin/python3

import math
import os
import random
import re
import sys

# single node
class SinglyLinkedListNode():
    def __init__(self, data):
        self.data = data
        self.next = None

# pointer for linked list
class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

def insertNodeAtTail(llist_head, data):
    # create a new node
    new_node = SinglyLinkedListNode(data)
    # insert the node to tail
    if llist_head == None:
        llist.head = llist.tail = new_node
    else:
        llist.tail.next = new_node
        llist.tail = new_node
    return llist.head
    

def print_singly_linked_list(head, sep, fptr):
    current = head
    while not current.next:
        fptr.write(str(current.data))
        current = current.next
        if current is not None:
            fptr.write(sep)


if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head)