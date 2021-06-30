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
    
    def insert(self,value):
        new_node = Node(value)
        node = self.head
        if node is None:
            self.head = new_node
            return

        while node is not None:
            if node is None:
                node = new_node
                return
            node = node.next
            
if __name__ == '__main__':
    linked_list = LinkedList() 
    linked_list.insert('dsada')
    linked_list.insert("313")
    linked_list.insert('dsadas')
    print(linked_list)