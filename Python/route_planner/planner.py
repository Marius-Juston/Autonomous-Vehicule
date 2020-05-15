# without problems
import math


class PathPlanner():
    """Construct a PathPlanner Object"""

    def __init__(self, world_map, start=None, goal=None):
        """ """
        self.map = world_map
        self.start = start
        self.goal = goal
        self.closedSet = self.create_closedSet() if goal is not None and start is not None else None
        self.openSet = self.create_openSet() if goal is not None and start is not None else None
        self.cameFrom = self.create_cameFrom() if goal is not None and start is not None else None
        self.gScore = self.create_gScore() if goal is not None and start is not None else None
        self.fScore = self.create_fScore() if goal is not None and start is not None else None
        self.path = self.run_search() if self.map and self.start is not None and self.goal is not None else None

    def reconstruct_path(self, current):
        """ Reconstructs path after search """
        total_path = [current]
        while current in self.cameFrom.keys():
            current = self.cameFrom[current]
            total_path.append(current)
        return total_path

    def _reset(self):
        """Private method used to reset the closedSet, openSet, cameFrom, gScore, fScore, and path attributes"""
        self.closedSet = None
        self.openSet = None
        self.cameFrom = None
        self.gScore = None
        self.fScore = None
        self.path = self.run_search() if self.map and self.start and self.goal else None

    def run_search(self):
        """ """
        if self.map is None:
            raise (ValueError, "Must create map before running search. Try running PathPlanner.set_map(start_node)")
        if self.goal is None:
            raise (
                ValueError, "Must create goal node before running search. Try running PathPlanner.set_goal(start_node)")
        if self.start is None:
            raise (
                ValueError,
                "Must create start node before running search. Try running PathPlanner.set_start(start_node)")

        self.closedSet = self.closedSet if self.closedSet is not None else self.create_closedSet()
        self.openSet = self.openSet if self.openSet is not None else self.create_openSet()
        self.cameFrom = self.cameFrom if self.cameFrom is not None else self.create_cameFrom()
        self.gScore = self.gScore if self.gScore is not None else self.create_gScore()
        self.fScore = self.fScore if self.fScore is not None else self.create_fScore()

        while not self.is_open_empty():
            current = self.get_current_node()

            if current == self.goal:
                self.path = [x for x in reversed(self.reconstruct_path(current))]
                return self.path
            else:
                self.openSet.remove(current)
                self.closedSet.add(current)

            for neighbor in self.get_neighbors(current):
                if neighbor in self.closedSet:
                    continue  # Ignore the neighbor which is already evaluated.

                if not neighbor in self.openSet:  # Discover a new node
                    self.openSet.add(neighbor)

                # The distance from start to a neighbor
                # the "dist_between" function may vary as per the solution requirements.
                if self.get_tentative_gScore(current, neighbor) >= self.get_gScore(neighbor):
                    continue  # This is not a better path.

                # This path is the best until now. Record it!
                self.record_best_path_to(current, neighbor)
        print("No Path Found")
        self.path = None
        return False

    def create_closedSet(self):
        """ Creates and returns a data structure suitable to hold the set of nodes already evaluated"""
        # EXAMPLE: return a data structure suitable to hold the set of nodes already evaluated
        return set()

    def create_openSet(self):
        """ Creates and returns a data structure suitable to hold the set of currently discovered nodes
        that are not evaluated yet. Initially, only the start node is known."""
        if self.start is not None:
            # TODO: return a data structure suitable to hold the set of currently discovered nodes
            # that are not evaluated yet. Make sure to include the start node.
            #         return PriorityQueue((0, self.start))
            #         print(self.start)
            return {self.start}
        raise (
            ValueError,
            "Must create start node before creating an open set. Try running PathPlanner.set_start(start_node)")

    def create_cameFrom(self):
        """Creates and returns a data structure that shows which node can most efficiently be reached from another,
        for each node."""
        # TODO: return a data structure that shows which node can most efficiently be reached from another,
        # for each node.
        return dict()

    def create_gScore(self):
        """Creates and returns a data structure that holds the cost of getting from the start node to that node,
        for each node. The cost of going from start to start is zero."""

        return {self.start: 0}

    def create_fScore(self):
        """Creates and returns a data structure that holds the total cost of getting from the start node to the goal
        by passing by that node, for each node. That value is partly known, partly heuristic.
        For the first node, that value is completely heuristic."""

        return {self.start: self.distance(self.start, self.goal)}

    def set_map(self, M):
        """Method used to set map attribute """
        self._reset()
        self.start = None
        self.goal = None
        # TODO: Set map to new value.

    def set_start(self, start):
        """Method used to set start attribute """
        self._reset()
        self.start = start

    def set_goal(self, goal):
        """Method used to set goal attribute """
        self._reset()
        self.goal = goal

    def is_open_empty(self):
        """returns True if the open set is empty. False otherwise. """
        return not self.openSet

    def get_current_node(self):
        """ Returns the node in the open set with the lowest value of f(node)."""
        # TODO: Return the node in the open set with the lowest value of f(node).

        a = {node: self.fScore[node] for node in self.openSet}

        return min(a, key=a.get)

    def get_neighbors(self, node):
        """Returns the neighbors of a node"""
        return self.map.roads[node]

    def get_gScore(self, node):
        """Returns the g Score of a node"""
        if node not in self.gScore:
            return float('infinity')

        return self.gScore[node]
        # TODO: Return the g Score of a node

    # In[37]:

    def distance(self, node_1, node_2):
        """ Computes the Euclidean L2 Distance"""
        # TODO: Compute and return the Euclidean L2 Distance
        node_1 = self.map.intersections[node_1]
        node_2 = self.map.intersections[node_2]

        return math.hypot((node_1[0] - node_2[0]), (node_1[1] - node_2[1]))

    def get_tentative_gScore(self, current, neighbor):
        """Returns the tentative g Score of a node"""
        # TODO: Return the g Score of the current node
        # plus distance from the current node to it's neighbors
        return self.get_gScore(current) + self.distance(current, neighbor)

    def heuristic_cost_estimate(self, node):
        """ Returns the heuristic cost estimate of a node """
        # TODO: Return the heuristic cost estimate of a node
        return self.distance(node, self.goal)

    def calculate_fscore(self, node):
        """Calculate the f score of a node. """
        # TODO: Calculate and returns the f score of a node.
        # REMEMBER F = G + H
        return self.get_gScore(node) + self.heuristic_cost_estimate(node)

    def record_best_path_to(self, current, neighbor):
        """Record the best path to a node """
        # TODO: Record the best path to a node, by updating cameFrom, gScore, and fScore
        print(current, neighbor)
        self.cameFrom[neighbor] = current
        self.fScore[neighbor] = self.calculate_fscore(neighbor)
        self.gScore[neighbor] = self.get_gScore(neighbor)
