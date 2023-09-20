from os import *
from sys import *
from collections import *
from math import *

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        


def evenOddLevelDifference(root): 
    if not root : return 0
    even = 0
    odd = 0
    q = [(root , 0)]
    while q:
        root , lvl = q.pop(0)
        if root.left: q.append((root.left , lvl+1))
        if root.right : q.append((root.right , lvl+1))
        if lvl%2: odd += root.data
        else : even+= root.data
    return abs(even - odd)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main 
t=int(input())
while t>0:
    levelOrder = [int(i) for i in input().strip().split()]
    root = buildLevelTree(levelOrder)
    print(evenOddLevelDifference(root))
    t-=1



