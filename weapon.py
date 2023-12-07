from ability import Ability
import random

class Weapon:
  def __init__(self, name, max_damage):
    self.name = name
    self.max_damage = int(max_damage)
 
  def attack(self):
    # TODO: Use integer division to find half of the max_damage value
    # then return a random integer between half of max_damage and max_damage
    random_value = random.randint(self.max_damage // 2, self.max_damage)
    return random_value