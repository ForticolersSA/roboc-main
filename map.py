# -*-coding:Utf-8 -*
# from maze import Maze
"""This module contains the class MazeMap


"""
class MazeMap:

        """This object will serve as a transition between the maze and a file

        """
        def __init__(self, name, str):
            self.name = name
            # self.maze = generate_maze_map(str)
        def __repr__(self):
            return f"<Map name : {self.name}>"
#test module
if __name__ == "__main__":
    maze = MazeMap("test", "stest")
    print(maze)
    maze
