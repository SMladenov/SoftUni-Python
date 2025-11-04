from project.battleships.base_battleship import BaseBattleship

class RoyalBattleship(BaseBattleship):
    def __init__(self, name, health, hit_strength):
        super().__init__(name, health, hit_strength, 100)
    
    def attack(self):
        self.ammunition -= 25
        if self.ammunition < 0:
            self.ammunition = 0