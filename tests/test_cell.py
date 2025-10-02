"""
Unit tests for Cell class.
"""
import unittest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.cell import Cell, AliveState, DeadState


class TestCell(unittest.TestCase):
    """Test cases for Cell class."""
    
    def test_cell_initial_state(self):
        """Test that a new cell is dead by default."""
        cell = Cell()
        self.assertFalse(cell.is_alive())
    
    def test_cell_set_alive(self):
        """Test setting a cell to alive."""
        cell = Cell()
        cell.set_alive()
        self.assertTrue(cell.is_alive())
    
    def test_cell_set_dead(self):
        """Test setting a cell to dead."""
        cell = Cell(AliveState())
        cell.set_dead()
        self.assertFalse(cell.is_alive())
    
    def test_alive_cell_with_two_neighbors_survives(self):
        """Test that alive cell with 2 neighbors stays alive."""
        cell = Cell(AliveState())
        cell.update(2)
        self.assertTrue(cell.is_alive())
    
    def test_alive_cell_with_three_neighbors_survives(self):
        """Test that alive cell with 3 neighbors stays alive."""
        cell = Cell(AliveState())
        cell.update(3)
        self.assertTrue(cell.is_alive())
    
    def test_alive_cell_with_fewer_than_two_neighbors_dies(self):
        """Test that alive cell with < 2 neighbors dies."""
        cell = Cell(AliveState())
        cell.update(1)
        self.assertFalse(cell.is_alive())
    
    def test_alive_cell_with_more_than_three_neighbors_dies(self):
        """Test that alive cell with > 3 neighbors dies."""
        cell = Cell(AliveState())
        cell.update(4)
        self.assertFalse(cell.is_alive())
    
    def test_dead_cell_with_three_neighbors_becomes_alive(self):
        """Test that dead cell with 3 neighbors becomes alive."""
        cell = Cell(DeadState())
        cell.update(3)
        self.assertTrue(cell.is_alive())
    
    def test_dead_cell_with_two_neighbors_stays_dead(self):
        """Test that dead cell with 2 neighbors stays dead."""
        cell = Cell(DeadState())
        cell.update(2)
        self.assertFalse(cell.is_alive())


if __name__ == '__main__':
    unittest.main()
