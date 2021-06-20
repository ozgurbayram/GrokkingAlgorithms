class Node:
    def __init__(self,data=None,next=None) -> None:
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return self.data

class LinkedList:
    def __init__(self,head=None) -> None:
        self.head = head

    def __repr__(self) -> str:
        node = self.head
        nodes =  []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return f'->'.join(nodes)
    
    def reverse_linked_list(self)-> str:
        pass

if __name__ == '__main__':
    a = Node("a node")
    b = Node('b node')
    c = Node('c node')
    a.next= b
    b.next =c

    linked_list = LinkedList() 
    linked_list.head = a

    # insert into head of linked list     
    d= Node('d node')
    d.next = linked_list.head
    linked_list.head = d

    print(linked_list)
