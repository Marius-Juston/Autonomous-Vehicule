from route_planner.helpers import load_map_10, load_map_40, show_map
from route_planner.planner import PathPlanner

if __name__ == '__main__':

    map_10 = load_map_10()
    # show_map(map_10)

    # map_40 is a bigger map than map_10
    map_40 = load_map_40()
    # show_map(map_40)

    # show_map(map_40, start=5, goal=34, path=[5, 16, 37, 12, 34])

    planner = PathPlanner(map_40, 5, 34)
    path = planner.path
    if path == [5, 16, 37, 12, 34]:
        print("great! Your code works for these inputs!")
    else:
        print("something is off, your code produced the following:")
        print(path)

    start = 5
    goal = 34

    show_map(map_40, start=start, goal=goal, path=PathPlanner(map_40, start, goal).path)

    from route_planner.test import test

    test(PathPlanner)
