from project.player import Player

class Guild:
    def __init__ (self, name: str):
        self.name = name
        self.players: list[Player] = []
    
    def assign_player (self, player: Player):
        if player not in self.players:
            if player.guild == "Unaffiliated":
                self.players.append(player)
                player.guild = self.name
                return f"Welcome player {player.name} to the guild {self.name}"
            else:
                return f"Player {player.name} is in another guild."
        
        elif player in self.players:
            return f"Player {player.name} is already in the guild."
        
    def kick_player (self, player_name: str):
        found = False
        for player in self.players:
            if player.name == player_name:
                player.guild = "Unaffiliated"
                self.players.remove(player)
                found = True
                return f"Player {player.name} has been removed from the guild."
        if not found:
            return f"Player {player_name} is not in the guild."
    
    def guild_info(self):
        listToOutput = []
        listToOutput.append(f"Guild: {self.name}")
        for player in self.players:
            listToOutput.append(player.player_info())
        
        return '\n'.join(listToOutput)

# player = Player("George", 50, 100)

# print(player.add_skill("Shield Break", 20))

# print(player.player_info())

# guild = Guild("UGT")

# print(guild.assign_player(player))

# print(guild.guild_info())