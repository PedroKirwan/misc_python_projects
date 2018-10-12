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

#Eating a provision
def use_provision():
    global provisions
    global hero_stamina
    provisions = provisions - 1
    hero_stamina = hero_stamina + 4
    if hero_stamina > initial_stamina:
        hero_stamina = initial_stamina
    else:
        hero_stamina = hero_stamina

#increase luck
def increase_luck(amount):
    global hero_luck
    print("your luck was", hero_luck)
    hero_luck = hero_luck + amount
    if hero_luck > initial_luck:
        hero_luck = initial_luck
    else:
        pass
    print("your luck is now", hero_luck)

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
        if hero_skill + random.randint(1, 12) > creature_skill + random.randint(1, 12):
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
        elif hero_skill + random.randint(1, 12) < creature_skill + random.randint(1, 12):
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
        condition1 =  (i % 2) == 0 and creature1_stamina > 0 and hero_stamina > 0
        condition2 = creature2_stamina < 1 and creature1_stamina > 0 and hero_stamina > 0
        condition3 =  (i % 2) != 0 and creature2_stamina > 0 and hero_stamina > 0
        condition4 = creature1_stamina < 1 and creature2_stamina > 0 and hero_stamina > 0
        condition5 = creature1_stamina < 1 and creature2_stamina < 1 and hero_stamina > 0
        if condition1 or condition2:
            print("hero stamina is", hero_stamina)
            print("creature1 stamina is", creature1_stamina)
            if hero_skill + random.randint(1, 12) > creature1_skill + random.randint(1, 12):
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
            elif hero_skill + random.randint(1, 12) < creature1_skill + random.randint(1, 12):
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
        elif condition3 or condition4:        
            print("hero stamina is", hero_stamina)
            print("creature2 stamina is", creature2_stamina)
            if hero_skill + random.randint(1, 12) > creature2_skill + random.randint(1, 12):
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
            elif hero_skill + random.randint(1, 12) < creature2_skill + random.randint(1, 12):
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

def page_33():
    print("""
    The sleeping creature awakens startled- He jumps
    up and rushes at you, unarmed. With your sword
    you should be able to defeat him, but his sharp teeth
    look rather vicious You may escape through the
    door (turn to 32o) or stand and fight the ORC who
    is attacking you.
    ORC SKILL 6 STAMINA 4
    If you defeat the creature, you may take the box.
    Tum to 147.
    """)
    choice = input("Do you wish to escape: y/n ")
    if choice is "y":
        escape()
        page_320()
    else:
        fight_creature(6, 4)
        print("You may take the box")
        page_147()

def page_71():
    print("""
    There is a right-hand turn to the north in the Passage.
    Cautiously you: approach a sentry Post on the
    comer and, as you look in, you can see a strange
    Goblin-like creature in leather armour asleep at his
    post. You hy to tiptoe past him. Test your Luck lt
    you are Lucky, he does not wake up and remains
    snoring loudly turn to 301. lf you are unlucky, you
    step with a crunch on some loose ground and his
    eyes flick open - turn to 248.		
    """)
    test_luck()
    if luck_test is "lucky":
        print("The goblin remains asleep")
        page_301()
    elif luck_test is "unlucky":
        print("The goblin is awake!")
        page_248()
        
def page_82():
    print("""
    The door opens to reveal a small smelly room. In
    the centre of the room is a rickety wooden table on
    which stands a lit candle. Undeneath the table is a
    small wooden box. Asleep on a strawm mattress in the
    far corner of the room is a short, stocky creature
    with an ugly, warty face; the same sort of creature
    that you found asleep at the sentry post. He must be
    the guard for the night watch. You may either
    return to the corridor and press on northwards (turn
    to 208) or creep into the room and try to take the box
    without waking the creature. If you want to try to
    steal the box, Testy your luck. If you are Lucky, he
    does not wake up - turn to 147. If you are Unlucky,
    turn to 33
    """)
    choice = input("choose to 'press on' or to 'steal' the box: ")
    if "press" in choice:
        page_208()
    else:
        test_luck()
        if luck_test is "lucky":
            page_147()
        else:
            page_33()

def page_92():
    print("""
    You arrive back at the junction in the passage. You look left to see the cave entrance in the dim distance but walk straight on
    """)
    page_71()

def page_116():
    print("""
    The two drunken ORCS you now face are obviously
    startled at your entrance and, as quickly as
    they are able, they fumble around for the weapons.
    You must attack each one in turn. Their drunkenness allows you 
    to add 1 point to your dice roll when
    rolling to work out your Attack Strength, during
    each Attack Round

    First ORC SKILL 5 STAMINA 4
    Second ORC SKILL 5 STAMINA 5

    lf you win the battle. turn to 378 If you wish to
    Escape during the battle, you may do so by turning to
    42
    """)

def page_145():
    print("""
    The box has fallen to the ground during you! fight
    with the Snake and out of it has fallen a bronze coloured
    key with the number 99 carved into it. You
    may take this key with you (note it on your Equipment
    List) and leave the room Add 1 luck point
    and turn to 363.
    """)
    increase_luck(1)
    equipment.append("key99")
    #adds number 99 key to equipment list
    #needs tweaked to allow luck to increase 1 above initial?

def page_147():
    print("""
    You leave the room and open the box in the passage
    inside you find a single piece of gold and a small
    mouse, which must have been the creature's pet.
    You keep the coin and release the mouse, which
    scurries of down the passageway. Gain 2 luck
    points and turn to 208.
    """)
    increase_luck(6)
    page_208()
    #need to add a gold coin here
    
#incompletei
def page_156():
    print("""
    You charge the door with your shoulder. Roll two
    dice. If the number lolled is less than or equal to
    your skill score, you succeed - turn to 343. If the
    number rolled is greater than your skill. you rub
    your bruised shoulder and decide against trying
    again. Turn to 92 to retum to the junction
    """)
    test_skill()
    if skill_test is "skillful":
        print("You successfully charge the door!")
        page_343()
    else:
        print("Ouch! ... well that was stupid. You return to the junction")

def page_157():
    print("""
    The door opens into an east-west passage, which
    turns north after several metres. To follow this
    direction, turn to 4. lf you decide against going
    through the door, turn to 329.
    """)
    choice = input("Go through the door? y/n: ")
    if "y" or "yes" in choice:
        page_4()
    else:
        page_329()

def page_208():
    print("""
    Further up the passage along the west wall you see
    another door. You listen at it but hear nothing if
    you want to try opening the door, turn to 397. If you
    want to continue northwards, turn to 363
    """)
    choice = input("Enter 'open' to open the door or 'north' to continue northwards: ")
    if "open" in choice:
        page_397()
    else:
        page_363()

def page_240():
    print("""
    The box is light, but something rattles within. You
    open the lid and a small SNAKE darts out to bit at
    your wrist! You must fight the Snake-
    
    SNAKE skill 5 stamina 2
    
    if you kill the Snake, turn to 145.
    """)
    fight_creature(5, 2)
    page_145()

def page_248():
    print("""
    The creature that has just awakened is an ORC! He scrambles to his feet and turns to grasp at a rope which is probably the alarm bell. You must     attack him quickly.
    """)
    fight_creature(6, 5)
    print("congratulations you survived. You continue up the passageway")
    page_301()

def page_278():
    print("""
    The passageway soon comes to an end at a locked
    wooden door. You listen at the door but hear
    nothing. W l you try to charge the door down? lf so
    turn to 156. II you would rather turn round and go
    back to the junction, turn to 92
    """)
    choice = input("enter y to charge down the door. Enter any other key to go back")
    if "y" in choice:
        page_156()
    else:
        page_92()

def page_301():
    print("""
    To your left, on the westface of the passage, there is
    a rough-cut wooden door. You listen at the door
    and can hear a rasping sound which may be some
    sort of creature snoring. Do you want to open the
    door? lf so, turn to 82. lf you wish to press on
    northwards, turn to 208.
    """)
    choice = input("choose to 'open' or press any other key to press on: ")
    if "open" in choice:
        page_82()
    else:
        page_208()

def page_343():
    print("""
    The door burst open and you fall headlong into a room. But your heart jumps as you realize you are not landing on the floor,
    but plunging down a pit of some kind! Luckily the pit is not particularly deep
    and you land in a heap less than two metres down.
    Lose 1 stamina point for your bruises, climb out
    of the pit into the room and leave through the door,
    heading westwards. Turn to 92.
    """)
    decrease_stamina(1)
    page_92()

def page_363():
    print("""
    Further up the passage on the wesr wall you see
    another similar door You listen at the door and
    grimace to hear the worst singing you have ever
    heard in your Life. Do you want to go into the room
    to investigate this hideous din (turn to 370) or walk
    on up the passageway (turn to 42)?
    """)
    choice = input("enter a page number: ")
    if choice is "370":
        page_370()
    else:
        page_42()

def page_370():
    print("""
    The door opens to reveal a small room. The room is
    dirty and unkempt. A straw matttess lies in one
    comer. In the centre of the room is a wooden table
    upon which a candle burns, lighting the room with
    its flickering flame. A small box rests under the
    table. Seated around the table are two small
    creatures with warty skin, dressed in leather
    arfilour. They are drinking some sort of grog and by
    the way they stagger to their feet on your arrival,
    you assume they are very drunk. You may either
    draw your sword and leap forward at them (turn to
    116) or slam the door quickly and run on up the
    Passage (turn to 42)
    """)
    choice = input("enter a page number: ")
    if choice is "116":
        page_116()
    else:
        page_42

def page_397():
    print("""
    The door opens to reveal a small room with a stone
    floor and dirty walls. There is a stale smell in the air.
    In the centre of the room is a makeshift wooden
    table on which is standing a lit candle. Under the
    table is a small box. ln the far corner of the room is a
    straw mathess. You may either open the box (turn
    to 240) or leave the room (turn to 363).
    """)
    choice = input("Do you want to open the box y/n? ")
    if "y" in choice:
        page_240()
    else:
        page_363()

#The adventure begins!

define_hero_skill()
define_hero_stamina()
define_hero_luck()

fight_creatures(5, 5, 5, 4)

print(f"""

Welcome Adventurer your vital statistics are as follows

Your skill level is {hero_skill}
Your stamina level is {hero_stamina}
Your luck level is {hero_luck}
Your inital luck level is {initial_luck}
""")

print("""
Rumours

Only a foolhardy adventurer would embark upon
such a pedlous quest without first finding out as
much as possible about the mountain and its treasures.
Before your anival at the foot of Firetop Mountain,
you spent several days with the townsfolk of a
local village some two days journey from the base.
Belng a likeable sort of person, you found it easy to
get on with the local peasants. Although they told
many stories about the mysterious Warlock's sanctuary,
you could not feel sure that all - or indeed any
-of these were based on fact. The villagers had seen
many adventurers pass through on their way to the
mountain, but very few ever returned. The journey
ahead was extremely dangerous, that you knew for
certain. Of those who returned to the village, none
contemplated going back to Firetop Mountain.

There seemed to be some truth in the rumour that
the Warlock's treasure was stored in a magnificent
chest with two locks, and the keys to these locks
were guarried by various creatures within the
dungeons. The Warlock himself was a sorcerer of
great power. Some described hrm as old, others as
young. Some said hrs power came from an
enchanted deck of cards, others lrom the silky black
gloves that he wore.

The entrance to the mountain was guarded by a
pack of warty-faced Goblins, stupid creatures, fond
of their food and drink. Towards the inner chambers,
the creatures became more fearsome. To reach
the inner chambers you would have to cross a river
The ferry service was regular but the ferryman
enjoyed a good barter, so you should save a Gold
Piece for the trip. The locals also encouraged you to
keep a good map of your wanderings, for without a
map you would end up hopelessly lost within the
mountain.

When it finally came to your day of leaving, the
whole village tumed out to wish you a safe journey.
Tears came to the eyes of many of the women,
young and old alike. You couldn't help wondering
whether they were tears of sorrow shed by eyes
which would never see you alive again . . .

""")

#1

print("""
At last your two-day hike is over, You unsheath
your sword, lay it on the ground and sigh with relief
as you lower your self down on to the mossy rocks to
sit for a moment's rest. You stretch, rub your eyes
and finally look up at Firetop Mountarn.

The very mountain itself looks menacing. The steep
face in front of you looks to have been savaged by
the claws of some gargantuan beast. Sharp rocky
crags jut out at unnatural angles. At the top of the
mountain you can see the eerie red colouring -
probably some strange vegetation - which has given
the mountain its name. Perhaps no one will ever
know exactly what grows up there, as climbing the
peak must surely be impossible.

Your quest lies ahead of you. Across the clearing is a
dark cave entrance. You pick uP your sword, get to
your feet and consider what dangers may lie ahead
of you. But with determination, you thrust the
sword home into its scabbard and approach the cave.

You peer into the gloom to see dark, slimy walls
with pools of water on the stone floor in front of
you. the air is cold and dank. You lightyour lantern
and step wadly into the blackness. Cobwebs brush
your face and you hear the scurrying of tiny feet:
rats, most likely, You set off into the cave. After a
few yards you arrive at a iunction. Will you turn
west (turn to 71) or east (turn to 278)?
""")

page_turn = input("will you go east or west ")

if page_turn == "west":
    page_71()
elif page_turn == "east":
    page_278()
else:
    print("I don't understand. Please enter east or west") 

     
