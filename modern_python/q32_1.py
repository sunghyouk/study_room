class Queue(object):
    def __init__(self):
        self.queue = []

    def get_queue_elements(self):
        return self.queue.copy()

    def size(self):
        return len(self.queue)

    def add_one(self, item):
        return self.queue.append(item)

    def add_many(self, item, n):
        for i in range(n):
            self.queue.append(item)

    def remove_one(self):
        return self.queue.pop(0)

    def remove_many(self, n):
        for i in range(n):
            self.queue.pop(0)

    def prettyprints(self):
        for thing in self.queue[::-1]:
            print("|_ ", thing, " _|")
