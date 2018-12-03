#To access this function use fight_creature(skill, stamina)

import random

hero_skill = 0
hero_stamina = 0
monster_skill = 0
monster_stamina = 0


#Functions to simulate dice roll to define levels
def define_hero_skill():
    global hero_skill
    global initial_skill
    hero_skill = random.randint(1, 6) + 6
    initial_skill = hero_skill    

def define_hero_stamina():
    global hero_stamina
    global initial_stamina
    hero_stamina = random.randint(1, 12) + 12
    initial_stamina = hero_stamina    

def define_monster_skill():
    global monster_skill
    global initial_skill
    monster_skill = random.randint(1, 12) + 12
    initial_skill = monster_skill    

def define_monster_stamina():
    global monster_stamina
    global initial_stamina
    monster_stamina = random.randint(1, 12) + 12
    initial_stamina = monster_stamina    

def hero_death(taunt):
    print(taunt)
    exit()

class creature(object):

    action = ["The creature lunges at you",
              "The creature stabs at you",
              "The creature kung fu kicks at you",
              "The creature round house kicks at you"]     
                                
    wounds = ["The creature hits you square in the face",
              "The creature hits you in the stomach",
              "The creature hits you in the leg",]

    def __init__(self):
        pass
    
    def creature_action(self):
        print(self.action[random.randint(0, len(self.action)-1)])

    def creature_wound(self):
        print(self.wounds[random.randint(0, len(self.wounds)-1)])

#fights a creature with specified skill and stamina
def fight_creature(skill, stamina, who):
    global hero_stamina
    creature_skill = skill 
    creature_stamina = stamina
    while creature_stamina > 0 and hero_stamina > 0:
        print("Your stamina is now", hero_stamina)
        print(f"The stamina of {who} is now", creature_stamina)
        beast = creature()
        beast.creature_action()
        if (hero_skill + random.randint(1, 12)
           > creature_skill + random.randint(1, 12)):
            print(f"You have wounded {who}")
            creature_stamina -= 2
        elif (hero_skill + random.randint(1, 12)
              < creature_skill + random.randint(1, 12)):
            beast.creature_wound()
            hero_stamina -= 2
        else: 
            print("You clash. Neither of you is wounded")
    if creature_stamina < 1: 
        print(f"{who} is dead")
    elif hero_stamina < 1:
        hero_death("You have died")
        


#The fight begins!

define_hero_skill()
define_hero_stamina()
define_monster_skill()
define_monster_stamina()

print(f"""
Welcome Adventurer your vital statistics are as follows

Your skill level is {hero_skill}
Your stamina level is {hero_stamina}

Before you stands an irate monster. There is no escape you must fight to survive!

The monster's skill level is {monster_skill}
The monster's stamina level is {hero_stamina}

""")

