class Player:

    def __init__(self, name, hp, mp, guild="Unaffiliated"):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = guild

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        unpacked_dictionary = []
        for skill_name, mana_cost in self.skills.items():
            unpacked_dictionary.append(f"==={skill_name} - {mana_cost}\n")
        return_message = f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n"
        return f"{return_message}{''.join(unpacked_dictionary)}"
