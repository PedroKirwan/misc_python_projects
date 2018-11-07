# this is a work in proress!


import random

class Dungeon_room(object):

    def enter(self):
        print("Welcome to dungeon room")
        return mouse

dungeon = Dungeon_room()

class Mouse_room(object):
   
    def enter(self):
        print("Welcome to the Mouse Room")
        return third

mouse = Mouse_room()

class Third_room(object):

    def enter(self):
        print("welcome to the third room")
        return fourth

third = Third_room()

class Fourth_room(object):

    def enter(self):
        print("welcome to the Fourth room")
        return final

fourth = Fourth_room()

class Final_room(object):
    pass

final = Final_room()

class Runner(object):

    def loop_through_rooms(self):
        next_room = dungeon.enter()
        while next_room != final:
            store = next_room.enter()
            next_room = store

Run = Runner()
Run.loop_through_rooms()


"""


        next_room = dungeon
        while next_room != "final_room":
            next_room.enter()

    print("It has come out of the loop now")

"""
