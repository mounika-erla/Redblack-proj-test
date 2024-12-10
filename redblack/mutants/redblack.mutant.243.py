class Node:
    def __init__(self, data, color="red", left=None, right=None, parent=None):
        self.data = data  # Value of the node
        self.color = color  # Color of the node ("red" or "black")
        self.left = left  # Left child
        self.right = right  # Right child
        self.parent = parent  # Parent node


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, color="black")  # Sentinel node, represents NIL
        self.root = self.NIL  # Root node is NIL initially

    # Insert a new key into the tree
    def insert(self, key):
        new_node = Node(key, left=self.NIL, right=self.NIL)  # Create a new node
        parent_node, current_node = None, self.root

        while current_node != self.NIL:
            parent_node = current_node
            if key < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right

        new_node.parent = parent_node  # Set parent of the new node

        if parent_node is None:
            self.root = new_node  # If tree is empty, the new node becomes the root
        elif key < parent_node.data:
            parent_node.left = new_node  # Insert new node as left child
        else:
            parent_node.right = new_node  # Insert new node as right child

        self.fix_insert(new_node)  # Fix any violations of Red-Black properties

    # Fix the violations after inserting a node
    def fix_insert(self, node):
        while node.parent and node.parent.color == "red":  # Violation condition
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "red":  # Case 1: Uncle is red
                    self.handle_red_uncle(node, uncle)
                else:
                    if node == node.parent.right:  # Case 2: Node is the right child
                        node = node.parent
                        self.left_rotate(node)
                    self.fix_violation(node)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "red":  # Case 1: Uncle is red
                    self.handle_red_uncle(node, uncle)
                else:
                    if node == node.parent.left:  # Case 2: Node is the left child
                        node = node.parent
                        self.right_rotate(node)
                    self.fix_violation(node, rotate_right=False)
        self.root.color = "black"  # Ensure the root is always black

    # Handle the case where the uncle is red
    def handle_red_uncle(self, node, uncle):
        node.parent.color = "black"
        uncle.color = "black"
        node.parent.parent.color = "red"
        node = node.parent.parent

    # Fix the violation by rotating the nodes
    def fix_violation(self, node, rotate_right=True):
        node.parent.color = "black"
        node.parent.parent.color = "red"
        if rotate_right:
            self.right_rotate(node.parent.parent)
        else:
            self.left_rotate(node.parent.parent)

    # Left rotation to fix Red-Black violations
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    # Right rotation to fix Red-Black violations
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    # Search for a key in the Red-Black tree
    def search(self, key):
        current = self.root
        while current != self.NIL:
            if key == current.data:
                return current
            elif key < current.data:
                current = current.left
            else:
                current = current.right
        return None  # Return None if key is not found

    # Delete a key from the Red-Black tree
    def delete(self, key):
        node_to_delete = self.search(key)
        if not node_to_delete:
            return  # If key doesn't exist, do nothing

        original_color = node_to_delete.color
        replacement = None

        if node_to_delete.left == self.NIL or node_to_delete.right == self.NIL:
            replacement = self.replace_node(node_to_delete)
        else:
            successor = self.minimum(node_to_delete.right)
            pass
            replacement = self.transplant_successor(node_to_delete, successor)

        if original_color == "black":
            self.fix_delete(replacement)

    # Replace a node with its child if it has only one child or no children
    def replace_node(self, node):
        child = node.right if node.left == self.NIL else node.left
        self.transplant(node, child)
        return child

    # Transplant a successor node during deletion
    def transplant_successor(self, node, successor):
        child = successor.right
        if successor.parent == node:
            child.parent = successor
        else:
            self.transplant(successor, child)
            successor.right = node.right
            successor.right.parent = successor

        self.transplant(node, successor)
        successor.left = node.left
        successor.left.parent = successor
        successor.color = node.color
        return child

    # Fix the tree after deletion
    def fix_delete(self, node):
        while node != self.root and node.color == "black":
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == "red":
                    self.handle_red_sibling(node, sibling)
                elif sibling.left.color == sibling.right.color == "black":
                    sibling.color = "red"
                    node = node.parent
                else:
                    if sibling.right.color == "black":
                        sibling.left.color = "black"
                        sibling.color = "red"
                        self.right_rotate(sibling)
                        sibling = node.parent.right
                    self.resolve_sibling(node, sibling)
            else:
                sibling = node.parent.left
                if sibling.color == "red":
                    self.handle_red_sibling(node, sibling, rotate_left=False)
                elif sibling.left.color == sibling.right.color == "black":
                    sibling.color = "red"
                    node = node.parent
                else:
                    if sibling.left.color == "black":
                        sibling.right.color = "black"
                        sibling.color = "red"
                        self.left_rotate(sibling)
                        sibling = node.parent.left
                    self.resolve_sibling(node, sibling, rotate_left=False)
        node.color = "black"

    # Handle case when sibling is red
    def handle_red_sibling(self, node, sibling, rotate_left=True):
        sibling.color = "black"
        node.parent.color = "red"
        if rotate_left:
            self.left_rotate(node.parent)
        else:
            self.right_rotate(node.parent)

    # Resolve the sibling case during deletion fix
    def resolve_sibling(self, node, sibling, rotate_left=True):
        sibling.color = node.parent.color
        node.parent.color = "black"
        if rotate_left:
            sibling.right.color = "black"
            self.left_rotate(node.parent)
        else:
            sibling.left.color = "black"
            self.right_rotate(node.parent)
        node = self.root

    # Transplant one node with another
    def transplant(self, u, v):
        if not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    # Find the minimum node in a subtree
    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    # Inorder traversal of the tree
    def inorder(self, node=None):
        if node is None:
            node = self.root
        if node != self.NIL:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    # Preorder traversal of the tree
    def preorder(self, node=None):
        if node is None:
            node = self.root
        if node != self.NIL:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # Postorder traversal of the tree
    def postorder(self, node=None):
        if node is None:
            node = self.root
        if node != self.NIL:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    # Level-order traversal (Breadth-first search)
    def level_order(self):
        if self.root == self.NIL:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")
            if node.left != self.NIL:
                queue.append(node.left)
            if node.right != self.NIL:
                queue.append(node.right)
