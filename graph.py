class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data
    def __repr__(self):
        return '<-'+str(self.left)+str(self.data)+str(self.right)+'->'

if __name__ == '__main__':
    a = Node(1)
    a.right=Node(2)
    a.left = Node(3)
    
    print(a)
