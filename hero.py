import random 
from ability import Ability
from armor import Armor

class Hero:
  def __init__(self, name, starting_health=100):
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

    self.abilities = list()
    self.armor = list()

  def fight(self, opponent):
    heroes = [self, opponent]
    if random.choice(heroes) == self:
      print(f"{self.name} defeats {opponent.name}!")
    else:
      print(f"{opponent.name} defeats {self.name}!")

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

if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.

  hero = Hero("Grace Hopper", 200)
  hero.take_damage(150)
  print(hero.is_alive())
  hero.take_damage(15000)
  print(hero.is_alive())