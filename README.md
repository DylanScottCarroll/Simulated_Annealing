## annealing.py

`annealing.py` contains the logic for running the annealing. It takes as input an initial state, neighbor function, energy function, and decay schedule and will run the simulation.

It is written to be agnostic to the problem at hand.

It also provides functionality for running the annealing simulation as an iterable with patience so it can be placed in a for-loop.


## salesman.py

`salesman.py` is where the logic behind the traveling salesman problem domain is defined. It provides functionality for creating new problems with a given number of cities, storing solutions, calculating distance heuristics, finding neighbors, and drawing solutions.

## main.py

`main.py` sets up the traveling salesman problem, and runs it with the annealer.

The parameters of the simulation like the temperature schedule and patience are defined here.