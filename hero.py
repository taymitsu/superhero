import random 
import ability from Ability

class Hero:
  def __init__(self, name, starting_health=100):
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

  def fight(self, opponent):
    heroes = [self, opponent]
    if random.choice(heroes) == self:
      print(f"{self.name} defeats {opponent.name}!")
    else:
      print(f"{opponent.name} defeats {self.name}!")


if __name__ == "__main__":
  #hero1 = Hero("Tiny Tyson", 200)
  hero1 = Hero("Wonder Woman", 300)
  hero2 = Hero("Dumbledore", 250) 
  hero1.fight(hero2)
  #print(hero1.name)
  #print(hero1.current_health)