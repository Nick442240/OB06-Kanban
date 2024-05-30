import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        if self.is_alive():
            damage = random.randint(1, self.attack_power)
            other.health -= damage
            print(f"{self.name} attacks {other.name} for {damage} damage.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        print(f"The battle between {self.player.name} and {self.computer.name} begins!")
        while self.player.is_alive() and self.computer.is_alive():
            if random.choice([True, False]):
                self.player.attack(self.computer)
                if self.computer.is_alive():
                    self.computer.attack(self.player)
            else:
                self.computer.attack(self.player)
                if self.player.is_alive():
                    self.player.attack(self.computer)
            self.print_status()
        self.declare_winner()

    def print_status(self):
        print(f"{self.player.name} Health: {self.player.health}")
        print(f"{self.computer.name} Health: {self.computer.health}")
        print("-" * 30)

    def declare_winner(self):
        if self.player.is_alive():
            print(f"{self.player.name} wins!")
        else:
            print(f"{self.computer.name} wins!")

# Пример использования:
player = Hero("Player")
computer = Hero("Computer")
game = Game(player, computer)
game.start()
