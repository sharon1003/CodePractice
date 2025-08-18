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

def compare_lists1(llist1, llist2):
    list1 = llist1
    stack1 = []
    list2 = llist2
    stack2 = []
    while list1:
        stack1.append(list1.data)
        list1 = list1.next
    while list2:
        stack2.append(list2.data)
        list2 = list2.next

    if len(stack1) != len(stack2):
        return 0
    else:
        while stack1:
            if stack1.pop() == stack2.pop():
                continue
            else:
                return 0
        return 1

def compare_lists(llist1, llist2):
    current1 = llist1
    current2 = llist2
    while current1 and current2:
        if current1.data != current2.data:
            return 0
        current1 = current1.next
        current2 = current2.next
    
    if current1 is not None or current2 is not None:
        return 0
    
    return 1



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

        result = compare_lists(llist1.head, llist2.head)
        print(result)