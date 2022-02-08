#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'removeDuplicates' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def removeDuplicates(llist):
    # Write your code here
    prevn = llist
    if prevn.next == None:
        return llist
    else:
        nnext = prevn.next
    # print(prevn.data,nnext.data)
            
        while nnext.next:
            if prevn.data == nnext.data:
                prevn.next = prevn.next.next
                print(prevn.data)
                nnext = prevn.next
                print(prevn.data,nnext.data)
            
            else:
                print("-----------")
                prevn = nnext
                nnext = nnext.next
                print(prevn.data,nnext.data)
        if prevn.data == nnext.data:
            prevn.next = None      
    return llist
            

if __name__ == '__main__':