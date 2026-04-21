class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Assemble car data structure that includes both position and speed
        cars = []
        numFleets = 0
        stack = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        # Sort cars in descending order of positi o
        cars.sort(reverse=True)
        print(cars)

        # Go through cars array and check for fleets
        for i in range(len(cars)):
            time = (target - cars[i][0]) / cars[i][1]
            if not stack:
                stack.append(time)
            elif time <= stack[0]:
                stack.append(time)
            else:
                stack = []
                stack.append(time)
                numFleets += 1
            print(stack)
        if stack:
            numFleets += 1
        return numFleets
                


        


        


        
        