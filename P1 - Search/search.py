# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())

    stack = util.Stack()
    stack.push((problem.getStartState(), []))  # Push current cell into stack
    visited = set()  # Create a set of visited cells

    while not stack.isEmpty():
        curState, direction = stack.pop()  # Removes top of the stack
        visited.add(curState)  # Marks it as visited

        # If successor cell is the goal, return list of actions
        if problem.isGoalState(curState):
            return direction

     # For each successor cell:
        for successor, action, stepCost in problem.getSuccessors(curState):       
            # If successor is not visited, push it to the stack
            if successor not in visited:
                stack.push((successor, direction + [action]))


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    queue = util.Queue()
    queue.push((problem.getStartState(), []))  # Push current cell into queue
    visited = []  # Create a set of visited cells
    visited.append(problem.getStartState())  # Marks starting cell as visited
    while not queue.isEmpty():
        curState, direction = queue.pop()  # Removes head of the queue

        # If current cell is the goal, return list of actions
        if problem.isGoalState(curState):
            return direction

        # For each successor cell:
        for successor, action, stepCost in problem.getSuccessors(curState):
            # If successor is not visited, push it to the queue
            if successor not in visited:
                queue.push((successor, direction + [action]))
                # if not problem.isGoalState(successor):
                visited.append(successor)  # Marks next successor as visited


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    priorityQueue = util.PriorityQueue()
    priorityQueue.push((problem.getStartState(), []), 0)
    visited = set()
    visited.add(problem.getStartState())  # Marks starting cell as visited
    while not priorityQueue.isEmpty():
        curState, direction = priorityQueue.pop()  # Removes head of the priority queue

        # If current cell is the goal, return list of actions
        if problem.isGoalState(curState):
            return direction

        # For each successor cell:
        for successor, action, stepCost in problem.getSuccessors(curState):
            # If successor is not visited, push it to the priority queue
            if successor not in visited:
                priorityQueue.push(
                    (successor, direction + [action]), problem.getCostOfActions(direction + [action]))
                if not problem.isGoalState(successor):
                    visited.add(successor)  # Marks next successor as visited


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    priorityQueue = util.PriorityQueue()
    priorityQueue.push((problem.getStartState(), []),
                       heuristic(problem.getStartState(), problem))
    visited = []
    visited.append(problem.getStartState())  # Marks starting cell as visited
    while not priorityQueue.isEmpty():
        curState, direction = priorityQueue.pop()  # Removes head of the priority queue

        # If successor cell is the goal, return list of actions
        if problem.isGoalState(curState):
            return direction

        # For each successor cell:
        for successor, action, stepCost in problem.getSuccessors(curState):
            # If successor is not visited, push it to the priority queue with a heuristic function
            if successor not in visited:
                priorityQueue.push(
                    (successor, direction + [action]), problem.getCostOfActions(direction + [action]) + heuristic(successor, problem))
                if not problem.isGoalState(successor):
                    visited.append(successor)  # Marks next successor as visited


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
