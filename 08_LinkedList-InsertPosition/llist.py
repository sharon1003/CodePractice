#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode():
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_node(self, data):
        new_node = SinglyLinkedListNode(data)
        if self.head is None:
            self.head = self.tail =  new_node
        else:
            self.tail.next = new_node
        self.tail = new_node


def insertNodeAtPosition(llist, data, position):
    # Write your code here
    new_node = SinglyLinkedListNode(data)
    if position == 0:
        new_node.next = llist 
        return llist
    
    current = llist
    for i in range(position-1):
        current = current.next
    new_node.next = current.next
    current.next = new_node

    return llist

def print_singly_linked_list(llist_head):
    current = llist_head
    while current:
        print(str(current.data))
        current = current.next


if __name__ == '__main__':

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)
    # print_singly_linked_list(llist.head)
    
    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head)
