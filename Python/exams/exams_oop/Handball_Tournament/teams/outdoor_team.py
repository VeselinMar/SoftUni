from Python.exams.exams_oop.Handball_Tournament.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    INITIAL_BUDGET = 1000.0
    ADVANTAGE_PER_WIN = 115

    def __init__(self, name, country, advantage):
        super().__init__(name, country, advantage, budget=self.INITIAL_BUDGET)

    def win(self):
        self.advantage += self.ADVANTAGE_PER_WIN
        self.wins += 1
