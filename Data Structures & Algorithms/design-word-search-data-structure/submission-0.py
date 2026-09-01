class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class WordDictionary:

    def __init__(self):
        self.root = Node()


    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = Node()
            curr = curr.children[letter]
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        
        def recurse(index, node):

            if index == len(word):
                return node.endOfWord
            
            if word[index] != ".":
                if word[index] in node.children:
                    return recurse(index+1, node.children[word[index]])
                else:
                    return False
            
            if word[index] == ".":
                for child in node.children.values():
                    if recurse(index+1, child):
                        return True
                return False

        return recurse(0, self.root)