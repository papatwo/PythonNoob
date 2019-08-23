
class Solution(object):
    def canAttendMeetings(self, v):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        # v.sort(key = lambda val: val.start)
        # return not any(v[i].start < v[i-1].end for i in range(1,len(v)))

        v.sort(key=lambda v: v[0])
        for i in range(1, len(v)):
            if v[i][0] < v[i-1][-1]:
                return False
            else:
                return True


if __name__ == '__main__':
    v = [[0, 30],[5, 10],[15, 20]]
    print(Solution().canAttendMeetings(v))


''' 
Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all
meetings.

For example, Given [[0, 30],[5, 10],[15, 20]], return false. 
'''
