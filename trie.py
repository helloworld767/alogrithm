import collections
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

print('##########')
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        #print(self.root)
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            print(current,'?????')
            if current is None:
                print('???')
                return False
        return current.is_word

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True
su = Trie()
su.insert('leetcode')
su.insert('letsgo')
res = su.search('leetcodea')
print(res)
