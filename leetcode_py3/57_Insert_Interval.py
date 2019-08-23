class Solution:
    def insert(self, intervals, newInterval):
        
        new_intervals = []
        index = len(intervals)
        
        if len(intervals) == 0 or not intervals:
            new_intervals.append(newInterval)
            return new_intervals
        
        
        for i, interval in enumerate(intervals):
            # print(interval[0])
            if interval[0] > newInterval[0]:
                index = i
                break
        
        intervals.insert(index, newInterval)
        print(intervals)
            
        for interval in intervals:
            if not new_intervals or new_intervals[-1][-1] < interval[0]:
                new_intervals.append(interval)
            else:
                print(interval[-1])
                new_intervals[-1][-1] = max(new_intervals[-1][-1], interval[-1])
                
        return new_intervals


if __name__ == '__main__':
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    print(Solution().insert(intervals, newInterval))

''' 
Given a set of non-overlapping intervals, insert a new interval into the
intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their
start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5] Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]] Explanation: Because the new interval [4,8]
overlaps with [3,5],[6,7],[8,10]. 
'''
