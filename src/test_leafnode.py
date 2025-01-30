import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leafnode(self):
        node = LeafNode("p", "Text")
        assert node.to_html() == "<p>Text</p>"
    def test_not_eq(self):
        node = LeafNode("asd", "ddas", "asdasdasd")
        node2 = LeafNode("asd", "ddas", "asdasdasd")
        self.assertNotEqual(node, node2)

