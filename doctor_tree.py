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
