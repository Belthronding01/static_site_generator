from textnode import TextNode, TextType

def main():
    text_node = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
    print(text_node.__repr__())

if __name__ == "__main__":
    main()

