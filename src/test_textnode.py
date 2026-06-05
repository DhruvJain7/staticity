import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.bold, "https//www.bootdev.com")
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertNotEqual(node, node2)

    def test_diff(self):
        node = TextNode("This is a text node", TextType.italic)
        node2 = TextNode("This is a text node", TextType.code)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
