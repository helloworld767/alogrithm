import collections

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end = -1
        self.palindrome = []


def addword(word, index, current):
    # current = root
    for i in range(len(word) - 1, -1, -1):
        current = current.children[word[i]]
        if ispalindrome(word[:i]):
            current.palindrome.append(index)
    current.end = index
    current.palindrome.append(index)


def search(words, i, current, res):
    for j in range(len(words[i])):
        if current.end >= 0 and ispalindrome(words[i][j + 1:]) and current.index != i and [i, current.index] not in res:
            res.append([i, current.index])

        current = current.children[words[i][j]]
        if not current:
            return

    for k in current.palindrome:
        if k == i:
            continue
        if [i, k] not in res:
            res.append([i, k])


def ispalindrome(word):
    return word == word[::-1]


words = ["abcd","dcba","lls","s","sssll"]
res = []
root = TrieNode()

for i in range(len(words)):
    addword(words[i], i, root)

for i in range(len(words)):
    search(words, i, root, res)
print(res)
