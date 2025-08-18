#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertNodeAtHead function below.

#
# For your reference:
class SinglyLinkedNode():
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
      
# Write your code here
def insertNodeAtHead(head, data):
    new_node = SinglyLinkedNode(data)
    if head is None:
        head = new_node
    else:
        new_node.next = head
        head = new_node
    return head

def print_singly_linked_list(node):
    while node:
        print(str(node.data))
        node = node.next

if __name__ == '__main__':

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head
    
    print_singly_linked_list(llist.head)