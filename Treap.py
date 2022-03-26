import random
from BST import BinarySearchTree
class Treap(BinarySearchTree):
    gen_priority = lambda : random.randint(0,1000)
    class Node:
        def __init__(self, val: int, priority: int,left: 'Treap.Node' = None, right: 'Treap.Node' = None):
            self.left: 'Treap.Node' = left
            self.right: 'Treap.Node' = right
            self.val: int = val
            self.priority: int = priority

    def __init__(self) -> None:
        self.head = None

    def rotate_left(self, root: Node) -> None: 
        if root.right is not None:
            r = root.right
            rl = root.right.left
            r.left = root
            root.right = rl
            if root == self.head:
                self.head = r
        return r
    def rotate_right(self, root: Node) -> None:
        l = root.left
        lr = root.left.right 
        l.right = root
        root.left = lr
        if root is self.head:
            self.head = l
        return l
    def search(self,root: Node, key: int) -> bool:
        if root is None:
            return False
        if root.val == key:
            new_pr = Treap.gen_priority()
            root.priority = new_pr if new_pr < root.priority else root.priority
            return True
        if key < root.val:
            return self.search(root.left,key)
        return self.search(root.right,key)

    def delete(self,root: Node,key: int) -> None:
        if root is None:
            return None
        if key < root.val:
            root.left = self.delete(root.left,key)
        elif key > root.val:
            root.right = self.delete(root.right,key)
        else:
            if root.left is None and root.right is None:
                root = None
            elif root.left and root.right:
                if root.left.priority < root.right.priority:
                    root = self.rotate_left(root)
                    root.left = self.delete(root.left,key)
                else:
                    root = self.rotate_right(root)
                    root.right = self.delete(root.right,key)
            else:
                root = root.left or root.right

    def insert(self, to_insert: Node,root: Node = None):
        if root is None:
            root = to_insert
            return root

        if to_insert.val < root.val:
            root.left = self.insert(to_insert,root.left)

            if root.left and root.left.priority > root.priority:
                root = self.rotate_right(root)
        else:
            root.right = self.insert(to_insert,root.right)
            if root.right and root.right.priority > root.priority:
                root = self.rotate_left(root)
        return root

    def print_tree(self, traverse = None) -> None:
        
        traverse = traverse if traverse is not None else self.head 
        if self.head is traverse:
            print("-------------printing Treap--------")
            print(f"head: {traverse.val,traverse.priority}",)
        if(traverse is None):
            return
        if traverse.left is not None:
            print(f"left-child of {traverse.val,traverse.priority}: {traverse.left.val,traverse.left.priority}")
            self.print_tree(traverse.left)
        if traverse.right is not None:
            print(f"right-child of {traverse.val,traverse.priority}: {traverse.right.val, traverse.right.priority}")
            self.print_tree(traverse.right)

if __name__ == '__main__':
    vals = [i for i in range(10)]
    random.shuffle(vals)
    t = Treap()
    for i in range(len(vals)):
        print("inserting: ",vals[i])
        rndm = random.randint(0,1000)
        t.head = t.insert(Treap.Node(val=vals[i],priority=Treap.gen_priority()),t.head)
    t.print_tree()
