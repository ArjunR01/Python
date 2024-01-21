class BTreeNode:
    def __init__(self, leaf=True):
        self.keys = []
        self.children = []
        self.leaf = leaf

def insert_btree(root, value):
    if not root:
        return BTreeNode(leaf=True, keys=[value])

    if root.leaf:
        # Insert into a leaf node
        root.keys.append(value)
        root.keys.sort()
        if len(root.keys) > 5:
            return split_leaf(root)
    else:
        # Insert into an internal node
        i = len(root.keys) - 1
        while i >= 0 and value < root.keys[i]:
            i -= 1
        i += 1

        child = root.children[i]
        if len(child.keys) == 5:
            new_child = insert_btree(split_leaf(child), value)
            root.keys.insert(i, new_child.keys[0])
            root.children.insert(i, new_child)
        else:
            insert_btree(child, value)

    return root

def split_leaf(leaf):
    split_index = len(leaf.keys) // 2
    new_leaf = BTreeNode(leaf.leaf)
    new_leaf.keys = leaf.keys[split_index:]
    leaf.keys = leaf.keys[:split_index]

    if not leaf.leaf:
        new_leaf.children = leaf.children[split_index:]
        leaf.children = leaf.children[:split_index]

    return new_leaf

# Given elements
elements = [10, 20, 35, 40, 50, 65, 70, 80, 90, 100, 110, 120, 130, 140, 160, 180, 190, 240, 260]

# Construct a B-tree of order 5
root = None

for value in elements:
    root = insert_btree(root,value)
