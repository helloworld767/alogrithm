import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end = False

def add(word, root):
    for i in range(len(word)):
        root = root.children[word[i]]
    root.end = word


def dfs(board, x, y, mask, res, root):
    if root.end:
        res.append(root.end)
        root.end = False
    for letter in root.children:
        for newx, newy in ((x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)):
            if 0 <= newx < len(board) and 0 <= newy < len(board[0]):
                if board[newx][newy] == letter and not mask[newx][newy]:
                    mask[newx][newy] = True
                    dfs(board, newx, newy, mask, res, root.children[letter])
                    mask[newx][newy] = False


root = TrieNode()
mask = [[False for i in range(len(board[0]))] for j in range(len(board))]
for word in words:
    add(word, root)

res = []
for i in range(len(board)):
    for j in range(len(board[0])):
        for letter in root.children:
            if board[i][j] == letter:
                mask[i][j] = True
                dfs(board, i, j, mask, res, root.children[letter])
                mask[i][j] = False
return res