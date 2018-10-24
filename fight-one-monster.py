import random

hero_skill = 0
hero_stamina = 0

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

def hero_death(taunt):
    print(taunt)
    exit()

class creature(object):

    action = ["The creature lunges",
              "The creature stabs",
              "The creature kung fu kicks",
              "The creature round house kicks"]     
                                
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
def fight_creature(skill, stamina):
    global hero_stamina
    global hero_luck
    creature_skill = skill 
    creature_stamina = stamina
    while creature_stamina > 0 and hero_stamina > 0:
        print("hero stamina is", hero_stamina)
        print("creature stamina is", creature_stamina)
        beast = creature()
        beast.creature_action()
        if (hero_skill + random.randint(1, 12)
           > creature_skill + random.randint(1, 12)):
            print("You have wounded the creature")
            creature_stamina -= 2
        elif (hero_skill + random.randint(1, 12)
              < creature_skill + random.randint(1, 12)):
            beast.creature_wound()
            hero_stamina -= 2
        else: 
            print("Your swords clash")
    if creature_stamina < 1: 
        print("the creature is dead")
    elif hero_stamina < 1:
        hero_death("So long amigo!")


#The fight begins!

define_hero_skill()
define_hero_stamina()

print(f"""
Welcome Adventurer your vital statistics are as follows

Your skill level is {hero_skill}
Your stamina level is {hero_stamina}
""")

fight_creature(20, 20)
