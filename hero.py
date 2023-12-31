from random import randint
from ability import Ability
from armor import Armor
from weapon import Weapon
from team import Team

class Arena:
  def __init__(self):
    self.team_one = Team("Team One")
    self.team_two = Team("Team Two")
  # TODO: create instance variables named team_one and team_two that
  # will hold our teams.

  def create_ability(self):
    name = input("What is the ability name?  ")
    max_damage = int(input("What is the max damage of the ability?  "))
    return Ability(name, max_damage)

  def create_weapon(self):
    name = input("What is the name of this weapon?  ")
    max_damage = input("What is the max damage of this weapon?  ")
    return Weapon(name, max_damage)

  def create_armor(self):
    name = input("What is the armor name? > ")
    max_block = input("What is the max block of the armor? > ")
    return Armor(name, max_block)

  def create_hero(self):
    hero_name = input("Hero's name: ")
    hero = Hero(hero_name)
    add_item = None

    while add_item != "4":
      add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
      if add_item == "1":
        hero.add_ability(self.create_ability())
      elif add_item == "2":
        hero.add_weapon(self.create_weapon())
      elif add_item == "3":
        hero.add_armor(self.create_armor())
    return hero

  def build_team_one(self):
    numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
    for i in range(numOfTeamMembers):
      hero = self.create_hero()
      self.team_one.add_hero(hero)

  def build_team_two(self):
    numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
    for i in range(numOfTeamMembers):
      hero = self.create_hero()
      self.team_two.add_hero(hero)

  def team_battle(self):
      self.team_one.attack(self.team_two)

  def show_stats(self):
      print("\n")
      print(self.team_one.name + " statistics: ")
      self.team_one.stats()
      print("\n")
      print(self.team_two.name + " statistics: ")
      self.team_two.stats()
      print("\n")

      team_kills_one = sum([hero.kills for hero in self.team_one.heroes])
      team_deaths_one = sum([hero.deaths for hero in self.team_one.heroes])
      if team_deaths_one == 0:
        team_deaths_one = 1
      print(self.team_one.name + " average K/D was: " + str(team_kills_one/team_deaths_one))

      team_kills_two = sum([hero.kills for hero in self.team_two.heroes])
      team_deaths_two= sum([hero.deaths for hero in self.team_two.heroes])
      if team_deaths_two == 0:
        team_deaths_two = 1
      print(self.team_two.name + " average K/D was: " + str(team_kills_two/team_deaths_two))

      print("Survived from " + self.team_one.name + ": ")
      for hero in self.team_one.heroes:
        if hero.deaths == 0:
          print("- " + hero.name)

      print("Survived from " + self.team_two.name + ": " + hero.name)
      for hero in self.team_two.heroes:
        if hero.deaths == 0:
          print("- " + hero.name)
          

class Hero:
  def __init__(self, name, starting_health=100):
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

    self.abilities = list()
    self.armors = list()

    self.deaths = 0
    self.kills = 0

  def add_ability(self, ability):
    self.abilities.append(ability)

  def add_armor(self, armor):
    self.armors.append(armor)

  def attack(self):
    total_damage = 0 

    for ability in self.abilities:
      total_damage += ability.attack()
    return total_damage

  def defend(self):
    total_block = 0
    if self.current_health == 0:
      return total_block
    for armor in self.armors:
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
            self.add_deaths()
            opponent.add_kills()
            return
        print(f"{self.name} won!")
        self.add_kills()
        opponent.add_deaths()

  def add_weapon(self, weapon):
    self.abilities.append(weapon)
    pass

  def add_kills(self):
    self.kills += 1
  
  def add_deaths(self):
    self.deaths += 1

if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  arena = Arena()
  arena.build_team_one()
  arena.build_team_two()
  arena.team_battle()
  arena.show_stats()
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
