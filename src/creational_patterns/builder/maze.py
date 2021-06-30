from typing import Optional

from interface import Interface
from interface import implements

from src.creational_patterns.maze.maze import Direction
from src.creational_patterns.maze.maze import Door
from src.creational_patterns.maze.maze import Maze
from src.creational_patterns.maze.maze import Room
from src.creational_patterns.maze.maze import Wall


class MazeBuilder(Interface):
    def build_maze(self):
        pass

    def build_room(self, room: int) -> Room:
        pass

    def build_door(self, room_from: int, room_to: int) -> Door:
        pass

    def get_maze(self) -> Maze:
        pass

class StandardMazeBuilder(implements(MazeBuilder)):
    def __init__(self):
        self._current_maze : Optional[Maze] = None

    def build_maze(self):
        self._current_maze = Maze()

    def build_room(self, room: int) -> Room:
        if self._current_maze.room_no(room) is None:
            room = Room(room)
            self._current_maze.add_room(room)

            room.set_side(Direction.North, Wall())
            room.set_side(Direction.South, Wall())
            room.set_side(Direction.East, Wall())
            room.set_side(Direction.West, Wall())

    def build_door(self, room_one:int, room_two:int):
        r1 = self._current_maze.room_no(room_one)
        r2 = self._current_maze.room_no(room_two)
        door = Door(r1, r2)

        r1.set_side(self.common_wall(r1, r2), door)
        r2.set_side(self.common_wall(r2, r1), door)

    def common_wall(self, room_one: Room, room_two:Room) -> Direction:
        # This function should return the common wall between two rooms.
        pass

    def get_maze(self) -> Maze:
        return self._current_maze


def create_maze(builder: MazeBuilder) -> Maze:
    builder.build_maze()
    builder.build_room(1)
    builder.build_room(2)
    builder.build_door(1, 2)

    return builder.get_maze()
