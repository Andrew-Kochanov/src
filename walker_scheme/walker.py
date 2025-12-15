import random


class Walker:
    def __init__(self, probabilities: list[tuple[str, float]]):
        self.probabilities = sorted(probabilities, key=lambda x: x[1])
        self.probabilities_walker = [[self.probabilities[i][0], 1 / len(self.probabilities)] for i in range(len(self.probabilities))]
        summa = sum[probabilities[i][1] for i in range(len(probabilities))]
        if summa != 1:
            raise ValueError('Сумма вероятностей не равна единице')

    def walker_scheme(self):
        barrier = 0
        for i in range(len(self.probabilities) - 1):
            if self.probabilities[i][1] < self.probabilities_walker[i][1]:
                self.probabilities_walker[i][1] = self.probabilities[i][1] + barrier
                self.probabilities_walker[i + 1][1] += (self.probabilities_walker[i][1] - self.probabilities[i][1])
                barrier = self.probabilities_walker[i][1]
            elif  self.probabilities[i][1] > self.probabilities_walker[i][1]:
                self.probabilities_walker[i][1] = self.probabilities[i][1] + barrier
                self.probabilities_walker[i + 1][1] -= (self.probabilities[i][1] - self.probabilities_walker[i][1])
                barrier = self.probabilities_walker[i][1]
            elif self.probabilities[i][1] == self.probabilities_walker[i][1]:
                self.probabilities_walker[i][1] += barrier
                barrier = self.probabilities_walker[i][1]
        self.probabilities_walker[-1][1] += barrier

    def get_random(self):
        probability = random.random()
        self.walker_scheme()
        for i in self.probabilities_walker:
            if probability <= i[1]:
                return i[0]
