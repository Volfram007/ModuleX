class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance > self.full_distance:  # ошибка ">=" ➤ верное ">"
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers


# r1 = Runner('Усэйн', 10)
# r2 = Runner('Андрей', 9)
# r3 = Runner('Ник', 3)
# t = Tournament(90, r3, r2, r1)
# res = t.start()
# print({place: runner.name for place, runner in res.items()})
