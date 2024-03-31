from Handball_Tournament.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    INITIAL_BUDGET = 500.0
    ADVANTAGE_PER_WIN = 145

    def __init__(self, name, country, advantage):
        super().__init__(name, country, advantage, budget=self.INITIAL_BUDGET)

    def win(self):
        self.advantage += self.ADVANTAGE_PER_WIN
        self.wins += 1
