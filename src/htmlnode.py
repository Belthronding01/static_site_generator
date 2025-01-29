class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not implemented yet")
    def props_to_html(self):
        if self.props is None:
            return ""
        result = ""
        for key,value in self.props.items():
            result += f' {key}="{value}"'
        return result
    def __repr__(self):
        return f"tag: {self.tag}\n value: {self.value}\n children: {self.children}\n props: {self.props}\n"
    