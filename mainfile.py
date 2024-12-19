import random

class HorrorAdventureGame:
    def __init__(self):
        self.state = "start"
        self.outcome = ""
        self.inventory = []

    def start_game(self):
        self.state = "dark_room"
        self.outcome = "You wake up in a dark room with no memory of how you got there. The air is thick with a musty smell.\n" \
                       "You see a faint light in the distance. Do you:\n1. Move toward the light\n2. Stay in the dark room"
        return self.outcome, ["Move toward the light", "Stay in the dark room"]

    def move_toward_light(self):
        self.state = "creepy_hallway"
        self.outcome = "You walk cautiously toward the light, only to find yourself in a long, creepy hallway. You hear faint whispers.\n" \
                       "Do you:\n1. Enter the first door you see\n2. Keep walking down the hallway"
        return self.outcome, ["Enter the first door", "Keep walking down the hallway"]

    def stay_in_dark_room(self):
        self.state = "haunted_room"
        self.outcome = "You stay in the room, but suddenly the door slams shut behind you. The temperature drops.\n" \
                       "Do you:\n1. Try to open the door\n2. Search for an escape route"
        return self.outcome, ["Try to open the door", "Search for an escape route"]

    def enter_first_door(self):
        self.state = "locked_room"
        self.outcome = "You enter the first door and find yourself in a small, locked room. There's a strange object on the table.\n" \
                       "Do you:\n1. Inspect the object\n2. Search for a key"
        return self.outcome, ["Inspect the object", "Search for a key"]

    def keep_walking(self):
        self.state = "demonic_figure"
        self.outcome = "As you continue walking, you see a demonic figure blocking the end of the hallway. It grins menacingly.\n" \
                       "Do you:\n1. Confront the figure\n2. Turn around and run"
        return self.outcome, ["Confront the figure", "Turn around and run"]

    def try_open_door(self):
        self.state = "game_over"
        self.outcome = "You try to open the door, but it bursts open by itself! A dark figure stands in the doorway.\n" \
                       "Before you can react, it grabs you. Game Over!"
        return self.outcome, []

    def search_escape_route(self):
        self.state = "escape_success"
        self.outcome = "You find a secret escape hatch behind a piece of furniture and crawl through it, escaping the room.\n" \
                       "Congratulations, you survived!"
        return self.outcome, []

    def inspect_object(self):
        self.state = "haunted_doll"
        self.outcome = "You inspect the object on the table, which turns out to be a haunted doll. Its eyes follow you.\n" \
                       "Do you:\n1. Touch the doll\n2. Leave the room and try another door"
        return self.outcome, ["Touch the doll", "Leave the room"]

    def search_for_key(self):
        self.state = "found_key"
        self.outcome = "You find a rusty key hidden beneath the floorboards. You unlock the door and leave the room.\n" \
                       "You escape safely, for now."
        return self.outcome, []

    def confront_figure(self):
        self.state = "game_over"
        self.outcome = "You confront the figure, but it suddenly disappears. You're left in darkness.\n" \
                       "Something grabs your ankle. Game Over!"
        return self.outcome, []

    def run_away(self):
        self.state = "game_over"
        self.outcome = "You run away from the demonic figure, but it chases you relentlessly. You stumble and fall, breaking your neck. Game Over!"
        return self.outcome, []

    def touch_doll(self):
        self.state = "game_over"
        self.outcome = "You touch the doll, and its eyes glow red. Suddenly, it comes to life and attacks you. Game Over!"
        return self.outcome, []

    def leave_room(self):
        self.state = "creepy_hallway"
        self.outcome = "You leave the room and return to the hallway, unsure of what awaits you next.\n" \
                       "Do you:\n1. Keep walking forward\n2. Turn back and go the other way"
        return self.outcome, ["Keep walking forward", "Turn back and go the other way"]
