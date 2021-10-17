#This problem was asked by Google.

#Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

#For example, given the following Node class

#class Node: def __init__(self, val, left=None, right=None): self.val = val self.left = left self.right = right 

#The following test should pass:

#node = Node('root', Node('left', Node('left.left')), Node('right')) assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def serialize(Node):
    com = []
    
    def incorporate(Node, com):
        com.append(str(Node.val))

        if Node.left:
            com.append('L')
            incorporate(Node.left, com)

        if Node.right:
            com.append('R')
            incorporate(Node.right, com)
        
        com.append('U')
        return ''.join(com)

    incorporate(Node, com)
    com.pop()
    return ''.join(com)

def deserialize(string):
    chars = ''
    nodes = []
    next_child = None
    for i, char in enumerate(string):
        if char not in ('L','R','U'):
            chars += char #sumamos el 'val' del node a serializar al string chars
        else:
            if not nodes: #root node
                nodes.append(Node(int(chars)))
            elif next_child == 'left':
                nodes[-1].left = Node(int(chars)) #utilizamos el índice -1 para ir connectando los nodes al final por orden.
                nodes.append(nodes[-1].left)
            elif next_child == 'right':
                nodes[-1].right = Node(int(chars))
                nodes.append(nodes[-1].right)
            elif next_child =='up':
                nodes.pop()
            if char == 'L':
                next_child = 'left'
            elif char == 'R':
                next_child = 'right'
            elif char == 'U':
                next_child = 'up'
            
            chars = ''
    return nodes[0] #al final quedaría un objeto al estilo [node [node.right [node.left [node.left...] ...]]]

    
nd = Node(1)
nd.left = Node(3)
nd.left.left = Node(6)
nd.right = Node(4)
nd.right.left = Node(7)
nd.right.right = Node(8)
a = serialize(nd)
b = deserialize(a)
print(a)

"""
    1
   / \
  3   4
 /   / \
6   7   8
"""
