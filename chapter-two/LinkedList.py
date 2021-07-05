class Node:
    def __init__(self,data=None,next=None) -> None:
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self,head=None) -> None:
        self.head = head

    def __repr__(self):
        node = self.head
        nodes =  []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
    
        return f'->'.join(nodes)
    
    def __len__(self)->int:
        node = self.head 
        count = 0
        while node:
            count +=1
            node = node.next
        return count 

    def insert_first(self,value):
        new_node = Node(value)
        # Swap head with new node
        new_node.next = self.head
        self.head=new_node
    
    def insert(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return  
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node
    
    def insert_value_list(self,value_list):
        for value in value_list:
            self.insert(value)

    def find(self,value):
        node = self.head
        count = 0
        while node is not None:
            if node.data==value:
                return 'found at {}'.format(count)
            count +=1
            node = node.next
        return 'not found'
    
    def remove_at_end(self):
        node = self.head 
        while node.next:
            if node.next.next== None:
                node.next = None
                return 'end' 
            node = node.next
        return 'out of while' 
    
    #Todo complete
    def find_and_remove(self,value):
        pass
        
if __name__ == '__main__':
    linked_list = LinkedList() 
    
    linked_list.insert('1')
    linked_list.insert('2')
    linked_list.insert('3')


    values = [321,31,41,53]
    linked_list.insert_value_list(values)
    linked_list.remove_at_end()
    
    linked_list.find_and_remove(321)
    # Print's
    print(linked_list.__len__())
    print(linked_list)
    print(linked_list.find('2'))
