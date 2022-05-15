class Counter:

    def __init__(self):
        self.id = 1

    def create_new(self):
        self.id += 1
        return self.id


id_creator = Counter()
