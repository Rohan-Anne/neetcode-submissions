
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = set()


class PrefixTree:

    def __init__(self):
        self.tree = TreeNode("")
        self.words = set()
    
    def insert(self, word: str) -> None:
        self.words.add(word)
        currentChildren = self.tree.children
        wordIndex = 0
        while wordIndex < len(word):
            characterPresent = False
            for child in currentChildren:
                if child.value == word[wordIndex]:
                    currentChildren = child.children
                    characterPresent = True
            if not characterPresent:
                node = TreeNode(word[wordIndex])
                currentChildren.add(node)
                currentChildren = node.children
            wordIndex += 1
    def search(self, word: str) -> bool:
        return word in self.words
    def startsWith(self, prefix: str) -> bool:
        print("Start of search")
        currentChildren = self.tree.children
        wordIndex = 0
        while wordIndex < len(prefix):
            characterPresent = False
            #print("Current Children: " + str(currentChildren))
            for child in currentChildren:
                if child.value == prefix[wordIndex]:
                    currentChildren = child.children
                    characterPresent = True
            print("Character Present at Word Index " + str(wordIndex) + ": " + str(characterPresent))
            if not characterPresent:
                print("Search completed")
                return False
            wordIndex += 1
        print("Current children: " + str(currentChildren))
        return True
        
        