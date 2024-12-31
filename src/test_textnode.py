import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.BOLD) 
        node4 = TextNode("This is a text node", TextType.BOLD, url=None) 
        self.assertEqual(node, node2)
        self.assertEqual(node3, node4)
        self.assertEqual(node.url, None)

    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, node2.url)

        node3 = TextNode("This is text node", TextType.BOLD, url="https://google.com")
        node4 = TextNode("This is text node", TextType.BOLD, url="https://google.com")
        self.assertEqual(node3.url, node4.url)
        
    

    

if __name__ == "__main__":
    unittest.main()