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


def has_cycle(head):
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast is slow:
            return 1
    return 0

if __name__ == '__main__':

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        extra = SinglyLinkedListNode(-1);
        temp = llist.head;

        for i in range(llist_count):
            if i == index:
                extra = temp

            if i != llist_count-1:
                temp = temp.next

        temp.next = extra

        result = has_cycle(llist.head)

        print(str(int(result)) + '\n')
