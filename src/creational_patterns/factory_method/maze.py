from interface import Interface

from src.creational_patterns.maze.maze import Direction
from src.creational_patterns.maze.maze import Door
from src.creational_patterns.maze.maze import Maze
from src.creational_patterns.maze.maze import Room
from src.creational_patterns.maze.maze import Wall


class MazeGame:
    def create_maze(self) -> Maze:
        a_maze = self.make_maze()

        r1 = self.make_room(1)

        a_maze.add_room(r1)

        r1.set_side(Direction.North, self.make_wall())
        r1.set_side(Direction.South, self.make_wall())
        r1.set_side(Direction.East, self.make_wall())
        r1.set_side(Direction.West, self.make_wall())

        return a_maze

    def make_maze(self) -> Maze:
        return Maze()

    def make_room(self, n: int) -> Room:
        return Room(n)

    def make_wall(self) -> Wall:
        return Wall()

    def make_door(self, r1: Room, r2: Room) -> Door:
        return Door(r1, r2)


class BombedWall(Wall):
    pass


class BombedMazeGame(MazeGame):
    def make_wall(self) -> BombedWall:
        return BombedWall()


if __name__ == '__main__':
    game = MazeGame()
    maze = game.create_maze()

    bombed_game = BombedMazeGame()
    bombed_maze = bombed_game.create_maze()

    print(bombed_maze.room_no(1).sides[0][0])
    print(maze.room_no(1).sides[0][0])
