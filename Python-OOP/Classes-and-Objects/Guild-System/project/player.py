
class Player:
    def __init__ (self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: dict = {}
        self.guild = "Unaffiliated"
    
    def add_skill (self, skill_name, manacost):
        if skill_name not in self.skills.keys():
            self.skills[skill_name] = manacost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        else:
            return f"Skill already added"
    
    def player_info (self):
        listToOutput = []
        listToOutput.append(f"Name: {self.name}")
        listToOutput.append(f"Guild: {self.guild}")
        listToOutput.append(f"HP: {self.hp}")
        listToOutput.append(f"MP: {self.mp}")
    
        for key, value in self.skills.items():
            listToOutput.append(f"==={key} - {value}")
            
        listToOutput.append("")
        return '\n'.join(listToOutput)
    
