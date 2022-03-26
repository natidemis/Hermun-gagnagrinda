

import random
class BinarySearchTree:
    class Node:
        def __init__(self, val: int,left: 'BinarySearchTree.Node' = None, right: 'BinarySearchTree.Node' = None) -> 'BinarySearchTree.Node':
            self.left: 'BinarySearchTree.Node' = left
            self.right: 'BinarySearchTree.Node' = right
            self.val: int = val

    
    def __init__(self) -> 'BinarySearchTree':
        self.head = None

    def _insert(self, node: 'BinarySearchTree.Node', curr: 'BinarySearchTree.Node') -> None:
        if curr is None:
            return
        if(node.val < curr.val):
            if curr.left is not None:
                self._insert(node,curr.left)
            else:
                curr.left = node
        else:
            if curr.right is not None:
                self._insert(node,curr.right)
            else:
                curr.right = node
        return 
    def insert(self, child: 'BinarySearchTree.Node') -> None:
        traverse = self.head
        if self.head == None:
            self.head = child
            return
        self._insert(child,traverse)
        
    def print_tree(self, traverse = None) -> None:
        
        traverse = traverse if traverse is not None else self.head 
        if self.head is traverse:
            print("-------------printing BinarySearchTree--------")
            print("head: ",traverse.val)
        if(traverse is None):
            return
        if traverse.left is not None:
            print(f"left-child of {traverse.val}: ",traverse.left.val)
            self.print_tree(traverse.left)
        if traverse.right is not None:
            print(f"right-child of {traverse.val}: ",traverse.right.val)
            self.print_tree(traverse.right)


    def search(self,root: Node, key: int):
        if root is None:
            return False
        if root.val == key:
            return True
        if key < root.val:
            return self.search(root.left, key)
        return self.search(root.right, key)

if __name__ == '__main__':
    vals = [i for i in range(10)]
    random.shuffle(vals)
    bst = BinarySearchTree()
    for i in range(0,len(vals)):
        print("insertting: ",vals[i])
        bst.insert(child = BinarySearchTree.Node(val = vals[i]))
    print(bst.search(bst.head,5))
    bst.print_tree()
    bst.rotate_left(bst.head)
    bst.print_tree()
