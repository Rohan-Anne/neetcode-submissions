class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = [tokens[0]]
        if len(tokens) == 1:
            return int(operands[0])
        for i in range(1, len(tokens)):
            if tokens[i] in set(["+", "-", "*", "/"]):
                second = int(operands.pop())
                first = int(operands.pop())
                if tokens[i] == "+":
                    operands.append(str(first + second))
                elif tokens[i] == "-":
                    operands.append(str(first - second))
                elif tokens[i] == "*":
                    operands.append(str(first * second))
                elif tokens[i] == "/":
                    operands.append(str(int(first / second)))
            else:
                operands.append(tokens[i])

        return int(operands[-1])


        

        