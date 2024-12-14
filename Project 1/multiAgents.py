# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        # print("newFood : {}".format(newFood))
        # print("newPos : {}".format(newPos))
        # print("currPos : {}".format(currentGameState.getPacmanPosition()))
        # print("newFoodPos : {}".format(newFood.asList()))
        # print("g = {}".format(newGhostStates))

        "*** YOUR CODE HERE ***"
        score = 0
        food = currentGameState.getFood().count()
        ate = (food - newFood.count())
        sTime = 0
        for s in newScaredTimes:
            sTime += s

        score += sTime * 10

        for g in newGhostStates:
            if g.scaredTimer == 0:
                pt = manhattanDistance(g.getPosition(), newPos)
                if 1 < pt < 4:
                    score += -50 + pt
                elif pt <= 1:
                    score = -100 + pt

        if ate == 0:
            dis = 1000000
            for foodPos in newFood.asList():
                newDis = manhattanDistance(foodPos, newPos)
                if newDis < dis:
                    dis = newDis
        else:
            dis = 0

        score -= dis
        return score


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        numAgents = gameState.getNumAgents()

        def minimax(currState, agentIndex, targetDepth, currDepth):
            if agentIndex == 0:
                currDepth += 1
            if targetDepth == currDepth or currState.isWin() or currState.isLose():
                return self.evaluationFunction(currState), None
            actions = currState.getLegalActions(agentIndex)
            chosenAct = Directions.STOP
            if agentIndex == 0:
                maxEval = -10000
                for action in actions:
                    successor = currState.generateSuccessor(agentIndex, action)
                    tmp = minimax(successor, (agentIndex + 1) % numAgents, targetDepth, currDepth)[0]
                    if maxEval < tmp:
                        maxEval = tmp
                        chosenAct = action
                return maxEval, chosenAct
            else:
                minEval = 10000
                for action in actions:
                    successor = currState.generateSuccessor(agentIndex, action)
                    tmp = minimax(successor, (agentIndex + 1) % numAgents, targetDepth, currDepth)[0]
                    if minEval > tmp:
                        minEval = tmp
                        chosenAct = action
                return minEval, chosenAct

        val, act = minimax(gameState, 0, self.depth + 1, 0)
        # print(act)
        return act


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        numAgents = gameState.getNumAgents()

        def minimax(currState, agentIndex, targetDepth, currDepth, alpha, beta):
            if agentIndex == 0:
                currDepth += 1
            if targetDepth == currDepth or currState.isWin() or currState.isLose():
                return self.evaluationFunction(currState), None
            actions = currState.getLegalActions(agentIndex)
            chosenAct = Directions.STOP
            if agentIndex == 0:
                maxEval = -10000
                for action in actions:
                    successor = currState.generateSuccessor(agentIndex, action)
                    tmp = minimax(successor, (agentIndex + 1) % numAgents, targetDepth, currDepth, alpha, beta)[0]
                    if maxEval < tmp:
                        maxEval = tmp
                        chosenAct = action
                    if alpha < tmp:
                        alpha = tmp
                    if alpha > beta:
                        break
                return maxEval, chosenAct
            else:
                minEval = 10000
                for action in actions:
                    successor = currState.generateSuccessor(agentIndex, action)
                    tmp = minimax(successor, (agentIndex + 1) % numAgents, targetDepth, currDepth, alpha, beta)[0]
                    if minEval > tmp:
                        minEval = tmp
                        chosenAct = action
                    if beta > tmp:
                        beta = tmp
                    if beta < alpha:
                        break
                return minEval, chosenAct

        val, act = minimax(gameState, 0, self.depth + 1, 0, -10000, 10000)
        # print(act)
        return act


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        numAgents = gameState.getNumAgents()

        def expectimax(currState, agentIndex, targetDepth, currDepth):
            if agentIndex == 0:
                currDepth += 1
            if targetDepth == currDepth or currState.isWin() or currState.isLose():
                return self.evaluationFunction(currState), None
            actions = currState.getLegalActions(agentIndex)
            chosenAct = Directions.STOP
            if agentIndex == 0:
                maxEval = -10000
                for action in actions:
                    successor = currState.generateSuccessor(agentIndex, action)
                    tmp = expectimax(successor, (agentIndex + 1) % numAgents, targetDepth, currDepth)[0]
                    if maxEval < tmp:
                        maxEval = tmp
                        chosenAct = action
                return maxEval, chosenAct
            else:
                avg = 0
                for action in actions:
                    successor = currState.generateSuccessor(agentIndex, action)
                    avg += expectimax(successor, (agentIndex + 1) % numAgents, targetDepth, currDepth)[0]
                return avg / len(actions), chosenAct

        val, act = expectimax(gameState, 0, self.depth + 1, 0)
        # print(act)
        return act


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    if currentGameState.isWin():
        return 10000
    elif currentGameState.isLose():
        return -10000
    pacmanPos = currentGameState.getPacmanPosition()
    food = currentGameState.getFood()
    ghostStates = currentGameState.getGhostStates()
    scaredTimes = [ghostState.scaredTimer for ghostState in ghostStates]
    score = 0
    sTime = 0
    for s in scaredTimes:
        sTime += s

    score += sTime*2

    dis = 1000000
    for foodPos in food.asList():
        newDis = manhattanDistance(foodPos, pacmanPos)
        if newDis < dis:
            dis = newDis
    for g in ghostStates:
        if g.scaredTimer == 0:
            pt = manhattanDistance(g.getPosition(), pacmanPos)
            if 1 < pt < 5:
                score += -70 + pt
            elif pt <= 1:
                score = -130 + pt
    score -= dis
    score -= 17 * food.count()
    return score


# Abbreviation
better = betterEvaluationFunction
