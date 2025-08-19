#!/bin/python3

import math
import os
import random
import re
import sys

class DoubleLinkedListNode():
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_node(self, data):
        new_node = DoubleLinkedListNode(data)
        
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.pre = self.tail
        self.tail = new_node


def print_doubly_linked_list(node):
    print("result") 
    while node:
        print(str(node.data))
        node = node.next


def sortedInsert(llist, data):
    # Write your code here
    new_node = DoubleLinkedListNode(data)
    head = llist
    while head:
        if new_node.data < head.data:
            new_node.next = head
            head.prev = new_node
            return new_node
        elif head.next is None and new_node.data > head.data:
            new_node.prev = head
            head.next = new_node
            break
        elif new_node.data >= head.data and new_node.data <= head.next.data:
            new_node.next = head.next
            new_node.prev = head.prev
            head.next = new_node
            head.next.prev = new_node
            break

        head = head.next
    return llist


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1)