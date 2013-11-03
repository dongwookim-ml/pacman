# valueIterationAgents.py
# -----------------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and Pieter 
# Abbeel in Spring 2013.
# For more info, see http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html

import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        # Write value iteration code here
        while self.iterations > 0:
            junk = self.values.copy()
            for state in self.mdp.getStates():
                garbage = {}
                for action in mdp.getPossibleActions(state):
                    garbage[action] = 0
                    for (nextState, prob) in self.mdp.getTransitionStatesAndProbs(state, action):
                        garbage[action] += prob * (mdp.getReward(state, action, nextState) + self.discount * junk[nextState])
                try:
                    self.values[state] = max(garbage.values())
                except ValueError:
                    self.values[state] = 0
            self.iterations -= 1
        #print self.values.__str__()
    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        k = 0
        for (nextState, prob) in self.mdp.getTransitionStatesAndProbs(state, action):
            q=k
            k += prob * (self.mdp.getReward(state, action, nextState) + self.discount * self.getValue(nextState))
            r = k - q
            #print " I CAN GO TO " + nextState.__str__() + " WITH PROBABILITY " + prob.__str__() + " WHOSE REWARD IS " + self.mdp.getReward(state, action, nextState).__str__() + " AND WHOSE Vk IS " + self.getValue(nextState).__str__() + "WHICH IS WHY I ADDED " + r.__str__()
        #print "RETURNEN " + k.__str__()
        return k

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        garbage = {}
        for action in self.mdp.getPossibleActions(state):
         #   print "I AM GOING TO REQUEST THE Q VALUE OF " + action.__str__() + " FROM " + state.__str__()
            garbage[action] = self.computeQValueFromValues(state, action)
        try:
            k =  max(garbage.values())
            for trash in garbage.keys():
                if garbage[trash] == k:
                    return trash
        except ValueError:
            return None
    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
