class TrieNode:
    # Initialize your data structure here.

    def __init__(self):
        self.next = {}
        self.has_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        now = self.root
        for ch in word:
            now = now.next.setdefault(ch, TrieNode())
        if now is not self.root:
            now.has_word = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        now = self.__startswith(word)
        return now is not None and now.has_word

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        return self.__startswith(prefix) is not None

    def __startswith(self, word):
        now = self.root
        for ch in word:
            if ch not in now.next:
                return None
            now = now.next[ch]
        return now

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
