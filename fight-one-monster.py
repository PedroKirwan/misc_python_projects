import random

# add in functions for luck, strength and stamina potions. each potion has two servings and can be taken at any time. Adventurer can choose ONE potion at start of journey. the luck potion will also add 1 to inital luck
# probably should put the page text in their own file and draw them out

equipment = ["sword", "shield"]
initial_skill = 0
initial_stamina = 0

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


#fights two creatures one at a time 
def fight_creatures(skill1, stamina1, skill2, stamina2):
    global hero_stamina
    global hero_luck
    creature1_skill = skill1 
    creature1_stamina = stamina1
    creature2_skill = skill2 
    creature2_stamina = stamina2
    i = 0
    while creature1_stamina or creature2_stamina > 0:
        i += 1
        fight_creature1 = (((i % 2) == 0 and creature1_stamina > 0)
                     or (creature2_stamina < 1 and creature1_stamina > 0))
        fight_creature2 = (((i % 2) != 0 and creature2_stamina > 0)
                      or (creature1_stamina < 1 and creature2_stamina > 0))
        
        if hero_stamina <= 0:
            hero_death()

        elif fight_creature1:
            print("hero stamina is", hero_stamina)
            print("creature1 stamina is", creature1_stamina)
            if (hero_skill + random.randint(1, 12)
                > creature1_skill + random.randint(1, 12)):
                print("You have wounded the creature1")
                test_your_luck = input("test your luck? ")
                if test_your_luck is "y" and hero_luck >= random.randint(1, 12):
                    print("You strike a major organ")
                    creature1_stamina = creature1_stamina - 4
                    print("your luck was", hero_luck)
                    hero_luck = hero_luck - 1
                    print("your luck is now", hero_luck)
                if test_your_luck is "y" and hero_luck < random.randint(1, 12):
                    print("Your barely hit the evil creature1")
                    creature1_stamina = creature1_stamina - 1 
                    print("your luck was", hero_luck)
                    hero_luck = hero_luck - 1
                    print("your luck is now", hero_luck)
                else: 
                    creature1_stamina = creature1_stamina - 2
                    print("you do a normal amount of damage")
            elif (hero_skill + random.randint(1, 12)
                  < creature1_skill + random.randint(1, 12)):
                print("The creature1 has wounded you!")
                test_your_luck = input("test your luck? ")
                if test_your_luck is "y" and hero_luck >= random.randint(1, 12):
                    print("The creature1's barely grazes you")
                    hero_stamina = hero_stamina - 1
                elif test_your_luck is "y" and hero_luck <= random.randint(1, 12):
                    print("Ouch! The creature1 strikes a major organ!")
                    hero_stamina = hero_stamina - 4
                else: 
                    hero_stamina = hero_stamina - 2
            else: 
                print("Your swords clash")
        elif fight_creature2:        
            print("hero stamina is", hero_stamina)
            print("creature2 stamina is", creature2_stamina)
            if (hero_skill + random.randint(1, 12)
                > creature2_skill + random.randint(1, 12)):
                print("You have wounded the creature2")
                test_your_luck = input("test your luck? ")
                if test_your_luck is "y" and hero_luck >= random.randint(1, 12):
                    print("You strike a major organ")
                    creature2_stamina = creature2_stamina - 4
                    print("your luck was", hero_luck)
                    hero_luck = hero_luck - 1
                    print("your luck is now", hero_luck)
                elif test_your_luck is "y" and hero_luck <= random.randint(1, 12):
                    print("Your barely hit the evil creature2")
                    creature2_stamina = creature2_stamina - 1 
                    print("your luck was", hero_luck)
                    hero_luck = hero_luck - 1
                    print("your luck is now", hero_luck)
                else: 
                    creature2_stamina = creature2_stamina - 2
            elif (hero_skill + random.randint(1, 12)
                  < creature2_skill + random.randint(1, 12)):
                print("The creature2 has wounded you!")
                test_your_luck = input("test your luck? ")
                if test_your_luck is "y" and hero_luck >= random.randint(1, 12):
                    print("The creature2 barely grazes you")
                    hero_stamina = hero_stamina - 1
                elif test_your_luck is "y" and hero_luck <= random.randint(1, 12):
                    print("Ouch! The creature2 strikes a major organ!")
                    hero_stamina = hero_stamina - 4 
                else: 
                    hero_stamina = hero_stamina - 2
            else: 
                print("Your swords clash")

    return print("Both creatures are dead")

'''elif hero_stamina < 1:
            print("you died")
            quit()
        if creature2_stamina < 1:
            print("creature2 is dead")
        elif hero_stamina < 1:
            print("you died")
            quit()
        '''

#The adventure begins!

define_hero_skill()
define_hero_stamina()

print(f"""

Welcome Adventurer your vital statistics are as follows

Your skill level is {hero_skill}
Your stamina level is {hero_stamina}
""")

fight_creature(20, 20)
