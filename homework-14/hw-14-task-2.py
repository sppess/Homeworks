from random import randint

# Implement 2 classes, the first one is Boss and the second one is Worker
# Worker has a property 'boss' which value must be an instance of Boss
# You can reassign this value, but you should check whether the new value
# is Boss. Each Boss has a list of his own workers. You should implement
# a method which allows you to add workers to a Boss. You're not allowed
# to add instances of Boss class to workers list!
# You can refactor the existing code.
#
# id_ - is just a random unique integer


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def __repr__(self):
        return f"Boss-{self.id}: {self.name}, {self.company}"

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.workers.append(worker)
            worker.company = self.company
        else:
            print("Boss can't be the boss of the boss")

    def fire_an_employee(self, worker):
        if isinstance(worker, Worker) and worker in self.workers:
            worker.company = 'jobless'
            self.workers.remove(worker)
        else:
            print("This person can't be fired")


class Worker:
    def __init__(self, id_, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss

    def __repr__(self):
        return f"[Worker-{self.id}]: {self.name}, {self.company}"

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self._boss.fire_an_employee(self)
            self._boss = new_boss
            self._boss.add_worker(self)
        else:
            print("This person is not a Boss")
