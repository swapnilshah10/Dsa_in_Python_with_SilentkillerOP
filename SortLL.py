from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the class structure of the Node class:

    class Node:
        def __init__(self, data):

            self.data = data
            self.next = None

        def __del__(self):
            if(self.next):
                del self.next
                
'''

def getLastNode(head):
    while head and head.next:
        head = head.next
    return head

def partition(head, end, newHead, newEnd):
    pivot = end
    prev = None
    curr = head
    tail = pivot

    while curr != pivot:
        if curr.data < pivot.data:
            if newHead is None:
                newHead = curr
            prev = curr
            curr = curr.next
        else:
            if prev:
                prev.next = curr.next
            temp = curr.next
            curr.next = None
            tail.next = curr
            tail = curr
            curr = temp

    if newHead is None:
        newHead = pivot

    newEnd = tail

    return pivot, newHead, newEnd

def quickSortRec(head, end):
    if not head or head == end:
        return head

    newHead = None
    newEnd = None

    pivot, newHead, newEnd = partition(head, end, newHead, newEnd)

    if newHead != pivot:
        temp = newHead
        while temp.next != pivot:
            temp = temp.next
        temp.next = None
        newHead = quickSortRec(newHead, temp)
        temp = getLastNode(newHead)
        temp.next = pivot

    pivot.next = quickSortRec(pivot.next, newEnd)

    return newHead

def quickSortLL(head):
    end = getLastNode(head)
    return quickSortRec(head, end)
