from project.zones.base_zone import BaseZone
from project.battleships.pirate_battleship import PirateBattleship

class RoyalZone(BaseZone):
    def __init__(self, code):
        super().__init__(code, 10)
    
    def zone_info (self):
        listToOutput = []

        listToOutput.append("@Royal Zone Statistics@")
        listToOutput.append(f"Code: {self.code}; Volume: {self.volume}")
        pirateShips = [ship for ship in self.ships if isinstance(ship, PirateBattleship)]
        listToOutput.append(f"Battleships currently in the Royal Zone: {len(self.ships)}, {len(pirateShips)} out of them are Pirate Battleships.")

        sortedShips = self.get_ships()
        if sortedShips:
            shipNames = [ship.name for ship in sortedShips]
            listToOutput.append(f"#{', '.join(shipNames)}#")
        
        return "\n".join(listToOutput)
    
        
