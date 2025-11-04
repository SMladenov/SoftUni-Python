from project.zones.base_zone import BaseZone
from project.battleships.royal_battleship import RoyalBattleship

class PirateZone(BaseZone):
    def __init__(self, code):
        super().__init__(code, 8)
    
    def zone_info (self):
        listToOutput = []

        listToOutput.append("@Pirate Zone Statistics@")
        listToOutput.append(f"Code: {self.code}; Volume: {self.volume}")
        royalShips = [ship for ship in self.ships if isinstance(ship, RoyalBattleship)]
        listToOutput.append(f"Battleships currently in the Pirate Zone: {len(self.ships)}, {len(royalShips)} out of them are Royal Battleships.")

        sortedShips = self.get_ships()
        if sortedShips:
            shipNames = [ship.name for ship in sortedShips]
            listToOutput.append(f"#{', '.join(shipNames)}#")
        
        return "\n".join(listToOutput)
    

    