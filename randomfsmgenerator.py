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

    class GraphNode:
        def __init__(self, nodeTuple):
            self.nodeTuple = nodeTuple

            # connections are two-ways
            self.connections = []

        def addConnection(self, smthing):
            #checks if it is already there
            #here to protect from duplicates

            if smthing not in self.connections:
                self.connections.append(smthing)



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

    def clearFsm(self):
        while len(self.nodes) > 0:
            del self.nodes[0]

    def generateMinimalFsm(self):

        self.generateFsm()

        while not self.minimalityWithGraph(): #if minimality check gives false
            self.clearFsm()
            self.generateFsm()

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

    def minimalityWithGraph(self):


        """ Create the graph """

        self.graphNodes = {} #keys are the actual node tuples and values are the indexes of them


        # The ultimate node
        self.graphNodes["GodNode"] = FSM.GraphNode("(God, Node)")

        # loop over all pairs and create graph nodes
        for i in range(len(self.nodes)):
            for j in range(i+1, len(self.nodes)):
                self.graphNodes[(self.nodes[i], self.nodes[j])] = FSM.GraphNode((self.nodes[i].index, self.nodes[j].index))

        #for node in self.graphNodes:
        #    print(self.graphNodes[node].nodeTuple)


        """ Connect the Graph """

        for graphNodeKey in self.graphNodes:

            if graphNodeKey == "GodNode":
                continue

            node1 = graphNodeKey[0]
            node2 = graphNodeKey[1]

            for i in range(self.numOfInputs): #Check each transition

                # Check the outputs
                if (node1.transitions[i][1] != node2.transitions[i][1]): # if different outputs
                    self.graphNodes[graphNodeKey].addConnection("GodNode") # Can be distinguished
                    self.graphNodes["GodNode"].addConnection(graphNodeKey)

                else: # Outputs are different

                    #Check if they go to the same state
                    if (node1.transitions[i][0] == node2.transitions[i][0]):
                        # No transitions added in this case
                        continue

                    else: # They go to different places

                        #This is needed because the smaller indexed node is always the first in the graphNodes dictionary
                        if (node1.transitions[i][0].index < node2.transitions[i][0].index):
                            placeTheyGoTo = (node1.transitions[i][0], node2.transitions[i][0])
                        else:
                            placeTheyGoTo = (node2.transitions[i][0], node1.transitions[i][0])

                        self.graphNodes[graphNodeKey].addConnection(placeTheyGoTo)
                        self.graphNodes[placeTheyGoTo].addConnection(graphNodeKey)

        #for node in self.graphNodes:
        #    print(self.graphNodes[node], self.graphNodes[node].connections)


        """ Search The Graph """

        startnode = "GodNode"

        visited = []

        queue = [] # Append to the end, delete from the front

        finished = False
        
        queue.append(self.graphNodes[startnode])

        while not finished:

            if len(queue) == 0:
                finished = True
                continue

            currNode = queue[0]

            for connection in currNode.connections:
                
                connection = self.graphNodes[connection]

                if ((connection not in visited) and (connection not in queue)):

                    queue.append(connection)
            
            visited.append(currNode)

            del queue[0]

        if len(self.graphNodes) == len(visited):
            return True

        return False


fsm = FSM(5,2,3)
fsm.generateFsm()
fsm.showFsm()
#fsm.divideWithOutputs()

fsm.clearFsm()
print("\n\n")

fsm.generateMinimalFsm() #We can use this now
fsm.showFsm()
