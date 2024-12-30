import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    # Write at least two more unit tests for TextNode to check implementation is correct
    # TODO: Test for when url is None
    # TODO: Test for TextNode Objects are not equal

if __name__ == "__main__":
    unittest.main()