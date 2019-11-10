# Minimal-FSM-Generator

*This is a work in progress*


## Important notes

The FSM.drawFsm() function requires the package graphviz.

Check out [graphviz website](https://graphviz.gitlab.io/download/) and [pypi.org](https://pypi.org/project/graphviz/) for detailed information

You can use `pip install graphviz` but you also need to make sure that the executables of graphviz is in your **System Path**

## Functions for general usage

- **FSM(** *number of states*, *number of inputs*, *number of outputs* **)**
  - Initializes the finite state machine object with the given attributes

- FSM.**generateFsm()**
  - Generates a random finite state machine.
  - Does not guarantee minimality
  
- FSM.**generateMinimalFsm()**
  - Generates a random *minimal* finite state machine.
  
- FSM.**clearFsm()**
  - Clears the FSM object
  - Cleared object can be used to create another random FSM

- FSM.**isMinimal()**
  - Applies a minimality check to the FSM object 
  - Returns True if the FSM is minimal, False otherwise
  
- FSM.**isMinimalGraph()**
  - Applies a graph based minimality check to the FSM object
  - Returns True if the FSM is minimal, False otherwise
  
- FSM.**isSurelyMinimal()**
  - Applies both minimality checks together.
  - Returns True if the FSM is minimal, False otherwise
  
- FSM.**showFsm()**
  - Prints the nodes of FSM in a formatted way
  
- FSM.**drawFsm(** *makePng=False* **)**
  - Uses the graphviz package to draw the graph.
  - Default output (only output for now) is pdf
  - If makePng is True, will also try to create a png file
  
## Example use

```
from randomfsmgenerator import FSM

myFsm = FSM(10, 5, 2)

myFsm.generateFsm()
myFsm.showFsm()

myFsm.ClearFsm()

myFsm.generateMinimalFsm()
if not myFsm.isSurelyMinimal():
  print("We have a big problem")


```
