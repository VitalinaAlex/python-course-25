"""Програма мінімум:
Розширити структуру, яку побудували на уроці, можливістю вставки дерева в наявне дерево 
та видалення піддерева з дерева, що існує.
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


def search(root, key):
    if root is None:
        return None
    if root.key == key:
        print(f'Found the key - {key}')
        return root

    
    direction = "rigt"
    if root.key < key:
        print(f"[search] Compared {key} with {root.key}; going {direction}")
        return search(root.right, key)
    direction = "left"
    print(f"[search] Compared {key} with {root.key}; going {direction}")
    return search(root.left, key)

def insert_tree(root, key, tree, direction):
    """
    key - значення вузла, куди вставляємо
    tree - корінь піддерева, що ми вставляємо
    direction - 'left' або 'right'
    """
    node = search(root, key)
    if node is None:
        print("[insert] Node for insertion not found")
        return

    if direction == "left":
        node.left = tree
    else:
        node.right = tree

def delete_tree(root, key):
    if root is None:
        return None

    if root.left and root.left.key == key:
        print(f"[delete] Delete subtree with root {key} (left)")
        root.left = None
        return

    if root.right and root.right.key == key:
        print(f"[delete] Delete subtree with root {key} (right)")
        root.right = None
        return

    delete_tree(root.left, key)
    delete_tree(root.right, key)

def print_result(root, key, msg):
    result = search(root, key)
    print(msg if not result else f"Found: {result.key}")

def repr_tree(node, level=0):
    if node is not None:
        repr_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.key)
        repr_tree(node.left, level + 1)
root = None
for v in [24, 37, 10, 3, 6, 14, 48,8, 20]:
        root = insert(root, v)
print("Initial tree:")
repr_tree(root)

print_result(root, 3, "Not found tree to delete")
delete_tree(root, 3)
print_result(root, 3, "Not found tree - deleted")
repr_tree(root)

import pytest

@pytest.fixture
def sample_tree():
    # дерево
    root = None
    for v in [8, 3, 10, 1, 6, 14]:
        root = insert(root, v)
    return root


def test_search_found(sample_tree):
    result = search(sample_tree, 6)
    assert result is not None
    assert result.key == 6


def test_search_not_found(sample_tree):
    result = search(sample_tree, 99)
    assert result is None


def test_insert(sample_tree):
    root = insert(sample_tree, 7)
    result = search(root, 7)
    assert result is not None
    assert result.key == 7


def test_insert_tree(sample_tree):
    subtree = Node(20)
    subtree.left = Node(15)
    subtree.right = Node(30)

    insert_tree(sample_tree, 6, subtree, "right")

    #(root.right.key == 20)
    node = search(sample_tree, 6)
    assert node.right is subtree


def test_delete_tree(sample_tree):
    delete_tree(sample_tree, 3)
    result = search(sample_tree, 3)
    assert result is None

if __name__ == "__main__":
    pytest.main([__file__, "-v"])