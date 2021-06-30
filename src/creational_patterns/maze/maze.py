import abc
from abc import ABC
from enum import Enum
from typing import List
from typing import Optional


class MapSite(ABC):
    @abc.abstractmethod
    def enter(self) -> None:
        pass


class Direction(Enum):
    North = 0
    East = 1
    South = 2
    West = 3


class Room(MapSite):
    sides: List[List[MapSite]] = [[], [], [], []]

    def __init__(self, room_no: int):
        self.room_no: int = room_no

    def get_side(self, direction: Direction) -> MapSite:
        return self.sides[direction.value][0]

    def set_side(self, direction: Direction, site: MapSite) -> None:
        self.sides[direction.value] = [site]

    def enter(self) -> None:
        pass


class Wall(MapSite):
    def enter(self) -> None:
        pass


class Door(MapSite):
    def __init__(self, room_one: Room, room_two: Room):
        self._room_one = room_one
        self._room_two = room_two
        self._is_open = False

    def enter(self) -> None:
        pass


class Maze:
    rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def room_no(self, n: int) -> Optional[Room]:
        for room in self.rooms:
            if room.room_no == n:
                return room

        return None


def create_maze() -> Maze:
    a_maze = Maze()

    r1 = Room(1)
    r2 = Room(2)

    a_maze.add_room(r1)
    a_maze.add_room(r2)

    r1.set_side(Direction.North, Wall())
    r1.set_side(Direction.South, Wall())
    r1.set_side(Direction.East, Wall())
    r1.set_side(Direction.West, Wall())

    r2.set_side(Direction.North, Wall())
    r2.set_side(Direction.South, Wall())
    r2.set_side(Direction.East, Wall())
    r2.set_side(Direction.West, Wall())

    return a_maze


if __name__ == '__main__':
    maze = create_maze()
    print(maze)
