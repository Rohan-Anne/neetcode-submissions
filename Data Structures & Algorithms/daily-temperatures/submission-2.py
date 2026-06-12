class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]

        # Create result array
        result = []
        for i in range(len(temperatures)):
            result.append(0)
        
        stack = [(temperatures[0], 0)]
        for i in range(1, len(temperatures)):
            while temperatures[i] > stack[-1][0]:
                day = stack.pop()[1]
                result[day] = i - day
                if not stack:
                    break
            stack.append((temperatures[i], i))
        return result
        
        
        

        
        