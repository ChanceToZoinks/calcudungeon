#!/usr/bin/env python3
from __future__ import annotations
import os
import random
try:  # readline doesnt work on windows apparently
    import readline
except:
    pass
from typing import Any, Dict, Tuple
import shlex

from pyfiglet import Figlet


places = (
    "field",
    "house",
    "ice cream parlor",
    "dungeon",
    "movie theater",
    "haunted house",
    "graveyard",
    "board room",
    "zoom meeting",
    "call with your product manager",
    "White House",
    "Among Us game",
)
place_adjectives = (
    "well lit",
    "musty",
    "boring",
    "bright",
    "dark",
    "misty",
    "spooky",
    "dark and foreboding",
    "bright and sunny",
    "colorful",
)
transitions = (
    "You stumble into a",
    "You walk into a",
    "You find yourself in a",
    "You enter into a",
    "You're now in a",
)
objects = (
    "apples",
    "oranges",
    "bananas",
    "gold dubloons",
    "diamonds",
    "dollars",
    "Obamas",
    "rocketships",
)
object_holders = (
    "a heap of",
    "a bunch of",
    "a barrel of",
    "a chest full of",
    "a mountain of",
    "a sack of",
    "a shitload of",
    "a whole lot of",
    "a gargantuan amount of",
    "a few",
    "some",
)
directions = ("north", "south", "east", "west")
direction_opposites = {
    "north": "south",
    "south": "north",
    "east": "west",
    "west": "east",
}
in_front = ("In front of you lies", "Before you there lies", "You see")

quit_cmds = (
    "q",
    "quit",
    "i quit",
    "donezo",
    "finito",
    "im over it",
    "ive had enough",
    "im out",
    "get me out",
    "fuck this",
    "take me home",
    "leave",
    "leave dungeon",
    "kill me",
    "compute",
    "calculate",
    "equals",
)
take_commands = (
    "grab",
    "yoink",
    "snatch",
    "take",
    "carry away",
    "requisition",
    '"borrow"',
    "'borrow'",
    "steal",
    "pick up",
)
move_commands = (
    "go",
    "go to",
    "walk",
    "move",
    "head",
    "trot",
    "scurry",
    "prance",
    "set forth",
)
inspect_commands = ("look", "inspect", "search", "check out", "peep", "observe")
describe_words = (
    "describe",
    "tell me",
    "sing to me",
    "tell me about this place",
    "where am I",
    "where is this",
    "what is this place",
)
inventory_words = ("how many", "bag", "inventory", "sack", "backpack", "holding")
random_events = (
    "A boulder fell on your head!",
    "You hear a click and suddenly spikes shoot out of the floor and impale your feet!",
    "A snake bit you!",
    "You tripped, fell and twisted your ankle!",
    "A witch cast a spell on you!",
    "A goblin beat you up and took your lunch money!",
    "A spider bit you!",
    "You got called in on your day off!",
    "A test failed--you have to rewrite that code!",
)


class WordBundle:
    def __init__(self) -> None:
        self.P = random.choice(places)
        self.A = random.choice(place_adjectives)
        self.T = random.choice(transitions)
        self.O = random.choice(objects)
        self.H = random.choice(object_holders)
        self.F = random.choice(in_front)

    @classmethod
    def wb_template(cls, msg: str, wb: WordBundle) -> str:
        return (
            msg.replace("@A", wb.A)
            .replace("@T", wb.T)
            .replace("@P", wb.P)
            .replace("@O", wb.O)
            .replace("@H", wb.H)
            .replace("@F", wb.F)
        )

    def __repr__(self) -> str:
        return f"WordBundle(P={self.P}, A={self.A}, T={self.T}, O={self.O}, H={self.H}, F={self.F})"


class Room:
    def __init__(
        self,
        _room_bundle: WordBundle,
        _directions: Dict[str, WordBundle],
        _random_event: bool,
        _symbol_map: dict,
    ) -> None:
        self.wb = _room_bundle
        self.entry = {"desc": WordBundle.wb_template("@T @A @P.", _room_bundle)}
        self.directions = {}
        for direction in directions:
            self.directions[direction] = {
                "wb": _directions[direction],
                "desc": WordBundle.wb_template(
                    f"To your {direction} is a @P. You think you see a {_symbol_map[direction]} sign as well.",
                    _directions[direction],
                ),
            }
        self.center = {"desc": WordBundle.wb_template("@F @H @O.", _room_bundle)}
        self.random_event = _random_event

    def __str__(self) -> str:
        _ = f"{self.entry['desc']}\n"
        for d, v in self.directions.items():
            _ += f"{v['desc']}\n"
        _ += self.center["desc"]
        return _

    def __repr__(self) -> str:
        return f"""
            Room(
                wb={self.wb},
                entry={self.entry},
                north={self.directions["north"]},
                south={self.directions["south"]},
                east={self.directions["east"]},
                west={self.directions["west"]},
                center={self.center},
                random_event={self.random_event}
            )
        """


class Point:
    def __init__(self, _xy: Tuple[int, int]) -> None:
        self.x, self.y = _xy

    def get_adj(self) -> Dict[str, Point]:
        _ = {}
        _["north"] = Point((self.x, self.y + 1))
        _["south"] = Point((self.x, self.y - 1))
        _["east"] = Point((self.x + 1, self.y))
        _["west"] = Point((self.x - 1, self.y))
        return _

    def get_diff(self, other: Point) -> Point:
        return Point((other.x - self.x, other.y - self.y))
    
    @classmethod
    def diff_to_dir(cls, diff: Point) -> str:
        diff_map = {
            Point((0,1)): "north",
            Point((0,-1)): "south",
            Point((1,0)): "east",
            Point((-1,0)): "west"
        }
        return diff_map[diff]


    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Point):
            return __o.x == self.x and __o.y == self.y
        else:
            raise TypeError(f"Unsupported type for comparison with Point: {type(__o)}")

    def __hash__(self) -> int:
        return hash((self.x, self.y))


class Dungeon:
    def __init__(self, _symbol_map: dict) -> None:
        start_dir_dict = {dir: WordBundle() for dir in directions}
        self.current_point = Point((0, 0))
        self.symbol_map = _symbol_map
        self.map: Dict[Point, Room] = {
            self.current_point: Room(
                WordBundle(), start_dir_dict, self._random_event(), self.symbol_map
            )
        }
        self.current_room = self.map[self.current_point]
        self.path: list[Point] = []
        self.path.append(self.current_point)
        self.grabbed_items: Dict[
            Point, float
        ] = {}  # {Point: number of items taken at that point}
        self.grabbed_items[self.current_point] = 0
        self._generate_adj_rooms(self.current_point)

    def _generate_adj_rooms(self, _point: Point) -> None:
        adj_points = _point.get_adj()
        for dir, point in adj_points.items():
            this_room = self.map[_point]
            if point in self.map:
                pass
            else:
                next_room_bundle = this_room.directions[dir]["wb"]
                next_room_dir_dict = {dir: WordBundle() for dir in directions}
                next_room_dir_dict[direction_opposites[dir]] = this_room.wb
                self.map[point] = Room(
                    next_room_bundle,
                    next_room_dir_dict,
                    self._random_event(),
                    self.symbol_map,
                )

    def _random_event(self, prob: float = 0) -> bool:
        return random.random() <= prob

    # the map is not a grid there is no notion of distance so (east -> north) and (north -> east) wont take you to the same place
    def move(self, direction: str) -> None:
        self.current_point = self.current_point.get_adj()[direction]
        self.path.append(self.current_point)
        self._generate_adj_rooms(self.current_point)
        self.current_room = self.map[self.current_point]
        self.grabbed_items[self.current_point] = 0

    def take(self, amount: float) -> None:
        self.grabbed_items[self.current_point] += amount

    def lookdir(self, direction: str, symbol_map: dict) -> str:
        _ = self.current_point.get_adj()[direction]
        __ = self.current_point.get_diff(_)
        return self.map[self.current_point].directions[direction]["desc"]

    def lookobj(self) -> str:
        return self.map[self.current_point].center["desc"]

    def get_random_path_point(self, exclude_end=True) -> Point:
        if exclude_end:
            return random.choice(self.path[0:-1])
        else:
            return random.choice(self.path)

    def __repr__(self) -> str:
        return f"Dungeon(map={self.map}, path={self.path})"


class Game:
    def __init__(self) -> None:
        math_symbols = ["+", "*", "-", "/"]
        random.shuffle(math_symbols)
        self.math_symbol_map = {
            "north": math_symbols[0],
            "south": math_symbols[1],
            "east": math_symbols[2],
            "west": math_symbols[3],
        }
        self._start_game()

    def _show_startup_logo(self) -> None:
        os.system("cls||clear")
        self._display_ascii_text("Calcu-dungeon\n")

    def _display_ascii_text(self, text: str, font: str = "slant") -> None:
        try:
            print(Figlet(font).renderText(text))
        except:  # exe bundling is completely fucked with pyfiglet and im not trynna fix it
            pass

    def _isfloat(self, thing: Any) -> bool:
        try:
            float(thing)
            return True
        except:
            return False

    def _describe_room(self, room: Room) -> None:
        print("-------------------\n" + str(room) + "\n-------------------")

    def _describe_inventory(self) -> None:
        _ = "You are holding "
        i = 1
        for point, amount in self.dungeon.grabbed_items.items():
            _ += f"{amount} {self.dungeon.map[point].wb.O}"
            if len(self.dungeon.grabbed_items.keys()) > i:
                _ += " and "
            i += 1
        print(_ + ".")
        print("-------------------")

    def _compute(self) -> float:
        _ = ""
        for i in range(l := len(self.dungeon.path)):
            _ += str(self.dungeon.grabbed_items[self.dungeon.path[i]])
            if i + 1 < l:
                diff = self.dungeon.path[i].get_diff(self.dungeon.path[i + 1])
                _ += self.math_symbol_map[Point.diff_to_dir(diff)]
        return eval(_)

    def _prompt(self, msg: str) -> str:
        return input(f"{msg}\n> ")

    def _start_game(self) -> None:
        self._show_startup_logo()
        self.dungeon = Dungeon(self.math_symbol_map)
        self._describe_room(self.dungeon.current_room)
        self._main_loop()

    def _main_loop(self) -> None:
        while True:
            try:
                cmd, *args = shlex.split(
                    self._prompt("What would you like to do?").lower()
                )
            except ValueError:  # im a merciful god i wont stop ctrl + c from working
                continue

            if cmd in quit_cmds:
                self._describe_inventory()
                print(f"In total that leaves you with {self._compute()} items!")
                break
            elif cmd in inspect_commands:
                target = args[0]
                if target in directions:
                    print(self.dungeon.lookdir(target, self.math_symbol_map))
                elif target in self.dungeon.current_room.wb.O:
                    print(self.dungeon.lookobj())
            elif cmd in take_commands:
                num, target = args
                if (
                    self.dungeon.current_room.wb.O.lower() in target
                    or target in self.dungeon.current_room.wb.O.lower()
                ) and self._isfloat(num):
                    self.dungeon.take(float(num))
                    print(f"You {cmd} {num} {self.dungeon.current_room.wb.O}.\n-------------------")
            elif cmd in move_commands:
                direction = args[0]
                if direction in directions:
                    print(f"You {cmd} {direction}.")
                    self.dungeon.move(direction)
                    if self.dungeon.current_room.random_event:
                        _ = self.dungeon.get_random_path_point()
                        print(
                            f"Uh oh! {random.choice(random_events)} You lost half your {self.dungeon.map[_].wb.O}."
                        )
                        self.dungeon.grabbed_items[_] /= 2
                    self._describe_room(self.dungeon.current_room)
            elif cmd in describe_words:
                self._describe_room(self.dungeon.current_room)
            elif cmd in inventory_words:
                self._describe_inventory()
            elif cmd in ("help", "h", "help me"):
                print("lol nah\n-------------------")


if __name__ == "__main__":
    g = Game()
    input("Press any key to close window.")
