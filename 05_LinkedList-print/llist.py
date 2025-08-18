#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_node(self, num):
        new_node = SinglyLinkedListNode(num)
        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node
        
        self.tail = new_node


def printLinkedList(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next
    

if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)