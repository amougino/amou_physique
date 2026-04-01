import numpy as np


class Approx:

    def __init__(self, function, x_values, y_values, initial_steps, guesses, factor):
        self.f = function  # function
        self.x = x_values  # int list
        self.y = y_values  # int list
        self.vars = guesses  # int list
        self.factor = factor  # int
        self.variations = initial_steps
        self.last_dir = -1
        self.iteration = [0 for i in self.vars]

    def iterate(self):
        self.iteration[0] += 1
        looking = True
        current = 0
        length = len(self.iteration)
        while looking:
            if self.iteration[current] > 2:
                if current == length - 1:
                    looking = False
                    self.iteration = [0 for i in range(length)]
                else:
                    self.iteration[current] = 0
                    self.iteration[current + 1] += 1
                    current += 1
            else:
                looking = False

    def vars_to_try(self):
        self.iteration = [0 for i in self.vars]
        self.tries = []
        length = len(self.iteration)
        for i in range(3**length):
            guess = []
            for j in range(length):
                guess.append(self.vars[j] +
                             (self.iteration[j] - 1)*self.variations[j])
            self.tries.append([i, guess])
            self.iterate()

    def distance(self, guess):
        sum = 0
        for i in range(len(self.x)):
            sum += (self.f(self.x[i], guess) - self.y[i])**2
        return np.sqrt(sum)

    def step(self):
        self.vars_to_try()
        results = []
        for i in self.tries:
            results.append([i[0], self.distance(i[1])])
        min = results[0]
        for i in results:
            if i[1] < min[1]:
                min = i

        if min[0] != self.last_dir:
            for j in range(len(self.variations)):
                self.variations[j] *= self.factor
        elif self.vars == self.tries[min[0]][1]:
            for j in range(len(self.variations)):
                self.variations[j] *= self.factor
        self.vars = self.tries[min[0]][1]
        self.last_dir = min[0]


'''
x1 = [40, 50, 100, 120, 280, 400]
y1 = [16, 13.5, 8.5, 6, 3, 1.8]


def F(x, variables):
    return (variables[0]*x + variables[1])


s = Approx(F, x1, y1, [5, 1], [5, 5], 0.99)

for x in range(50):
    s.step()
    print(s.vars)
'''

# TO DO : MAKE VARIATION DIFFERENT FOR EACH PARAMETER
