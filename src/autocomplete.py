from typing import List
from sys import argv


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

    def complete(self, search_term: str) -> List[str]:
        tmp = self.root

        def move_root(pos=0):
            nonlocal tmp

            for char in tmp.next:
                if pos < len(search_term) and char == search_term[pos]:
                    tmp = tmp.next[char]
                    move_root(pos + 1)

        move_root()
        self._traverse(tmp, search_term)
        return self.search_results

    def _traverse(self, node: TrieNode, prefix: str, res='', char=""):
        """Traverses the Trie from a given node to find all completion paths
        """
        res += char

        if node.leaf:
            self.search_results.append(prefix + res)

        for key in node.next:
            self._traverse(node.next[key], prefix, res, key)


if __name__ == '__main__':
    trie = Trie()

    with open('res/dictionary.txt') as file:
        for line in file.readlines():
            trie.insert(line.strip().replace('"', '').replace(',', ''))

    res = trie.complete(argv[1])[:15]
    for r in res:
        print(r)
