class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def in_order_traversal(self, node, values):
        if node:
            self.in_order_traversal(node.left, values)
            values.append(node.value)
            self.in_order_traversal(node.right, values)
        return values

    def pre_order_traversal(self, node, values):
        if node:
            values.append(node.value)
            self.pre_order_traversal(node.left, values)
            self.pre_order_traversal(node.right, values)
        return values

    def post_order_traversal(self, node, values):
        if node:
            self.post_order_traversal(node.left, values)
            self.post_order_traversal(node.right, values)
            values.append(node.value)
        return values

    def display_in_order(self):
        values = self.in_order_traversal(self.root, [])
        print("In-order Traversal:", values)

    def display_pre_order(self):
        values = self.pre_order_traversal(self.root, [])
        print("Pre-order Traversal:", values)

    def display_post_order(self):
        values = self.post_order_traversal(self.root, [])
        print("Post-order Traversal:", values)

# Example usage
tree = Tree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(18)

tree.display_in_order()  # Output: In-order Traversal: [3, 5, 7, 10, 12, 15, 18]
tree.display_pre_order() # Output: Pre-order Traversal: [10, 5, 3, 7, 15, 12, 18]
tree.display_post_order()# Output: Post-order Traversal: [3, 7, 5, 12, 18, 15, 10]
