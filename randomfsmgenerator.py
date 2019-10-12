#RANDOM FSM GENERATOR
import random

def randomnumber(x):
        num = random.randint(0, x)
        return num
        
def generate_random(numOfStates,  numofInputs,  numofOutputs):
        outputs = " "
        nextStates= " "
        for i in range(0,numofInputs):
                for j in range(0,numOfStates):
                        print("a")
                       # outputs[i][j] = random.randint(0,10) % numofOutputs
                        #nextStates[i][j] = random.randint(0,10) % numOfStates

    
                
                

class FSM(object):
        def init(self,numOfStates,numOfInputs,numOfOutputs,liste ): #x is range of randomness.
                self.numOfStates = numOfStates
                self.numOfInputs = numOfInputs
                self.numOfOutputs = numOfOutputs
                
                print(self.numOfStates)
                print(self.numOfInputs)
                print(self.numOfOutputs)
                liste.append(self.numOfStates)
                liste.append(self.numOfInputs)
                liste.append(self.numOfOutputs)
                
                
                                
   #def generateFsm(n,p,q):
                
        class Node(object):
                transition = {}



                
liste = []
fsm1 = FSM()
a=fsm1.init(randomnumber(10),randomnumber(10),randomnumber(10),liste)
print(liste)

generate_random(liste[0], liste[1], liste[2])







                
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

        
