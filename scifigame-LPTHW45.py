# this is a work in process!

from os import system
import sys
import random
import fightlibrary
from textwrap import dedent

# planned improvements
# launch the sci-fi music in the background
# make bensound.com clickable
# add in something that notices if someone tries an options more than once (e.g. checking walls)

print(dedent("""
Some atmospheric sci-fi music by bensound.com.
You can either minimise or close it if you like")

Close any pictures that pop up to continue with the story
"""))

system("audacious bensoundscifi.mp3 . &")

class Dungeon_room(object):

    def enter(self):
        system("display prisoncell.jpeg")
        print(dedent("""
              You awake to find yourself in a prison. This is hardly a surprise.
              After all saboteurs are rarely given banquets in their honour and
              this is what you are. A saboteur, a spy, a ghost but one that
              signed up with their eyes wide open. You knew the risks. After the
              Veden detonated the neural bomb in your hometown, though,
              there was no going back. Thousands of people reduced 
              to hollow shells in seconds. You were having tea with
              mum and dad that day. Her scolding him about the small
              leaning tower of biscuits next to his cup and him 
              winking and smuggling another as soon as she
              looked away. Then the bomb went off and they
              just stared. Silently, unblinking. An entire town turned to
              blank slates. The United Planets called it a War Crime but
              the Veden don't understand such concepts. No matter, you thought,
              they don't need to understand they just need to pay. So you
              signed up and got to work. Four ships you've taken care of.
              You disable the engines and then the fleet moves in and 
              mops them up. This fifth was the bridge too far, though, and they 
              had been expecting you. This is not over though, you mutter
              to yourself. You'll take down fifty Veden ships before you're
              done but first you have to get out of this prison.

              You examine your surroundings. Where would you like to start.

              Choose to:

              Check the door
              Check the ceiling
              Check the floor
              Check the walls
              """))
        
        choice = ""
        
        stop_ceiling_loop = None
        while stop_ceiling_loop != "stop":
            choice = input("What would you like to do? ")
            if "door" in choice:
                print(dedent("""
                It's solid. There's no way you're getting through it.
                Plus the lock is biometric and last you checked you weren't
                even the right species for it. Choose again.
                """))
            elif "floor" in choice:
                print(dedent("""
                      The floor is reinforced steel with no joins.
                      You're going to need to find a different way out
                      """))
            elif "wall" in choice:
                print(dedent("""
                      You find some graffiti from previous guests.
                      "Bristol remembers". You catch your breath for a second
                      but this is no time for sentimentality. You must 
                      find a way out.
                      """))
            elif "ceiling" in choice:
                print(dedent("""
                      You press on the ceiling slightly and one of the tiles moves
                      Shoddy Veden craftsmanship! Too busy declaring war to learn
                      masonry. You push the tile away and see it opens 
                      into an air-vent. Checking for the guard you quickly haul 
                      yourself up and put the tile back in place. The vent is
                      dark and smells stale but you press on. Ahead you hear 
                      nervous squeaking. You crawl further forward and away 
                      from the prison ...
                      """))
                stop_ceiling_loop = "stop"
            else:
                print("That doesn't make sense. Try something else")
        return mouse

dungeon = Dungeon_room()

class Mouse_room(object):
   
    def enter(self):
        system("display mice_around_table.jpeg")
        choice = input(dedent("""
                      Crawling forward you realise the squeaking is 
                      coming from the next room below the air-vent.
                      Now you are above it and you peer cautiously
                      through the vent. From your time hauling gas
                      on the moons of Mouse World you can just about
                      make sense of the squeaks though it's
                      in a dialect you're unfamiliar with.

                      First mouse: 'With respect, we must rise up
                      General Nibbles! We've been patient but now
                      is the time for action! How many more must die
                      as we wait "till the time is right?"'

                      General Nibbles: 'I respect your fire
                      Private Basil but you're young and don't
                      remember the disastrous attack on Catus-5. We will
                      continue to wait and that is final'

                      Suddenly the vent gives way beneath your weight
                      and you find yourself amongst the startled mice.
                      They look at you and you look at them, both 
                      in shock.

                      What do you want to do:

                      - Fight the mice
                      - Explain to them you mean no harm
                      """))
        
        if "fight" in choice:
            print(dedent("""
                  You tower over the tiny mice but they are unafraid.
                  General Nibbles turns away in the ultimate sign of
                  mouse disrespect. You are an unworthy opponent for
                  such a distinguished mouse. Killing you is not, however,
                  below Private Basil who steps forward bearing her teeth
                  and shadow boxing.
                  """))
            fightlibrary.fight_creature(4, 4, "Private Basil")
            print(fightlibrary.speeches[0])
            door_choice = input(dedent("""Do you wish to enter or continue walking
                                enter/continue
                                """))
            if "enter" in door_choice:
                return experimental_lab
            else:
                print("You continue down the corridor")
                return locked_door
        elif "explain" in choice:
            print(dedent("""
                  You start to explain about how you come in peace
                  and that some of your best friends are mice but 
                  the mice look sceptical. Run a charm test to see
                  if you can persuade them.
                  """))
            print("hero charm is", fightlibrary.hero_charm)
            charm_choice = input("Press any key to start the charm test ")
            if (random.randint(1, 24) <= fightlibrary.hero_charm):
                print(dedent("""
                      General Nibbles nods slowly. 'Clearly you are a
                      friend of mice and these are indeed times when mice
                      need friends. Dark times. Our kin are held
                      against their will on this station in awful labs where
                      the Veden experiment on them and then, when their small
                      bodies can't take anymore, kill them. 

                      Friend of mice, will you help rescue our kin?
                      They are, all of them, skilled mice and can help you
                      in your own escape.'

                      You say you will do all you can to help the mouse cause.
                      You all exchange bows and then you exit by the door into
                      a corridor. There's a door in the wall of the corridor.                                       
                      """))
                corridor_choice = input("Enter the door or keep on walking? enter/continue ")
                if "enter" in corridor_choice:
                    return experimental_lab
                else:
                    return locked_door
            else:
                print(dedent("""
                These mice have been lied to before 
                and aren't inclined
                to trust strangers. General Nibbles 
                starts ranting about assassins and before
                you can calm him down, Private Basil
                launches her tiny frame at your face 
                screaming the thousand year
                old war cry of her people. For better or worse you will
                need to fight this mouse. General Nibbles refuses to engage
                for you are too lowly for his dagger. As Private Basil attacks
                she starts chanting in a low voice
                """))
                fightlibrary.fight_creature(4, 4, "Private Basil")
                print(fightlibrary.speeches[0])
                door_choice = input(dedent("""Do you wish to enter or continue walking
                                enter/continue
                                """))
                if "enter" in door_choice:
                    return experimental_lab
                else:
                    print("You continue down the corridor")
                    return locked_door


        else:
            print("that doesn't make sense")
            
        
mouse = Mouse_room()

class experiment_lab(object):

    def enter(self):
        print(dedent("""
        You find yourself in some sort of experimental lab.
        There's no Veden here but there's a small mouse in the corner
        in a cage. The key lies on a table in the middle of the room
        upon which there's also a strange looking gun and a armoured
        bracelet. There's only space in your jacket for one of these
        """))
        carry_choice = input(dedent("""
                       Which/who would you like to take 
                       with you? mouse/gun/bracelet? """))
        if "mouse" in carry_choice:
            fightlibrary.coat_pockets["side_pocket"] = "Old Jake" 
            print(dedent("""
            You turn the key and release the mouse from the cage. The mouse
            is weak and weary but manages to find his voice
            Many thanks for my release stranger my name is Old Jake.
            Many torments have myself and my kin suffered at the hands
            of the Veden in the name of science but that will
            soon be over. The Prophets spoke of the coming
            of the Meepishan who will deliver us from bondage. When
            we dance on the bones of our enemies, you will be an honoured guest
            at the feast. First, though, we must get you off this ship. Let us
            make haste!'

            You tuck Old Jake in your side pocket and continue on
            down the corridor where you find yourself at a dead end
            with a locked door in front of you
            """))
            return locked_door
        elif "gun" in carry_choice:
            fightlibrary.coat_pockets["side_pocket"] = "veden gun" 
            print(dedent("""
            What the Veden lack in culture they make up for in weaponry.
            This gun likely packs a punch. You put it in your side pocket
            and continue on down the corridor where you find yourself
            at a dead end with a locked door in front of you
            """))
            return locked_door
        elif "bracelet" in carry_choice:
            fightlibrary.coat_pockets["side_pocket"] = "bracelet" 
            print(dedent("""
            Veden armour is universe renown. You suspect this will come in use later
            
            You continue on down the corridor where you find yourself
            at a dead end with a locked door in front of you
            """))
            return locked_door
        else:
            print(dedent("""
            You babble incoherently to yourself and then leave
            the room. 

            You continue on down the corridor where you find yourself
            at a dead end with a locked door in front of you
            """))
            return locked_door
        
experimental_lab = experiment_lab()

class lock_door(object):

    def enter(self):
        print(dedent("""
        The door is solid steel so you've no hope of
        blasting your way through it. There's a keypad
        and you'll have to guess the passcode. Above the
        keypad you see an old tattered yellow sticky note.
        There's four numbers on there but you can only
        make out the first (a one) and the last (a four).
        
        A bead of sweat falls down your brow as you remember
        that Veden keypads only allow 20 attempts before taking
        "counter-measures"
        """))
        for x in range(20):
            keypad_choice = input("Guess the entry code ")
            print(keypad_choice)
            if keypad_choice == "1234":
                print("The door swings open ...")
                return veden_guard
            else:
                print("Nope that's not it. Try again")
        print(dedent("""
        You hear a small hissing noise and poison gas releases from
        the top of the door. As you remembered, it seems the
        Veden set it as a security measure to stop unlimited
        guessing. You die choking.
        """))
        sys.exit()

locked_door = lock_door()

class veden(object):

    def enter(self):
        print(dedent("""
        On the other side of the door is a Veden Guard!
        You must fight!
        """))
        fightlibrary.fight_creature(6, 6, "Door Guard")
        print(dedent("""
        Bruised and bloodied you stumble past the Veden's lifeless
        body. Every inch of you is tired but there is no time for
        rest. You hear shouts from the corridor behind you and start running.
        The corridor forks left and right. 
        """))
        stop_loop = None
        while stop_loop != "stop":
            choice_corridor_fork = input(dedent("""
            right or left?
            """))
            if "right" in choice_corridor_fork:
                stop_loop = "stop"
                return shuttlebay   
            elif "left" in choice_corridor_fork:
                stop_loop = "stop"
                return gun_turret_place
            else:
                print(dedent("""
                that doesn't make sense. Please choose
                left or right
                """))

veden_guard = veden()

class gun_turret(object):

    def enter(self):
        print(dedent("""
        An alarm goes off and a machine gun turret appears out of
        the ceiling. You hide behind some storage containers and try
        to disable it
        """))
        fightlibrary.fight_turret(10, 4, "Gun Turret")
        print(dedent("""
        The corridor curves around to the right and you follow it.
        """))
        return shuttlebay
        
gun_turret_place = gun_turret()

class shuttle_bay(object):

    def enter(self):
        print(dedent("""
        You reach the shuttle bay and burst through the doors.
        There's no one to stop you so you jump into the first
        craft you see and blast off into space. No sooner have you
        launched but you seen 3 Veden fighters burst out of the mothership
        in hot pursuit. Suddenly you hear a beeping come from your dashboard
        and you look down to see the following message on all screens.

        'Death to the Veden! Blessed is the Meepishan who will deliver
        mice from their tormentors'

        You are not sure what is happening but feel confident that it 
        is not good ...

        """))
        input("press any key to continue ...")
        if fightlibrary.coat_pockets["side_pocket"] == "Old Jake":
            return final
        else:
            print(dedent("""
            Your timing is not great my friend.
            The mice aboard the Veden ship have risen
            up against their captors and have rigged all the
            fighter ships to explode upon acceleration. Your
            sweetest moment of escape is also your last. It
            happens so quickly you never notice. Your last
            thought is whether you might get back to Bristol
            in time for the football this weekend. You will
            not be back because you, your ship and the pursuing
            Vedens are instantly vaporised.
            """))
            sys.exit()
            

shuttlebay = shuttle_bay()

class Final_room(object):

    def enter(self):
        print(dedent("""
        No soon do you hear the beeping than old Jake awakes
        
        'Let me take care of this' he says and starts typing
        on the keyboard.

        Unknown to you the mice aboard the Veden ship had rigged
        all the fighter ships to explode upon acceleration. Luckily
        for you, your small companion knows the override code.

        The Vedden ships in pursuit are not so lucky and explode
        behind you one after the other.

        You hit light speed, smile at Old Jake and realise you
        have time to make it back to Bristol in time for the football this weekend.

        Beside you Old Jake looks far into the darkness and nods
        slowly.

        'So it begins ...'
        
        """))
        system("audacious bensoundscifi.mp3 . &")
        sys.exit()
    
final = Final_room()

class Runner(object):

    def loop_through_rooms(self):
        next_room = dungeon.enter()
        while 1 != 2:
            store = next_room.enter()
            next_room = store


Run = Runner()
Run.loop_through_rooms()

