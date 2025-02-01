import unittest
from textnode import *
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)
	def test_url_eq(self):
		node = TextNode("asds", TextType.CODE, "https://boot.dev")
		node2 = TextNode("asdsasda", TextType.ITALIC, "https://boot.dev")
		self.assertEqual(node.url, node2.url)
	def test_url_none(self):
		node = TextNode("asds", TextType.CODE)
		node2 = TextNode("asds", TextType.CODE, None)
		self.assertEqual(node, node2)
	def test_texttype_eq(self):
		node = TextNode("aass", TextType.CODE)
		node2 = TextNode("asds", TextType.CODE, "https://boot.dev")
		self.assertEqual(node.text_type, node2.text_type)
	def test_text_not_eq(self):
		node = TextNode("asdssd", TextType.CODE, "https://boot.dev")
		node2 = TextNode("asds", TextType.CODE, "https://boot.dev")
		self.assertNotEqual(node.text, node2.text)
	def test_text_node_to_html_node(self):
		# Test plain text
		node = TextNode("Hello, world!", TextType.TEXT)
		html_node = text_node_to_html_node(node)
		assert html_node.tag is None
		assert html_node.value == "Hello, world!"
		assert html_node.props is None
	def test_text_node_to_html_node_case_bold(self):
		# Test bold text
		node = TextNode("Bold text", TextType.BOLD)
		html_node = text_node_to_html_node(node)
		assert html_node.tag == "b"
		assert html_node.value == "Bold text"
		assert html_node.props is None
	def test_text_node_to_html_node_case_italic(self):
		# Test italic text
		node = TextNode("Italic text", TextType.ITALIC)
		html_node = text_node_to_html_node(node)
		assert html_node.tag == "i"
		assert html_node.value == "Italic text"
		assert html_node.props is None
	def test_text_node_to_html_node_case_code(self):
		# Test code text
		node = TextNode("Code", TextType.CODE)
		html_node = text_node_to_html_node(node)
		assert html_node.tag == "code"
		assert html_node.value == "Code"
		assert html_node.props is None
	def test_text_node_to_html_node_case_link(self):
		# Test link
		node = TextNode("Click", TextType.LINK, "https://boot.dev")
		html_node = text_node_to_html_node(node)
		assert html_node.tag == "a"
		assert html_node.value == "Click"
		assert html_node.props == {"href":"https://boot.dev"}
	def test_text_node_to_html_node_case_image(self):
		# Test image
		node = TextNode("Image text", TextType.IMAGE, "https://boot.dev/image.png")
		html_node = text_node_to_html_node(node)
		assert html_node.tag == "img"
		assert html_node.value == ""
		assert html_node.props == {"src": "https://boot.dev/image.png", "alt":"Image text"}
if __name__ == "__main__":
	unittest.main()
