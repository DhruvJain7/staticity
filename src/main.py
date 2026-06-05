from textnode import TextNode, TextType


def main():
    demo = TextNode("This is some anchor text", TextType.link, "https://www.boot.dev")
    print(demo)


main()
