from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("Must have a tag")
        self.tag = tag
        if children is None:
            raise ValueError("Must have a child")
        if isinstance(children, list) is False or len(children) == 0:
            raise ValueError("Children must be a non-empty list")
        self.children = children
        self.props = props
    def to_html(self):
        result = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            result += child.to_html()
        result += f"</{self.tag}>"
        return result
        
