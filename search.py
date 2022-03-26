from LL import LinkedList
from BST import BinarySearchTree
from Treap import Treap
import random
import time
if __name__ == '__main__':


    ns = [25000,125000] #veljum tvö n
    ms = [1,25,50,75,100]

    iteration = 1

    llsearch = {f"{n}-{m}": [] for m in ms for n in ns}
    tsearch = {f"{n}-{m}": [] for m in ms for n in ns}
    bstsearch = {f"{n}-{m}": [] for m in ms for n in ns}

    for n in ns:
        for m in ms:
            vals = [i for i in range(n)]
            random.shuffle(vals)

            search_values = list(list(range(n))*m)
            random.shuffle(search_values)

            ll = LinkedList()
            bst = BinarySearchTree()
            t = Treap()

            #--------------Linked list----------
            for val in vals:
                ll.insert(LinkedList.Node(val = val))

            lltime = time.time()
            for sv in search_values:
                ll.search(sv)
            llsearch[f"{n}-{m}"].append(time.time() - lltime)

            #----------treap-------------
            for val in vals:
                t.head = t.insert(Treap.Node(val=val,priority=Treap.gen_priority()),t.head)

            ttime = time.time()
            for sv in search_values:
                t.search(t.head,sv)
            tsearch[f"{n}-{m}"].append(time.time() - ttime)

            for val in vals:
                bst.insert(child = BinarySearchTree.Node(val = val))

            bsttime = time.time()
            for sv in search_values:
                bst.search(bst.head,sv)
            bstsearch[f"{n}-{m}"].append(time.time() - bsttime)
            print(f"{n}-{m} on iteration {iteration}")
            iteration += 1
