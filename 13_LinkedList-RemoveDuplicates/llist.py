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
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node


def print_singly_linked_list(llist_head):
    current = llist_head
    while current:
        print(str(current.data))
        current = current.next


def removeDuplicates(llist):
    current = llist
    while current and current.next:
        if current.next.data == current.data:
            current.next = current.next.next
        else:
            current = current.next

    return llist

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = removeDuplicates(llist.head)

        print_singly_linked_list(llist1)

