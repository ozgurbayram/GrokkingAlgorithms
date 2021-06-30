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
    
    def insert_first(self,value):
        new_node = Node(value)
        # Swap head with new node
        new_node.next = self.head
        self.head=new_node

    def insert(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node
            
if __name__ == '__main__':
    linked_list = LinkedList() 
    linked_list.insert_first('first')
    linked_list.insert('dsada')
    linked_list.insert_first('ese')
    linked_list.insert('dsada')
    linked_list.insert('dsada')
    print(linked_list)