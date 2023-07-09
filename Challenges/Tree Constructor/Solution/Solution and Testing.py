def TreeConstructor(strArr):
    nodeArr = [list(map(int, a)) for a in [s.strip("()").split(",") for s in strArr]]
    treeNode = []
    setNode = set()
    
    for node in nodeArr:
        setNode.add(node[0])
        setNode.add(node[1])
    
    setNode = sorted(list(setNode))
    
    for val in setNode:
        treeNode.append(Node(val))
    
    for node in nodeArr:
        child = findNode(node[0], treeNode)
        parent = findNode(node[1], treeNode)
        child.parent = parent
        
        if parent.value < child.value:
            parent.right = child
        elif parent.value > child.value:
            parent.left = child
        elif parent.right is not None and parent.left is not None:
            return "false"
    
    root = None
    rootCnt = 0
    
    for node in treeNode:
        if node.parent is None:
            root = node
            rootCnt += 1
    
    if rootCnt >= 2:
        return "false"
    
    traverseNode = []
    
    def traverse(node):
        if node is None:
            return
        traverseNode.append(node.value)
        traverse(node.left)
        traverse(node.right)
    
    traverse(root)
    
    traverseNode.sort()
    setNode.sort()
    
    return "true" if traverseNode == setNode else "false"

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def findNode(value, nodes):
    for node in nodes:
        if node.value == value:
            return node
    return None

# Example usage
print(TreeConstructor(["(1,2)", "(2,4)", "(7,2)"]))  # Output: true
print(TreeConstructor(["(1,2)", "(3,2)", "(2,12)", "(5,2)"]))  # Output: false
