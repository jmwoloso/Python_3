#!/usr/bin/python
#
# Test Suite For foresty.py
#    test_forestry.py
#
# Created by: Jason M Wolosonovich
#    6/09/2015
#
# Lesson 11 - Exercise 1
"""
test_forestry.py: Test suite for forestry.py

@author: Jason M. Wolosonovich
"""
import unittest
from forestry import Lumberjack, Tree, start_logging

sizes = (("S", 1), ("M", 2), ("L", 3), ("XL", 4), ("XXL", 5))

class TestTree(unittest.TestCase):
    
    def test_lumber(self):
        for code, boards in sizes:
            tree = Tree(code)
            self.assertEqual(boards, tree.get_boards())
            
    def test_string(self):
        tree = Tree("L")
        self.assertEqual(str(tree), "Tree: Size L")
        
    def test_exceptions(self):
        self.assertRaises(ValueError, Tree, "parrot")
        self.assertRaises(TypeError, Lumberjack().cut_down_tree)
        
        
class TestLumberjack(unittest.TestCase):
    
    def test_lumberjack(self):
        for code, boards in sizes:
            tree = Tree(code)
            graham = Lumberjack()
            self.assertIsNone(graham.tree)
            graham.tree = tree
            brds = graham.cut_down_tree()
            self.assertIsNone(graham.tree)
            self.assertEqual(boards, brds)
            

if __name__ == "__main__":
    start_logging(level="info")
    unittest.main()