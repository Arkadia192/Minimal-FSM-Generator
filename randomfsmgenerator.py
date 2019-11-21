#RANDOM FSM GENERATOR

global GraphvizImportSuccessful

import random

from collections import deque

try:
    from graphviz import Digraph
    from graphviz import render
except Exception as e:
    GraphvizImportSuccessful = False
else:
    GraphvizImportSuccessful = True

class FSM:
    class Node:
        def __init__(self, numOfInputs, index):
            self.transitions = []
            self.index = index
            self.newGroup=[]
            
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

    def generate(self):
        #Create all the states:
        for i in range(self.numOfStates):
            self.nodes.append(FSM.Node(self.numOfInputs, i))

        #Connect them randomly
        for node in self.nodes:
            for i in range(self.numOfInputs):
                node.transitions[i] = (random.choice(self.nodes), random.randint(0, self.numOfOutputs-1))

    def clear(self):
        while len(self.nodes) > 0:
            del self.nodes[0]

    def isSurelyMinimal(self):
        return self.isMinimal() and self.isMinimalGraph()

    def generateMinimal(self):

        self.generate()

        while not self.isSurelyMinimal(): #if minimality check gives false
            self.clear()
            self.generate()

    def generateRandomTrace(self, length=10, startNode=-1):
        # Generates an input trace
        # Returns a list of tuples with the format [(input, output)]

        if 0 <= startNode and startNode < len(self.nodes): 
            currentNode = self.nodes[startNode]
        else:
            currentNode = random.choice(self.nodes)

        traceList = []

        for i in range(length):
            randomInput = random.randint(0, self.numOfInputs-1)
            traceList.append((randomInput, currentNode.transitions[randomInput][1]))
            currentNode = currentNode.transitions[randomInput][0]

        return traceList

    def show(self):
        for node in self.nodes:
            print("Node:", node.index, ":")
            print("[", end="")
            for i in range(len(node.transitions)):
                print("(input:{}, to:{}, output:{})".format(i, node.transitions[i][0].index, node.transitions[i][1]), end="")
            print("]")

    def draw(self, makePng = False):

        if not GraphvizImportSuccessful:
            print("You need to successfully install graphviz to use draw method")
            return 

        f = Digraph("Finite_State_Machine", filename="fsm.gv")

        f.attr("node", shape="circle")

        for node in self.nodes:
            for i in range(self.numOfInputs):
                f.edge(str(node.index), str(node.transitions[i][0].index), label="i:{}/o:{}".format(i, node.transitions[i][1]))

        try:
            f.view() #Tries to view the graph
        except Exception as e:
            print(e)
            print("Unable to draw the graph")
            return


        if makePng:
            render("dot", "png", "fsm.gv") # Makes a png file
        
    def isMinimalGraph(self):

        self.createGraphNodes()
        self.connectGraphNodes()

        return self.searchInGraphNodes()

    def createGraphNodes(self):
        """ Create the graph """

        self.graphNodes = {} #keys are the actual node tuples and values are the indexes of them


        # The ultimate node
        self.graphNodes["SeparableNode"] = FSM.GraphNode("(Separable, Node)")

        # loop over all pairs and create graph nodes
        for i in range(len(self.nodes)):
            for j in range(i+1, len(self.nodes)):
                self.graphNodes[(self.nodes[i], self.nodes[j])] = FSM.GraphNode((self.nodes[i].index, self.nodes[j].index))

        #for node in self.graphNodes:
        #    print(self.graphNodes[node].nodeTuple)


    def connectGraphNodes(self):
        """ Connect the Graph """

        for graphNodeKey in self.graphNodes:

            if graphNodeKey == "SeparableNode":
                continue

            node1 = graphNodeKey[0]
            node2 = graphNodeKey[1]

            for i in range(self.numOfInputs): #Check each transition

                # Check the outputs
                if (node1.transitions[i][1] != node2.transitions[i][1]): # if different outputs
                    self.graphNodes[graphNodeKey].addConnection("SeparableNode") # Can be distinguished
                    self.graphNodes["SeparableNode"].addConnection(graphNodeKey)

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


    def searchInGraphNodes(self):
        """ Search The Graph """

        startnode = "SeparableNode"

        visited = []

        queue = deque()
        #queue = [] # Append to the end, delete from the front

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

            queue.popleft()

        if len(self.graphNodes) == len(visited):
            return True

        return False



    def divideWithOutputs(self):

        self.groupsList = []

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

        """
        for i in range(len(self.groupsList)):
            print("[", end="")
            for k in range(len(self.groupsList[i])):
                print(self.groupsList[i][k].index, end="")
            print("]")
        """

    def isMinimal(self):

        self.divideWithOutputs()
        
        temp = []
        temp2 = []
        
        Divide = True
        while(Divide):
            for i in range(len(self.groupsList)): #for every group
                for j in range(len (self.groupsList[i])): #for every elements in the group 
                    self.groupsList[i][j].newGroup = i 
                    #print(self.groupsList[i][j].index, self.groupsList[i][j].newGroup)

                    
            for i in range(len(self.groupsList)):
                samegroup = True
                newi=i
                temp2.append(self.groupsList[i][0]) #add first element of the ith list.
                temp.append(temp2)
                temp2 = []
                group2bePlaced = -1
                
                for j in range(1, len(self.groupsList[i])):
                    for x in range(newi, len(temp)):
                        #print("***")
                        samegroup = True
                        for c in range(len(self.groupsList[i][j].transitions)):
                            if self.groupsList[i][j].transitions[c][0].newGroup != temp[x][0].transitions[c][0].newGroup:
                                #print("divide")
                                samegroup = False

                        if samegroup:
                            group2bePlaced = x
                            break
                        
                    if group2bePlaced == -1: #append to new list
                        temp.append([self.groupsList[i][j]])   
                    else:
                        temp[x].append(self.groupsList[i][j]) # append to the corresponding list x.
                        #print("same group, do not divide")
              

            if(len(self.groupsList) == len(temp)):
                Divide =False  #if two lists are the same, no further division, break loop.

            self.groupsList = temp
            temp = []
        
        """
        for x in range(len(self.groupsList)):#print self.groupsList's elements
            print("[", end="")
            for k in range(len(self.groupsList[x])):
                print(self.groupsList[x][k].index, end="")
            print("]")
        """

        if len(self.groupsList) == self.numOfStates:
            return True

        return False

if __name__ == "__main__":
    fsm = FSM(5,2,3)
    fsm.generate()
    fsm.show()

    fsm.clear()
    print("\n\n")

    fsm.generateMinimal() #We can use this now
    fsm.show()
