class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = Node()
            curr = curr.children[letter]
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)-1):
            if word[i] not in curr.children:
                return False
            curr = curr.children[word[i]]
        
        if word[len(word)-1] in curr.children:
            curr = curr.children[word[len(word)-1]]
            if curr.endOfWord is True:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            if prefix[i] not in curr.children:
                return False
            curr = curr.children[prefix[i]]
        return True
        
        
        