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


def mergeLists1(head1, head2):
    current1 = head1
    current2 = head2
    llist3 = SinglyLinkedList()
    idx = 0    
    while current1 is not None and current2 is not None:
        idx += 1 
        if current1.data <= current2.data:
            llist3.insert_node(current1.data)
            current1 = current1.next
        else:
            llist3.insert_node(current2.data)
            current2 = current2.next

    while current1 is not None:
        llist3.insert_node(current1.data)
        current1 = current1.next

    while current2 is not None:
        llist3.insert_node(current2.data)
        current2 = current2.next
    return llist3.head

def mergeLists(head1, head2):
    dummy = SinglyLinkedListNode(0)
    tail = dummy
    while head1 and head2:
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next
    tail.next = head1 if head1 else head2
    return dummy.next


if __name__ == '__main__':

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3)