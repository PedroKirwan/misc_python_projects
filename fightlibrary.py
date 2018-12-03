#To access this function use fight_creature(skill, stamina)

import random

hero_skill = 0
hero_stamina = 0
hero_charm = 0


coat_pockets = {
        "side_pocket": "",
        "chest_pocket": "regular_gun",
}

speeches = [
"""
You look at General Nibbles but he will not fight you:

'You're a coward stranger and the world is filled with
your kind. I've seen enough of cowards
and suffering. Private Basil was the only one that
gave me hope for, unknown to her, she was Meepishan, the one of
which the ancients spoke. But all that is done now.'

With that General Nibbles falls on his dagger.

You have, you realise, made a terrible mistake and somewhere
deep inside you something withers and dies. 

You must, however, push on and you exit by the door and
walk down the corridor. There's a door in the wall.
""",
"""
second multiple lines
speech
"""
]

#Functions to simulate dice roll to define levels
def define_hero_skill():
    global hero_skill
    hero_skill = random.randint(1, 6) + 6

def define_hero_stamina():
    global hero_stamina
    hero_stamina = random.randint(1, 12) + 12

def define_hero_charm():
    global hero_charm
    hero_charm = random.randint(1, 12) + 12

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
        
define_hero_skill()
define_hero_stamina()
define_hero_charm()

