import unittest
from examples.redblack.redblack import RedBlackTree


class TestRedBlackTree(unittest.TestCase):

    def setUp(self):
        self.tree = RedBlackTree()

    def test_insert(self):
        # Insert values into the Red-Black Tree
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)
        
        # Test that the values are inserted correctly
        self.assertIsNotNone(self.tree.search(10))
        self.assertIsNotNone(self.tree.search(20))
        self.assertIsNotNone(self.tree.search(30))

    def test_insert_and_inorder_traversal(self):
        # Insert values and verify the inorder traversal
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)
        
        # Capture the output of inorder traversal
        with self.assertLogs(level='INFO') as log:
            self.tree.inorder(self.tree.root)
        self.assertIn("10 20 30", log.output[0])  # Inorder should print 10, 20, 30

    def test_delete(self):
        # Insert and delete a node
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)
        
        self.assertIsNotNone(self.tree.search(20))  # 20 should exist
        self.tree.delete(20)
        self.assertIsNone(self.tree.search(20))  # 20 should be deleted

    def test_delete_root(self):
        # Test deleting the root node
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)
        
        self.assertIsNotNone(self.tree.search(10))  # 10 should exist
        self.tree.delete(10)
        self.assertIsNone(self.tree.search(10))  # 10 should be deleted

    def test_preorder_traversal(self):
        # Insert values and verify preorder traversal
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)

        with self.assertLogs(level='INFO') as log:
            self.tree.preorder(self.tree.root)
        self.assertIn("10 20 30", log.output[0])  # Preorder should print 10, 20, 30

    def test_postorder_traversal(self):
        # Insert values and verify postorder traversal
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)

        with self.assertLogs(level='INFO') as log:
            self.tree.postorder(self.tree.root)
        self.assertIn("30 20 10", log.output[0])  # Postorder should print 30, 20, 10

    def test_level_order_traversal(self):
        # Insert values and verify level-order traversal
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)

        with self.assertLogs(level='INFO') as log:
            self.tree.level_order()
        self.assertIn("10 20 30", log.output[0])  # Level order should print 10, 20, 30

    def test_empty_tree_search(self):
        # Search in an empty tree
        self.assertIsNone(self.tree.search(10))  # Tree is empty, should return None

    def test_insert_and_delete_multiple_nodes(self):
        # Insert multiple nodes, delete some, and check consistency
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)
        self.tree.insert(40)
        
        self.assertIsNotNone(self.tree.search(10))  # Should exist
        self.assertIsNotNone(self.tree.search(20))  # Should exist
        self.assertIsNotNone(self.tree.search(30))  # Should exist
        self.assertIsNotNone(self.tree.search(40))  # Should exist
        
        # Delete some nodes
        self.tree.delete(20)
        self.tree.delete(40)
        
        self.assertIsNone(self.tree.search(20))  # Should be deleted
        self.assertIsNone(self.tree.search(40))  # Should be deleted
        self.assertIsNotNone(self.tree.search(10))  # Should still exist
        self.assertIsNotNone(self.tree.search(30))  # Should still exist


if __name__ == "__main__":
    unittest.main()
