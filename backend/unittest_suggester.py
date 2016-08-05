import unittest
from suggester import Suggester

class TestStringMethods(unittest.TestCase):

    def test_empty(self):
        sug = Suggester()
        sug.update_trie([])
        self.assertEqual(sug.search_prefix('a'), [])

    def test_normal(self):
        sug = Suggester()
        sug.update_trie(['denmark', 'sweden', 'norway', 'swizerland', 'united kingdom'])
        self.assertEqual(set(sug.search_prefix('s')), set(['sweden', 'swizerland']))

    def test_too_long(self):
        sug = Suggester()
        sug.update_trie(['denmark', 'sweden', 'norway', 'swizerland', 'united kingdom'])
        self.assertEqual(sug.search_prefix('swizerland federation'), [])

if __name__ == '__main__':
    unittest.main()