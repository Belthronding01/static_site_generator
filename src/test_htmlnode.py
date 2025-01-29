import unittest 
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_none(self):
        html_node = HTMLNode()
        self.assertEqual(html_node.props_to_html(), "")
    def test_not_eq(self):
        html_node = HTMLNode("asd", "ddas", "asdasd", "asdasdasd")
        html_node2 = HTMLNode("asd", "ddas", "asdasasd", "asdasdasd")
        self.assertNotEqual(html_node, html_node2)
    def test_props_to_html_one_prop(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')
    
    def test_props_to_html_multiple_props(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank"
        })
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    
