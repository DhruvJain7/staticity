import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_no_props(self):
        node = HTMLNode("")
        self.assertEqual(node.props_to_html(), "")

    def test_single_props(self):
        node = HTMLNode("h1", "Hello", "h2", {"value": "heat"})
        self.assertEqual(node.props_to_html(), ' value="heat"')

    def test_more_props(self):
        node = HTMLNode("h1", "Hello", "h2", {"value": "heat", "cricket": "rcb"})
        self.assertEqual(node.props_to_html(), ' value="heat" cricket="rcb"')


if __name__ == "__main__":
    unittest.main()
