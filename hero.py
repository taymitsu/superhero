import random
from ability import Ability
from armor import Armor
from weapon import Weapon
from team import Team

class Hero:
  def __init__(self, name, starting_health=100):
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

    self.abilities = list()
    self.armor = list()

  def add_ability(self, ability):
    self.abilities.append(ability)

  def add_armor(self, armor):
    self.armor.append(armor)

  def attack(self):
    total_damage = 0 

    for ability in self.abilities:
      total_damage += ability.attack()
    return total_damage

  def defend(self):
    total_block = 0
    if self.current_health == 0:
      return total_block
    for armor in self.armor:
      total_block += armor.block()
    return total_block

  def take_damage(self, damage):
    defense = self.defend()
    new_damage = damage - defense 
    if new_damage > 0:
      self.current_health -= new_damage
      return self.current_health
    else:
      return "No damage was taken"

  def is_alive(self):
    if self.current_health <= 0:
      return False
    else: 
      return True

  def fight(self, opponent):
    if len(self.abilities) == 0 and len(opponent.abilities) == 0:
      print("Draw!")
    else: 
      while self.is_alive() and opponent.is_alive():
        total_damage = self.attack()
        opponent.take_damage(total_damage)

        if opponent.is_alive():
          total_damage = opponent.attack()
          self.take_damage(total_damage)
          if not self.is_alive():
            print(f"{opponent.name} won!")
            return
        print(f"{self.name} won!")

  def add_weapon(self, weapon):
    self.abilities.append(weapon)
    pass

if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.

  hero1 = Hero("Wonder Woman")
  hero2 = Hero("Dumbledore")
  ability1 = Ability("Super Speed", 300)
  ability2 = Ability("Super Eyes", 130)
  ability3 = Ability("Wizard Wand", 80)
  ability4 = Ability("Wizard Beard", 20)
  hero1.add_ability(ability1)
  hero1.add_ability(ability2)
  hero2.add_ability(ability3)
  hero2.add_ability(ability4)
  hero1.fight(hero2)
