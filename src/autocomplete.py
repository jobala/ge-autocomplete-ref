from typing import List


class TrieNode:
    def __init__(self):
        self.next: dict[str, dict] = {}
        self.leaf: bool = False


class Trie:
    def __init__(self):
        self.root: TrieNode = TrieNode()
        self.search_results: List[str] = []

    def insert(self, word: str):
        i = 0
        tmp = self.root

        while i < len(word):
            char = word[i]

            if char not in tmp.next:
                tmp.next[char] = TrieNode()
            tmp = tmp.next[char]

            if i == len(word) - 1:
                tmp.leaf = True
            i += 1

    def autocomplete(self, search_term: str) -> List[str]:
        tmp = self.root

        def move_root(pos=0):
            nonlocal tmp

            for c in tmp.next.keys():
                if pos < len(search_term) and c == search_term[pos]:
                    tmp = tmp.next[c]
                    move_root(pos + 1)

        move_root()
        self._traverse(tmp, search_term)
        return self.search_results

    def _traverse(self, node: TrieNode, prefix: str, res='', char=""):
        res += char

        if node.leaf:
            self.search_results.append(prefix + res)

        for c in node.next.keys():
            self._traverse(node.next[c], prefix, res, c)


if __name__ == '__main__':
    trie = Trie()

    with open('res/dictionary.txt') as file:
        for line in file.readlines():
            trie.insert(line.strip().replace('"', '').replace(',', ''))

    res = trie.autocomplete("/me/c")[:15]
    for r in res:
        print(r)

