class Player:
    max_hp = 4000
    apple = 3500

player1 = Player()
print(player1.max_hp)
player2 = Player()
print(player2.apple)

class Players:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.score = 0


new_player1 = Players("Olly", 12000)
new_player1.hp += 500
new_player1.score += 10
print(new_player1.name, new_player1.hp, new_player1.score)
