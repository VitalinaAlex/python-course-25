class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def search(root, data):
    # Base Cases: root is null or data 
    # is present at root
    if root is None or root.data == data:
        return root
    
    # data is greater than root's data
    if root.data < data:
        return search(root.right, data)
    
    # data is smaller than root's data
    return search(root.left, data)

def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print("    " * level + str(node.data))
        print_tree(node.left, level + 1)

def insert(root, data):
    if root is None:
        return TreeNode(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

values = [50, 30, 70, 20, 40, 60, 80]
root = None
for v in values:
    root = insert(root, v)

print("root.right.left.data:", root.right.left.data)
print("root.right.right.data:", root.right.right.data)

print(search(root, 50).data)  # корінь
print(search(root, 30).data)  # ліва гілка
print(search(root, 70).data)  # права гілка
print(search(root, 85))

print_tree(root)