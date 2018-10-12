import random

# add in an array for items in backpack
# add in functions for luck, strength and stamina potions. each potion has two servings and can be taken at any time. Adventurer can choose ONE potion at start of journey. the luck potion will also add 1 to inital luck
# probably should put the page text in their own file and draw them out


equipment = ["sword", "shield"]
initial_skill = 0
initial_stamina = 0
initial_luck = 0
provision_capacity = 10

hero_skill = 0
hero_stamina = 0
hero_luck = 0
provisions = 10 #eating one provision adds 4 to stamina

def decrease_stamina(amount):
    global hero_stamina
    print("your stamina was", hero_stamina)
    hero_stamina = hero_stamina - amount
    if hero_stamina <= 0:
        print("You have perished")
        quit()
    else:
        print("Your stamina is now", hero_stamina)

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

def define_hero_luck():
    global hero_luck
    global initial_luck
    hero_luck = random.randint(1, 6) + 6
    initial_luck = hero_luck    

def test_skill():
    global skill_test
    global hero_skill
    print("testing skill ....")
    skill_test = random.randint(1, 12)
    if skill_test <= hero_skill:
        skill_test = "skillful"
    else:
        skill_test = "unskillful"

#test your luck function
def test_luck():
    global luck_test
    global hero_luck
    print("testing luck ....")
    print("your luck is", hero_luck)
    luck_test = random.randint(1, 12)
    if luck_test <= hero_luck:
        luck_test = "lucky"
    else:
        luck_test = "unlucky"
    hero_luck = hero_luck - 1
    print("your luck is now", hero_luck)

#escape function
def escape():
    global hero_stamina
    print("hero stamina is", hero_stamina)
    hero_stamina = hero_stamina - 2
    print("hero stamina is", hero_stamina)

#fights a creature with specified skill and stamina
def fight_creature(skill, stamina):
    global hero_stamina
    global hero_luck
    creature_skill = skill 
    creature_stamina = stamina
    while creature_stamina > 0 and hero_stamina > 0:
        print("hero stamina is", hero_stamina)
        print("creature stamina is", creature_stamina)
        if (hero_skill + random.randint(1, 12)
           > creature_skill + random.randint(1, 12)):
            print("You have wounded the creature")
            test_your_luck = input("test your luck? ")
            if test_your_luck is "y" and hero_luck >= random.randint(1, 12):
                print("You strike a major organ")
                creature_stamina = creature_stamina - 4
                print("your luck was", hero_luck)
                hero_luck = hero_luck - 1
                print("your luck is now", hero_luck)
            elif test_your_luck is "y" and hero_luck <= random.randint(1, 12):
                print("Your barely hit the evil creature")
                creature_stamina = creature_stamina - 1 
                print("your luck was", hero_luck)
                hero_luck = hero_luck - 1
                print("your luck is now", hero_luck)
            else: 
                creature_stamina = creature_stamina - 2
        elif (hero_skill + random.randint(1, 12)
              < creature_skill + random.randint(1, 12)):
            print("The creature has wounded you!")
            test_your_luck = input("test your luck? ")
            if test_your_luck is "y" and hero_luck >= random.randint(1, 12):
                print("The creature's barely grazes you")
                hero_stamina = hero_stamina - 1
            elif test_your_luck is "y" and hero_luck <= random.randint(1, 12):
                print("Ouch! The creature strikes a major organ!")
                hero_stamina = hero_stamina - 4 
            else: 
                hero_stamina = hero_stamina - 2
        else: 
            print("Your swords clash")
    if creature_stamina < 1: 
        print("the creature is dead")
    elif hero_stamina < 1:
        print("You have perished")
        quit()
    # how to deal with 2 on 1 scenarios

def hero_death():
    print("You died")
    exit()

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
define_hero_luck()

print(f"""

Welcome Adventurer your vital statistics are as follows

Your skill level is {hero_skill}
Your stamina level is {hero_stamina}
Your luck level is {hero_luck}
Your inital luck level is {initial_luck}
""")

fight_creatures(10, 10, 10, 10)    
