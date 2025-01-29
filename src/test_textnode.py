import unittest
from textnode import TextNode, TextType

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

if __name__ == "__main__":
	unittest.main()
