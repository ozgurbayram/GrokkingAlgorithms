class Node:
    def __init__(self,data=None,next=None,prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        return self.data

class DoublyLinkedList:
    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        pass

    def insert():
        pass

if __name__ == '__main__':
    # Create 2 node
    first_node = Node("first node")
    second_node = Node("second node")
    
    first_node.next = second_node
    second_node.prev = first_node

