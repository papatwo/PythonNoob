class Solution:
    def minMeetingRooms(self, intervals):
        starts = sorted([interval[0] for interval in intervals])
        ends = sorted([interval[1] for interval in intervals])

        print(starts)
        print(ends)

        min_room = 0
        count = 0
        s, e = 0, 0

        while s < len(starts):
            if starts[s] < ends[e]:
                count += 1
                min_room = max(min_room, count)
                s += 1
            else:
                count -= 1
                e += 1

        return min_room

if __name__ == '__main__':
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(Solution().minMeetingRooms(intervals))

