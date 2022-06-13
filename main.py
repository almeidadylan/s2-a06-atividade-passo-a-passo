"""
class Villager:
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.defense = 0
        self.attack = 0
        self.is_alive = True

    def check_health(self, incoming_attack_value):
        if self.defense < incoming_attack_value:
            self.health -= incoming_attack_value
            if self.health <= 0:
                self.is_alive = False
                self.health = 0
                return (False, "Target is dead!")
            return self.health
        else:
            return self.health

    def normal_attack(self, target):
        self.attack = target.attack
        target.check_health(target.attack)
        if target.health <= 0:
            return (False, "Target is dead!")
        elif target.health > 0:
            return target.health

class Mage(Villager):
    def __init__(self, name):
        super().__init__(name)
        self.attack = 10
        self.mana = 100    

    def fire_ball(self, target):
        if self.mana >= 20:
            self.mana -= 20
            target.check_health(self.attack + 20)
            if target.health <= 0:
                return (False, "Target is dead!")
            elif target.health > 0:
                return target.health
        elif self.mana < 20:
            return (False, "Not enough mana!")

"""
class Villager:
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.defense = 0
        self.attack = 0
        self.is_alive = True
    
    def check_health(self, incoming_attack_value):
        damage = incoming_attack_value - self.defense
        self.health -= damage
        self.health = self.health if self.health > 0 else 0
        if not self.health:
            self.is_alive = False
            return (False, "Target is dead!")
        return self.health
    
    def normal_attack(self, target):
        return target.check_health(self.attack)

class Mage(Villager):
    def __init__(self, name):
        super().__init__(name)
        self.attack = 10
        self.mana = 100
    
    def fire_ball(self, target):
        mana_spend = 20
        if self.mana < mana_spend:
            return (False, "Not enough mana!")
        self.mana -= mana_spend
        damage = self.attack + mana_spend
        return target.check_health(damage)



if __name__ == "__main__":
    villager = Villager("Villager")
    mage = Mage("Mage")

    print(
        "*"*50,
        "teste 1\n",
        "Esperado: {'name': 'Villager', 'health': 50, 'defense': 0, 'attack': 0, 'is_alive': True}",
        f"Resultado: {vars(villager)}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "teste 2\n",
        "Esperado: {'name': 'Mage', 'health': 50, 'defense': 0, 'attack': 10, 'is_alive': True, 'mana': 100}",
        f"Resultado: {vars(mage)}",
        "*"*50,
        sep="\n"
    )
    
    battle_result = mage.fire_ball(villager)

    print(
        "*"*50,
        "teste 3\n",
        "Esperado: 20",
        f"Resultado: {battle_result}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "teste 4\n",
        "Esperado: {'name': 'Villager', 'health': 20, 'defense': 0, 'attack': 10, 'is_alive': True}",
        f"Resultado: {vars(villager)}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "teste 5\n",
        "Esperado: {'name': 'Mage', 'health': 50, 'defense': 0, 'attack': 10, 'is_alive': True, 'mana': 80}",
        f"Resultado: {vars(mage)}",
        "*"*50,
        sep="\n"
    )

    battle_result = mage.normal_attack(villager)

    print(
        "*"*50,
        "teste 6\n",
        "Esperado: 10",
        f"Resultado: battle_result",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "teste 7\n",
        "Esperado: {'name': 'Villager', 'health': 10, 'defense': 0, 'attack': 0, 'is_alive': True}",
        f"Resultado: {vars(villager)}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "teste 8\n",
        "Esperado: {'name': 'Mage', 'health': 50, 'defense': 0, 'attack': 10, 'is_alive': True, 'mana': 80}",
        f"Resultado: {vars(mage)}",
        "*"*50,
        sep="\n"
    )

    battle_result = mage.fire_ball(villager)

    print(
        "*"*50,
        "teste 9\n",
        f"Esperado: {(False, 'Target is dead!')}",
        f"Resultado: {battle_result}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "teste 10\n",
        "Esperado: {'name': 'Villager', 'health': 0, 'defense': 0, 'attack': 0, 'is_alive': False}",
        f"Resultado: {vars(villager)}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "teste 11\n",
        "Esperado: {'name': 'Mage', 'health': 50, 'defense': 0, 'attack': 10, 'is_alive': True, 'mana': 60}",
        f"Resultado: {vars(mage)}",
        "*"*50,
        sep="\n"
    )

    battle_result = mage.fire_ball(villager)

    print(
        "*"*50,
        "teste 12\n",
        f"Esperado: {(False, 'Target is dead!')}",
        f"Resultado: {battle_result}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "teste 13\n",
        f"Esperado: 40",
        f"Resultado: {mage.mana}",
        "*"*50,
        sep="\n"
    )

    battle_result = mage.fire_ball(villager)
    battle_result = mage.fire_ball(villager)
    battle_result = mage.fire_ball(villager)

    print(
        "*"*50,
        "teste 14\n",
        f"Esperado: {(False, 'Not enough mana!')}",
        f"Resultado: {battle_result}",
        "*"*50,
        sep="\n"
    )
