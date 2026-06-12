class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create array of tuples with both position and speed
        information = []
        for i in range(len(position)):
            information.append((position[i], speed[i]))
        information = sorted(information)
        print(information)
        
        numFleets = 0
        while information:
            numFleets += 1
            # Calculate # of jumps away for current car
            currentPosition, currentSpeed = information.pop()
            currentJumps = (target - currentPosition) / currentSpeed
            print("Current Jumps before entering loop: " + str(currentJumps))
            # Add cars to this fleet if they have less jumps than current car
            while information:
                pos, speed = information[-1]
                jumps = (target - pos) / speed
                print("Jumps: " + str(jumps))
                if jumps <= currentJumps:
                    information.pop()
                else:
                    break

        return numFleets

    

        
        