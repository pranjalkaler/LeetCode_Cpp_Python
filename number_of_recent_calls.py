class RecentCounter:

    def __init__(self):
        self.counter = 0
        self.queue = []

    def ping(self, t: int) -> int:
        if not self.queue:
            self.queue.append(t)
            return 1
        else:
            self.queue.append(t)
            while self.queue and t - self.queue[0] > 3000:
                self.queue.pop(0)
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)