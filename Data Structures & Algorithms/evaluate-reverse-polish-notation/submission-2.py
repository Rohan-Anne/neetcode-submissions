class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                operands.append(operands.pop() + operands.pop())
            elif tokens[i] == "-":
                firstNumber = operands.pop()
                secondNumber = operands.pop()
                operands.append(secondNumber - firstNumber)
            elif tokens[i] == "*":
                operands.append(operands.pop() * operands.pop())
            elif tokens[i] == "/":
                firstNumber = operands.pop()
                secondNumber = operands.pop()
                operands.append(int(secondNumber / firstNumber))
            else:
                operands.append(int(tokens[i]))

        return operands.pop()
            
        
        