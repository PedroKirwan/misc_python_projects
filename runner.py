class Runner(object):

    def loop_through_rooms(self):
        next_room = dungeon.enter()
        while next_room != final:
            store = next_room.enter()
            next_room = store

Run = Runner()
