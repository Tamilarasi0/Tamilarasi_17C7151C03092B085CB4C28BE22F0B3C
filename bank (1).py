class Player:
    def __init__(self, name):
        self.name = name
    def play(self):
        print(f"{self.name} is playing cricket.")
class Batsman(Player):
    def play(self):
        print(f"{self.name} is batting.")
class Bowler(Player):
    def play(self):
        print(f"{self.name} is bowling.")
batsman = Batsman("Sachin")
bowler = Bowler("Malinga")
batsman.play()
bowler.play()
class AllRounder(Player):
    def play(self):
        super().play()
        print(f"{self.name} is also bowling and batting.")
all_rounder = AllRounder("Kallis")
all_rounder.play()
