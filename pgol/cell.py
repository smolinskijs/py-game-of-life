"""
Cell class representing a single cell in the Game of Life.
Uses State pattern for alive/dead states.
"""


class CellState:
    """Abstract base class for cell states."""
    
    def is_alive(self):
        raise NotImplementedError
    
    def get_next_state(self, alive_neighbors):
        raise NotImplementedError
    
    def __str__(self):
        raise NotImplementedError


class AliveState(CellState):
    """State representing a living cell."""
    
    def is_alive(self):
        return True
    
    def get_next_state(self, alive_neighbors):
        # Alive cell stays alive with 2 or 3 neighbors
        if alive_neighbors in (2, 3):
            return AliveState()
        return DeadState()
    
    def __str__(self):
        return "Alive"


class DeadState(CellState):
    """State representing a dead cell."""
    
    def is_alive(self):
        return False
    
    def get_next_state(self, alive_neighbors):
        # Dead cell becomes alive with exactly 3 neighbors
        if alive_neighbors == 3:
            return AliveState()
        return DeadState()
    
    def __str__(self):
        return "Dead"


class Cell:
    """Represents a single cell in the Game of Life grid."""
    
    def __init__(self, state=None):
        self.state = state if state else DeadState()
    
    def is_alive(self):
        return self.state.is_alive()
    
    def update(self, alive_neighbors):
        """Update cell state based on number of alive neighbors."""
        self.state = self.state.get_next_state(alive_neighbors)
    
    def set_alive(self):
        """Set cell to alive state."""
        self.state = AliveState()
    
    def set_dead(self):
        """Set cell to dead state."""
        self.state = DeadState()
    
    def __str__(self):
        return str(self.state)
