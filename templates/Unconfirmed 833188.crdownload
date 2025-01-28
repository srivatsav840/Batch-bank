# # class Node:
# #     def __init__(self, data):
# #         self.data = data
# #         self.left = None
# #         self.right = None
# #
# #
# #     def insert(self, num):
# #         if self is None:
# #             return Node(num)
# #         elif num < self.data:
# #             self.left = self.left.insert(num)
# #         else:
# #             self.right = self.right.insert(num)
# #         return self
# #
# #     def inorder(self):
# #         if self is None:
# #             return
# #         if self.left:
# #             self.left.inorder()
# #         print(self.data, end=" ")
# #         if self.right:
# #             self.right.inorder()
# #
# #     def postorder(self):
# #         if self is None:
# #             return
# #         if self.left:
# #             self.left.postorder()
# #         if self.right:
# #             self.right.postorder()
# #         print(self.data, end=" ")
# #
# #
# # # Example usage:
# # if __name__ == "__main__":
# #     # Read input from STDIN
# #     elements = list(map(int, input().split()))  # Assuming input is space-separated integers
# #
# #     # Construct the BST
# #     root = None
# #     for num in elements:
# #         if root is None:
# #             root = Node(num)
# #         else:
# #             root.insert(num)
# #
# #     # Perform inorder traversal and print the result
# #     if root:
# #         print("Inorder Traversal:")
# #         root.inorder()
# #
# #     # Perform postorder traversal and print the result
# #     if root:
# #         print("\nPostorder Traversal:")
# #         root.postorder()
#
#
# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
#
# def insert(root, key):
#     if root is None:
#         return Node(key)
#     if key < root.key:
#         root.left = insert(root.left, key)
#     elif key > root.key:
#         root.right = insert(root.right, key)
#     return root
#
# def is_complete(root):
#     if root is None:
#         return True
#
#     queue = [root]
#     reached_last_level = False
#
#     while queue:
#         node = queue.pop(0)
#
#         # If we have reached the last level and encounter a node with children,
#         # or if we encounter a node with no left child but a right child,
#         # then the tree is not a complete binary tree
#         if reached_last_level and (node.left or node.right) or (node.left is None and node.right):
#             return False
#
#         # If the current node has a left child but no right child,
#         # or if we have reached the last level,
#         # mark reached_last_level as True
#         if node.left and node.right is None or reached_last_level:
#             reached_last_level = True
#
#         # Enqueue the children of the current node
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
#
#     return True
#
# if __name__ == "__main__":
#     T = int(input())  # Number of test cases
#     for _ in range(T):
#         N = int(input())  # Number of nodes in the BST
#         values = list(map(int, input().split()))  # Values of the nodes
#
#         # Construct the binary search tree
#         root = None
#         for value in values:
#             root = insert(root, value)
#
#         # Check if the binary search tree is a complete binary tree
#         if is_complete(root):
#             print("Yes")
#         else:
#             print("No")

# li=[1,2,4,56,23,34]
# x=sorted(li)
# print(x)
