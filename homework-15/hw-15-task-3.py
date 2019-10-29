# Add a new method to our Worker-Boss program to the Boss class.
# This method is called (dump_workers). It must take all workers from
# workers list and output them into a .csv file (just the way we did it)
#
# Extra point for doing it using built-in csv library
# Extra point for doing it using 3rd party library pandas

from abc import ABC


class Person(ABC):
    def __init__(self, id_, name, company):
        self.id = id_
        self.name = name
        self.company = company


class Boss(Person):
    def __init__(self, id_, name, company):
        super(Boss, self).__init__(id_, name, company)
        self.workers = []

    def __repr__(self):
        return f"Boss-{self.id}: {self.name}, {self.company}"

    def dump_workers(self):
        with open('files/new_worker_file.csv', 'r') as file:
            if 'id_,name,company,boss_id' not in (file.read()):
                with open('files/new_worker_file.csv', 'w') as file:
                    file.write('id_,name,company,boss_id\n')

        with open('files/new_worker_file.csv', 'a') as file:
            for worker in self.workers:
                file.write(f"{worker.id},"
                           f"{worker.name},"
                           f"{worker.company},"
                           f"{worker._boss.id}\n")


class Worker(Person):
    def __init__(self, id_, name, company, boss):
        super(Worker, self).__init__(id_, name, company)
        self._boss = boss
        self._boss.workers.append(self)

    def __repr__(self):
        return f"[Worker-{self.id}]: {self.name}, {self.company}, " \
                f"my boss is {self._boss.name}"

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self._boss.workers.remove(self)
            self._boss = new_boss
            self._boss.workers.append(self)
        else:
            print("This person is not a Boss")


bosses = []
workers = []

with open('bosses.csv', 'r') as file:
    readfile = file.readlines()
    for boss in readfile[1:]:
        id_, name, company = boss.split(',')
        bosses.append(Boss(id_, name, company))

with open('workers.csv', 'r') as file1:
    for worker in file1.readlines()[1:]:
        id_, name, company, boss_id = worker.split(',')
        workers.append(Worker(id_, name, company, bosses[int(boss_id)]))

print(bosses[1])
bosses[3].dump_workers()
bosses[2].dump_workers()
