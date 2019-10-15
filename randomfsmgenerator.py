#RANDOM FSM GENERATOR
import random


class FSM:
    class Node:
        def __init__(self, numOfInputs, index):
            self.transitions = []
            self.index = index
            ## initialize the node to have #inputs many transitions
            for i in range(numOfInputs):
                self.transitions.append((None, None)) # Destination and output is empty for now


    def __init__(self, numOfStates, numOfInputs, numOfOutputs): #x is range of randomness.
        self.numOfStates = numOfStates
        self.numOfInputs = numOfInputs
        self.numOfOutputs = numOfOutputs

        self.nodes = []
                

    def generateFsm(self):
        #Create all the states:
        for i in range(self.numOfStates):
            self.nodes.append(FSM.Node(self.numOfInputs, i))

        #Connect them randomly
        for node in self.nodes:
            for i in range(self.numOfInputs):
                node.transitions[i] = (random.choice(self.nodes), random.randint(0, self.numOfOutputs-1))

    def showFsm(self):
        for node in self.nodes:
            print("Node:", node.index, ":")
            print("[", end="")
            for i in range(len(node.transitions)):
                print("(input:{}, to:{}, output:{})".format(i, node.transitions[i][0].index, node.transitions[i][1]), end="")
            print("]")

fsm = FSM(5,2,3)
fsm.generateFsm()
fsm.showFsm()

