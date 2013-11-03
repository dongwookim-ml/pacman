# Analysis`````.py
# -----------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and Pieter 
# Abbeel in Spring 2013.
# For more info, see http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html

######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.
import random
def question2():
    answerDiscount = 0.9
    answerNoise = 0.0
    return answerDiscount, answerNoise

def question3a():
    answerDiscount = 1
    answerNoise = 0.0
    answerLivingReward = -5
    print "IN THREE A I USED " + answerDiscount.__str__() + " AND " + answerNoise.__str__() + " AND " + answerLivingReward.__str__()
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3b():
    answerDiscount = .6
    answerNoise = 0.4
    answerLivingReward = -1
    print "IN THREE b I USED " + answerDiscount.__str__() + " AND " + answerNoise.__str__() + " AND " + answerLivingReward.__str__()

    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3c():
    answerDiscount = 1.0
    answerNoise = 0.0
    answerLivingReward = -.1
    print "IN THREE c I USED " + answerDiscount.__str__() + " AND " + answerNoise.__str__() + " AND " + answerLivingReward.__str__()

    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3d():
    answerDiscount = 1.0
    answerNoise = .49
    answerLivingReward = -.5
    print "IN THREE d I USED " + answerDiscount.__str__() + " AND " + answerNoise.__str__() + " AND " + answerLivingReward.__str__()

    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3e():
    answerDiscount = 0.0
    answerNoise = 0.0
    answerLivingReward = 0.0
    print "IN THREE e I USED " + answerDiscount.__str__() + " AND " + answerNoise.__str__() + " AND " + answerLivingReward.__str__()

    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question6():
    answerEpsilon = 0.2
    answerLearningRate = 0.2
    return 'NOT POSSIBLE'
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    randy = 0.0
    print 'Answers to analysis questions:'
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print '  Question %s:\t%s' % (q, str(response))
