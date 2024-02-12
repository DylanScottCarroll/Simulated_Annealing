import random

class Annealer:
    def __init__(self, start_state, neighbor_function, energy_function, temp_decay, start_temp = 1):
        self.neighbor_function = neighbor_function
        self.energy_function = energy_function
        
        # The current state
        self.state = start_state
        self.energy = self.energy_function(self.state)

        #The best state found so far (not part of the algorithm)
        self.best_state = self.state
        self.best_energy = self.energy

        self.temp_decay = temp_decay
        self.temp = start_temp

    def _acceptence_probability(self, e, e_new):
        if e_new < e:
            return 1
        
        else:
            p = ((e - e_new) / (e + e_new)) + 1
            return p * self.temp

    def step(self):
        next_state = self.neighbor_function(self.state)
        next_energy = self.energy_function(next_state)


        if  random.random() < self._acceptence_probability(self.energy, next_energy):
            self.state = next_state
            self.energy = next_energy

            self.patience = self.default_patience


        if self.energy < self.best_energy:
            self.best_energy = self.energy
            self.best_state = self.state

        self.temp = self.temp_decay(self.temp)

    def __iter__(self):
        return self

    def loop(self, patience):
        self.patience = patience
        self.default_patience = patience

        return self

    def __next__(self):
        self.patience -= 1
        
        start_energy = self.energy
        self.step()

        if start_energy != self.energy:
            self.patience = self.default_patience

        if self.patience <= 0 or self.temp < 0:
            raise StopIteration
        else:
            return self
