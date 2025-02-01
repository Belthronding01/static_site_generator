import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_no_children(self):
            with self.assertRaises(ValueError):
                 node = ParentNode("b", [], None)
                 node.to_html()
    def test_correct_input(self):
        node = ParentNode("div", [LeafNode("span", "Text in a span")])
        expected_html = "<div><span>Text in a span</span></div>"
        assert node.to_html() == expected_html
    def test_nested_parent(self):
        child_node = ParentNode("p", [LeafNode(None, "text inside paragraph")])
        parent_node = ParentNode("div", [child_node])
        expected_html = "<div><p>text inside paragraph</p></div>"
        assert parent_node.to_html() == expected_html
    def test_props_addition(self):
        parent_node = ParentNode("div", [LeafNode(None, "child content")], props={"class": "container"})
        expected_html = '<div class="container">child content</div>'
        assert parent_node.to_html() == expected_html