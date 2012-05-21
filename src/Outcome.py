class Outcome(object): pass


class UncertainOutcome(Outcome): pass


class PositiveOutcome(Outcome):
    def __init__(self, observation):
        self.observation = observation

    def __repr__(self):
        return '<PositiveOutcome(observation=%s)>' % self.observation


class NegativeOutcome(Outcome):
    def __init__(self, problem, solution=None):
        self.problem = problem
        self.solution = solution

    def __repr__(self):
        return '<NegativeOutcome(problem=%s, solution=%s)>' % (self.problem, self.solution)

