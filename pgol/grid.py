"""
Grid/Board class that manages the collection of cells.
Implements the core Game of Life logic.
"""
from pgol.cell import Cell, AliveState, DeadState


class Grid:
    """Represents the game board with a grid of cells."""
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.cells = [[Cell() for _ in range(width)] for _ in range(height)]
    
    def get_cell(self, x, y):
        """Get cell at position (x, y)."""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.cells[y][x]
        return None
    
    def set_cell_alive(self, x, y):
        """Set cell at position (x, y) to alive."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.cells[y][x].set_alive()
    
    def set_cell_dead(self, x, y):
        """Set cell at position (x, y) to dead."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.cells[y][x].set_dead()
    
    def toggle_cell(self, x, y):
        """Toggle cell state at position (x, y)."""
        cell = self.get_cell(x, y)
        if cell:
            if cell.is_alive():
                cell.set_dead()
            else:
                cell.set_alive()
    
    def count_alive_neighbors(self, x, y):
        """Count alive neighbors for cell at position (x, y)."""
        count = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if self.cells[ny][nx].is_alive():
                        count += 1
        return count
    
    def update(self):
        """Update all cells to next generation."""
        # Calculate next state for all cells
        next_states = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                alive_neighbors = self.count_alive_neighbors(x, y)
                current_state = self.cells[y][x].state
                next_state = current_state.get_next_state(alive_neighbors)
                row.append(next_state)
            next_states.append(row)
        
        # Apply next states
        for y in range(self.height):
            for x in range(self.width):
                self.cells[y][x].state = next_states[y][x]
    
    def clear(self):
        """Clear the grid (set all cells to dead)."""
        for y in range(self.height):
            for x in range(self.width):
                self.cells[y][x].set_dead()
    
    def get_alive_count(self):
        """Get total count of alive cells."""
        count = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.cells[y][x].is_alive():
                    count += 1
        return count
