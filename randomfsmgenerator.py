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
        
        #[[2,5][1,3][4]]
        self.groupsList = None

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

    def divideWithOutputs(self):
        if self.groupsList != None:
            return

        self.groupsList = [[self.nodes[0]]] #initialize with one node

        for i in range(1, len(self.nodes)): #for each node

            for j in range(len(self.groupsList)): #check each group
                match = True
                for k in range(len(self.nodes[i].transitions)): #compare each output
            
                    if (self.nodes[i].transitions[k][1] != self.groupsList[j][0].transitions[k][1]): #if some outputs dont match
                        match = False
                        break

                if match: #All outputs matched, add to group, exit this loop
                    self.groupsList[j].append(self.nodes[i])
                    break

            if not match: #No group matched, create new group

                self.groupsList.append([self.nodes[i]])


        for i in range(len(self.groupsList)):
            print("[", end="")
            for k in range(len(self.groupsList[i])):
                print(self.groupsList[i][k].index, end="")
            print("]")

fsm = FSM(5,2,3)
fsm.generateFsm()
fsm.showFsm()
fsm.divideWithOutputs()

