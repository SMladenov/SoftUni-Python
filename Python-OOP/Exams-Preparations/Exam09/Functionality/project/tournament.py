from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam

class Tournament():
    def __init__ (self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: list[BaseEquipment] = []
        self.teams: list[BaseTeam] = []
    
    @property
    def name (self):
        return self.__name
    @name.setter
    def name (self, name: str):
        for _ in name:
            if not _.isalpha() and not _.isdigit():
                raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = name
    
    def add_equipment (self, equipment_type: str):
        if equipment_type not in ["KneePad", "ElbowPad"]:
            return f"Invalid equipment type!"
        
        if equipment_type == "KneePad":
            newEquip = KneePad()
            self.equipment.append(newEquip)
        elif equipment_type == "ElbowPad":
            newEquip = ElbowPad()
            self.equipment.append(newEquip)
        return f"{equipment_type} was successfully added."
    
    def add_team (self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in ["OutdoorTeam", "IndoorTeam"]:
            return f"Invalid team type!"
        
        if self.capacity == 0:
            return f"Not enough tournament capacity."
        
        if team_type == "OutdoorTeam":
            newTeam = OutdoorTeam(team_name, country, advantage)
            self.teams.append(newTeam)
        elif team_type == "IndoorTeam":
            newTeam = IndoorTeam(team_name, country, advantage)
            self.teams.append(newTeam)
        self.capacity -= 1
        return f"{team_type} was successfully added."
    
    def sell_equipment (self, equipment_type: str, team_name: str):
        teamFound = [team for team in self.teams if team.name == team_name]
        equipmentFound = [equipment for equipment in self.equipment if equipment.__class__.__name__ == equipment_type]

        teamBudget = teamFound[0].budget
        equipmentPrice = equipmentFound[0].price

        if teamBudget < equipmentPrice:
            raise Exception("Budget is not enough!")
        
        self.equipment.remove(equipmentFound[0])
        teamFound[0].equipment.append(equipmentFound[0])
        teamFound[0].budget -= equipmentPrice
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team (self, team_name: str):
        teamFound = [team for team in self.teams if team.name == team_name]
        if not teamFound:
            raise Exception("No such team!")
        
        if teamFound[0].wins > 0:
            raise Exception(f"The team has {teamFound[0].wins} wins! Removal is impossible!")
        
        self.teams.remove(teamFound[0])
        self.capacity += 1
        return f"Successfully removed {team_name}."
    
    def increase_equipment_price (self, equipment_type: str):
        equipmentFound = [equipment for equipment in self.equipment if equipment.__class__.__name__ == equipment_type]
        for equipment in equipmentFound:
            equipment.increase_price()
        return f"Successfully changed {len(equipmentFound)}pcs of equipment."

    def play (self, team_name1: str, team_name2: str):
        team1Found = [team for team in self.teams if team.name == team_name1]
        team2Found = [team for team in self.teams if team.name == team_name2]
        team1 = team1Found[0]
        team2 = team2Found[0]

        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception(f"Game cannot start! Team types mismatch!")
        
        result1 = team1.advantage + sum([equipment.protection for equipment in team1.equipment])
        result2 = team2.advantage + sum([equipment.protection for equipment in team2.equipment])

        if result1 == result2:
            return f"No winner in this game."
        elif result1 > result2:
            team1.win()
            return f"The winner is {team1.name}."
        else:
            team2.win()
            return f"The winner is {team2.name}."
    
    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda team: (-team.wins, team.name))
        team_stats = "\n".join([team.get_statistics() for team in sorted_teams])
        
        return f"Tournament: {self.name}\nNumber of Teams: {len(self.teams)}\nTeams:\n{team_stats}"
    

    
# t = Tournament('SoftUniada2023', 2)

# print(t.add_equipment('KneePad'))
# print(t.add_equipment('ElbowPad'))

# print(t.add_team('OutdoorTeam', 'Levski', 'BG', 250))
# print(t.add_team('OutdoorTeam', 'Spartak', 'BG', 250))
# print(t.add_team('IndoorTeam', 'Dobrich', 'BG', 280))

# print(t.sell_equipment('KneePad', 'Spartak'))

# print(t.remove_team('Levski'))
# print(t.add_team('OutdoorTeam', 'Lokomotiv', 'BG', 250))

# print(t.increase_equipment_price('ElbowPad'))
# print(t.increase_equipment_price('KneePad'))

# print(t.play('Lokomotiv', 'Spartak'))

# print(t.get_statistics())


