"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervalTuples = []
        for i in range(len(intervals)):
            intervalTuples.append((intervals[i].start, intervals[i].end))
        intervalTuples = sorted(intervalTuples)
        for i in range(0, len(intervalTuples) - 1):
            if intervalTuples[i][1] > intervalTuples[i + 1][0]:
                return False
        return True


        
