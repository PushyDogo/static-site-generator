import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, "www.f95zone.com")
        node2 = TextNode("This is a text node", TextType.NORMAL_TEXT)
        self.assertNotEqual(node, node2)

    def test_bad(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT, None)
        node2 = TextNode("This is a text node", TextType.NORMAL_TEXT)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()