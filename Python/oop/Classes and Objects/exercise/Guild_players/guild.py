from Python.oop.classes_and_objects.exercise.Guild_players.player import Player


class Guild:

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        player_to_remove = next((player for player in self.players if player.name == player_name), None)
        if player_to_remove:
            self.players.remove(player_to_remove)
            player_to_remove.guild = "Unaffiliated"
            return f"Player {player_name} has been kicked from the guild."
        else:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        unpacked_players = '\n'.join([player.player_info() for player in self.players])
        return f"Guild: {self.name}\n{unpacked_players}"


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.add_skill("Shield Break", 20))
print(player.add_skill("Sword Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
