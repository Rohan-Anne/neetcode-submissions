class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        currentString = ""
        def traversal(i, openBrackets, closedBrackets):
            nonlocal currentString
            # Cut off paths that are invalid
            if closedBrackets > openBrackets:
                return
            # If valid and reached length, add to combinations
            if i >= 2 * n:
                combinations.append(currentString)
                return
            if openBrackets - closedBrackets >= (2 * n) - len(currentString):
                # Forced to just append closed brackets
                currentString += ")"
                traversal(i + 1, openBrackets, closedBrackets + 1)
            else:
                # Normal backtracking algorithm
                oldString = currentString
                currentString += "("
                traversal(i + 1, openBrackets + 1, closedBrackets)
                currentString = oldString
                currentString += ")"
                traversal(i + 1, openBrackets, closedBrackets + 1)
             
        traversal(0, 0, 0)
        return combinations

        