from collections import deque
class RecentCounter_list_queue:
    num_ping = []
    def __init__(self):
        self.ping_q = []

        

    def ping(self, t):
        # print('current time', t)
        self.ping_q.append(t)
        # print('when there is a ping', self.ping_q)
        while self.ping_q[0] < t - 3000:
            self.ping_q.pop(0)
            # print('now ping queue', self.ping_q)
        return len(self.ping_q)
        

class RecentCounter_deque_queue:
    def __init__(self):
        self.ping_q =deque()
        

    def ping(self, t):
        # print('current time', t)
        self.ping_q.append(t)

        # print('when there is a ping', self.ping_q)
        while self.ping_q[0] < t - 3000:
            self.ping_q.popleft()
            # print('now ping queue', self.ping_q)
        return len(self.ping_q)
 
# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter_deque_queue()
time = [1, 100, 3001, 3002]
for t in time:
    param_1 = obj.ping(t)
print(param_1)


'''
Write a class RecentCounter to count recent requests.

It has only one method: ping(int t), where t represents some time in milliseconds.

Return the number of pings that have been made from 3000 milliseconds ago until now.

Any ping with time in [t - 3000, t] will count, including the current ping.

It is guaranteed that every call to ping uses a strictly larger value of t than before.

Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
Output: [null,1,2,3,3]
'''
