class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
    
    def searchHelper(self, root, word):
        cur = root
        for i in range(len(word)):
            if word[i] != ".":
                if word[i] not in cur.children:
                    return False
                cur = cur.children[word[i]]
            else:
                for childIndex in cur.children.keys():
                    if self.searchHelper(cur.children[childIndex], word[i + 1:]):
                        return True
                return False
        return cur.endOfWord
    
    def search(self, word: str) -> bool:
        return self.searchHelper(self.root, word)
        
                
                    
            
        
