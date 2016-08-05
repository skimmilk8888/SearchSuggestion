from pytrie import StringTrie

class Suggester(object):
    def __init__(self):
        self.trie = None

    def update_trie(self, word_list):
        self.trie = StringTrie()
        for word in word_list:
            word = word.lower()
            self.trie[word] = word

    def search_prefix(self, prefix):
        return self.trie.values(prefix=prefix)
