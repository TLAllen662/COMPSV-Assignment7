class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def _find(self, name):
        stack = [self.root] if self.root else []
        while stack:
            node = stack.pop()
            if node.name == name:
                return node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return None

    def insert(self, parent_name, employee_name, side):
        """Add employee_name under parent_name on 'left' or 'right'.

        Returns True on success, False if the parent isn't found, the side
        is invalid, or that side is already occupied.
        """
        if side not in ("left", "right"):
            return False
        parent = self._find(parent_name)
        if parent is None or getattr(parent, side) is not None:
            return False
        setattr(parent, side, DoctorNode(employee_name))
        return True

    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


# Test your DoctorTree and DoctorNode classes here
if __name__ == "__main__":
    # Empty tree
    empty = DoctorTree()
    assert empty.root is None
    assert empty.insert("Anyone", "Dr. X", "left") is False
    assert empty.preorder(empty.root) == []
    assert empty.inorder(empty.root) == []
    assert empty.postorder(empty.root) == []

    # Build the example tree
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")
    assert tree.insert("Dr. Croft", "Dr. Goldsmith", "right") is True
    assert tree.insert("Dr. Croft", "Dr. Phan", "left") is True
    assert tree.insert("Dr. Phan", "Dr. Carson", "right") is True
    assert tree.insert("Dr. Phan", "Dr. Morgan", "left") is True

    # Traversals
    assert tree.preorder(tree.root) == ["Dr. Croft", "Dr. Phan", "Dr. Morgan", "Dr. Carson", "Dr. Goldsmith"]
    assert tree.inorder(tree.root) == ["Dr. Morgan", "Dr. Phan", "Dr. Carson", "Dr. Croft", "Dr. Goldsmith"]
    assert tree.postorder(tree.root) == ["Dr. Morgan", "Dr. Carson", "Dr. Phan", "Dr. Goldsmith", "Dr. Croft"]

    # Traversal of a subtree and a leaf
    assert tree.preorder(tree.root.left) == ["Dr. Phan", "Dr. Morgan", "Dr. Carson"]
    assert tree.inorder(tree.root.left.left) == ["Dr. Morgan"]

    # Edge cases: all must fail and leave the tree unchanged
    before = tree.preorder(tree.root)
    assert tree.insert("Dr. Nobody", "Dr. X", "left") is False    # missing parent
    assert tree.insert("Dr. Croft", "Dr. X", "up") is False       # invalid side
    assert tree.insert("Dr. Croft", "Dr. X", "Left") is False     # case-sensitive side
    assert tree.insert("Dr. Croft", "Dr. X", "") is False         # empty side
    assert tree.insert("Dr. Croft", "Dr. X", "left") is False     # occupied side
    assert tree.insert("Dr. Phan", "Dr. X", "right") is False     # occupied side
    assert tree.preorder(tree.root) == before

    # Insert deep in the tree
    assert tree.insert("Dr. Morgan", "Dr. Lee", "left") is True
    assert tree.preorder(tree.root) == ["Dr. Croft", "Dr. Phan", "Dr. Morgan", "Dr. Lee", "Dr. Carson", "Dr. Goldsmith"]

    # Single-node tree
    solo = DoctorTree()
    solo.root = DoctorNode("Dr. Solo")
    assert solo.preorder(solo.root) == solo.inorder(solo.root) == solo.postorder(solo.root) == ["Dr. Solo"]

    print("All DoctorTree tests passed.")
