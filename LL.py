import random



class LinkedList:
    class Node:
        def __init__(self, val: int,next: 'LinkedList.Node' = None):
            self.next : 'LinkedList.Node' = next
            self.val: int = val
    def __init__(self) -> 'LinkedList':
        self.head: 'LinkedList.Node' = None


    def insert(self, node: 'LinkedList.Node') -> None:
        node.next = self.head
        self.head = node


    def print_list(self) -> None:
        traverse = self.head 
        while(traverse is not None):
            print(f"{traverse.val} -> ",end="")
            traverse = traverse.next
    def search(self, key: int) -> Node or None:
        traverse = self.head
        if traverse.val == key:
            return self.head
        result = None
        while(traverse.next is not None):
            if traverse.next.val == key:
                result = traverse
                break
            traverse = traverse.next
        if result is not None:
            while(traverse.next is not None):
                traverse = traverse.next
        
            traverse.next = self.head
            self.head = result.next
            result.next = None
            return self.head
        return None
if __name__ == '__main__':
    vals = [i for i in range(10)]
    random.shuffle(vals)
    ll = LinkedList()
    for val in vals:
        print("Inserting: ", val)
        ll.insert(LinkedList.Node(val = val))

    ll.print_list()
    ll.search(4)
    print()
    ll.print_list()