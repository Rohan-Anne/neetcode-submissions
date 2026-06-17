class TimeMap:

    def __init__(self):
        self.internalDict = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.internalDict.keys():
            self.internalDict[key] = [(value, timestamp)]
        else:
            self.internalDict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        print("Get() call starting.")
        if key not in self.internalDict.keys():
            return ""
        
        values = self.internalDict[key]
        print(values)
        l = 0
        r = len(values) - 1
        currentValue = ""
        while l < r:
            print("Left: " + str(l))
            print("Right: " + str(r))
            m = int((l + r) / 2)
            if values[m][1] == timestamp:
                currentValue = values[m][0]
                break
            elif values[m][1] > timestamp:
                r = m - 1
            else:
                currentValue = values[m][0]
                l = m + 1

        if l == r and values[l][1] <= timestamp:
            currentValue = values[l][0]
        return currentValue


        
