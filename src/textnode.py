from enum import Enum
from leafnode import LeafNode

__all__ = ["TextNode", "TextType", "text_node_to_html_node"]

def text_node_to_html_node(text_node):
		match (text_node.text_type):
			case TextType.TEXT:
				return LeafNode(None, text_node.text, None)
			case TextType.BOLD:
				return LeafNode("b", text_node.text, None)
			case TextType.ITALIC:
				return LeafNode("i", text_node.text, None)
			case TextType.CODE:
				return LeafNode("code", text_node.text, None)
			case TextType.LINK:
				return LeafNode("a", text_node.text, {"href":text_node.url})
			case TextType.IMAGE:
				node = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
				return node
			case _:
				raise ValueError(f"Invalid text type {text_node.text_type}")

class TextType(Enum):
	BOLD = "bold"
	TEXT = "text"
	ITALIC = "italic"
	CODE = "code"
	LINK = "link"
	IMAGE = "image"

class TextNode():
	def __init__(self, text, text_type, url=None):
		self.text = text
		self.text_type = text_type
		self.url = url
	
	def __eq__(self, value):
		if self.text == value.text and self.text_type == value.text_type and self.url == value.url:
			return True
		return False
	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type.value}, {self.url})"