#RANDOM FSM GENERATOR
import random

def randomnumber(x):
        num = random.randint(0, x)
        return num
        
# def generate_random(numOfStates,  numofInputs,  numofOutputs):
#         outputs = " "
#         nextStates= " "
#         for i in range(0,numofInputs):
#                 for j in range(0,numOfStates):
#                         print("a")
#                        # outputs[i][j] = random.randint(0,10) % numofOutputs
#                         #nextStates[i][j] = random.randint(0,10) % numOfStates


class FSM:
    class Node:
        def __init__(self, numOfInputs):
            self.transitions = {}
            ## initialize the node to have #inputs many transitions
            for i in range(numOfInputs):
                self.transitions[i] = (None, None) # Destination and output is empty for now


    def __init__(self, numOfStates, numOfInputs, numOfOutputs): #x is range of randomness.
        self.numOfStates = numOfStates
        self.numOfInputs = numOfInputs
        self.numOfOutputs = numOfOutputs

        self.nodes = []
        
        # print(self.numOfStates)
        # print(self.numOfInputs)
        # print(self.numOfOutputs)
        # liste.append(self.numOfStates)
        # liste.append(self.numOfInputs)
        # liste.append(self.numOfOutputs)
                

    def generateFsm(self):
        #Create all the states:
        for i in range(self.numOfStates):
            self.nodes.append(FSM.Node(self.numOfInputs))

        #Connect them randomly
        for node in self.nodes:
            for i in range(self.numOfInputs):
                node.transitions[i] = (random.choice(self.nodes), random.randint(0, self.numOfOutputs-1))

    def showFsm(self):
        for node in self.nodes:
            print(node.transitions)


fsm = FSM(5,2,3)
fsm.generateFsm()
fsm.showFsm()

# liste = []
# fsm1 = FSM()
# a=fsm1.init(randomnumber(10),randomnumber(10),randomnumber(10),liste)
# print(liste)

# generate_random(liste[0], liste[1], liste[2])

                
##                self.trans = None
##                self.states = {}
##                self.currentState = None

                
##        self.generateFsm(n,p,q)
##        self.isMinimal(FSM)
##        self.generateMinimal(FSM(n,p,q))
##                
##                
##
##                
##        def settingstate(self, statename):
##                self.currentState = self.states[statename]
##
##        def transition(self, transitionname):
##                self.trans = self.transitions[transitionname]
##
##
##        def execution(self):
##                if(self.trans):
##                        self.trans.execution()
##                        self.settingstate(self.trans.toState)
##                        self.trans = None
##                self.currentState.execution()
##


#generate_random(2 ,2, 2)

        
