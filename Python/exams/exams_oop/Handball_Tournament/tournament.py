import re

from Handball_Tournament.equipment.elbow_pad import ElbowPad
from Handball_Tournament.equipment.knee_pad import KneePad
from Handball_Tournament.teams.indoor_team import IndoorTeam
from Handball_Tournament.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT_TYPES = {
        "KneePad": KneePad,
        "ElbowPad": ElbowPad,
    }

    VALID_TEAM_TYPES = {
        "OutdoorTeam": OutdoorTeam,
        "IndoorTeam": IndoorTeam,
    }

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not re.match(r'^[a-zA-Z0-9]+$', value):
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        item = Tournament.VALID_EQUIPMENT_TYPES.get(equipment_type)
        if item is None:
            raise Exception("Invalid equipment type!")
        self.equipment.append(item())
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        team = Tournament.VALID_TEAM_TYPES.get(team_type)
        if team is None:
            raise Exception("Invalid team type!")
        if self.capacity == len(self.teams):
            return "Not enough tournament capacity."
        self.teams.append(team(team_name, country, advantage))
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = (self.VALID_EQUIPMENT_TYPES.get(equipment_type))()
        team = self.get_team(team_name)
        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")
        index = next((i for i, e in reversed(list(enumerate(self.equipment))) if e.__class__.__name__ == equipment_type))
        piece_of_equipment = self.equipment.pop(index)
        team.budget -= piece_of_equipment.price
        team.equipment.append(piece_of_equipment)
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = self.get_team(team_name)
        if team is None:
            raise Exception("No such team!")
        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        num_of_changed_items = 0
        for item in self.equipment:
            if item.__class__.__name__ == equipment_type:
                num_of_changed_items += 1
                item.increase_price()

        return f"Successfully changed {num_of_changed_items}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team_one = self.get_team(team_name1)
        team_two = self.get_team(team_name2)
        if team_one.__class__.__name__ != team_two.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")
        team_one_total_score = self.calculate_total_protection(team_one) + team_one.advantage
        team_two_total_score = self.calculate_total_protection(team_two) + team_two.advantage

        if team_one_total_score == team_two_total_score:
            return "No winner in this game."
        if team_one_total_score > team_two_total_score:
            team_one.win()
            return f"The winner is {team_name1}."
        team_two.win()
        return f"The winner is {team_name2}."

    def get_statistics(self):
        return_string = f"Tournament: {self.name}\n"

        sorted_teams = sorted(self.teams, key=lambda team: team.wins, reverse=True)

        number_of_teams = len(sorted_teams)
        return_string += f"Number of Teams: {number_of_teams}\nTeams:\n"

        teams_stats = '\n'.join([team.get_statistics() for team in sorted_teams])
        return_string += teams_stats

        return return_string

    @staticmethod
    def calculate_total_protection(team):
        total = 0
        for item in team.equipment:
            total += item.protection
        return total

    def get_team(self, team_name: str):
        return next((team for team in self.teams if team.name == team_name), None)
