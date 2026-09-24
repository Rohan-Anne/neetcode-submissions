class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        mapping = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'], "4": ['g', 'h', 'i'], "5": ['j', 'k', 'l'], "6": ['m', 'n', 'o'], "7": ['p', 'q', 'r', 's'], "8": ['t', 'u', 'v'], "9" : ['w', 'x', 'y', 'z']}
        combinations = []
        currentString = ""
        def traversal(i):
            nonlocal currentString
            if i >= len(digits):
                combinations.append(currentString)
                return
            currentChars = mapping[digits[i]]
            for char in currentChars:
                oldString = currentString
                currentString += char
                traversal(i + 1)
                currentString = oldString
        traversal(0)
        return combinations

        