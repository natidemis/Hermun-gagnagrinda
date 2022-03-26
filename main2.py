from LL import LinkedList
from BST import BinarySearchTree
from Treap import Treap
import random
import time
if __name__ == '__main__':
    n = 1000
    iteration = 1
    lltime = ttime = bsttime = 0
    while(lltime + ttime +bsttime  < 10):
        vals = [i for i in range(n)]
        random.shuffle(vals)

        ll = LinkedList()
        bst = BinarySearchTree()
        t = Treap()
        lltime = time.time()
        for val in vals:
            ll.insert(LinkedList.Node(val = val))
        lltime = time.time() - lltime
        ttime = time.time()
        for val in vals:
            t.head = t.insert(Treap.Node(val=val,priority=Treap.gen_priority()),t.head)
        ttime = time.time() - ttime
        bsttime = time.time()
        for val in vals:
            bst.insert(child = BinarySearchTree.Node(val = val))
        bsttime = time.time() - bsttime
        n *= 10

        print(f"Iteration: {iteration} - n = {n} --",f"Linked list time: {lltime}", f"Treap time: {ttime}", f"BST time: {bsttime}")
        iteration += 1