from src.creational_patterns.maze.maze import Maze, Room, Direction, Wall, Door


class MazeFactory:
    def make_maze(self) -> Maze:
        return Maze()

    def make_wall(self) -> Wall:
        return Wall()

    def make_room(self, n: int) -> Room:
        return Room(n)

    def make_door(self, r1: Room, r2: Room) -> Door:
        return Door(r1, r2)

def create_maze(factory: MazeFactory) -> Maze:
    a_maze = factory.make_maze()
    r1 = factory.make_room(1)
    r2 = factory.make_room(2)
    door = factory.make_door(r1,r2)

    a_maze.add_room(r1)
    a_maze.add_room(r2)

    r1.set_side(Direction.North, factory.make_wall())
    r1.set_side(Direction.East, door)
    r1.set_side(Direction.West, factory.make_wall())
    r1.set_side(Direction.South, factory.make_wall())


    r2.set_side(Direction.North, factory.make_wall())
    r2.set_side(Direction.East, factory.make_wall())
    r2.set_side(Direction.West, door)
    r2.set_side(Direction.South, factory.make_wall())

    return a_maze

if __name__=='__main__':
    factory = MazeFactory()
    maze = create_maze(factory)
    print(maze)
