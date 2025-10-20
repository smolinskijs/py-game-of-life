"""
Unit tests for Grid class.
"""
# TODO: Implement tests for Grid class
# klasa Grid, konstruktor i metoda get_cell() (można użyć mocka )
import pytest
from pgol.grid import Grid
from unittest.mock import Mock

@pytest.fixture
def square_grid():
    return Grid(4,4)

def test_constructor_width(square_grid):
    assert square_grid.width == 4

def test_constructor_height(square_grid):
    assert square_grid.height == 4

def test_consturctor_cells(square_grid):
    assert [len(_) for _ in square_grid.cells] == [4,4,4,4]

def test_get_cell_outside_scope(square_grid):
    x = 1
    y = 4
    assert square_grid.get_cell(-x,-x) == None
    assert square_grid.get_cell(-x,y) == None
    assert square_grid.get_cell(y,-x) == None
    assert square_grid.get_cell(y,y) == None

def test_get_cell_inside_scope(square_grid):
    x = 0
    y = 3
    assert square_grid.get_cell(x,x) == square_grid.cells[x][x]
    assert square_grid.get_cell(y,x) == square_grid.cells[x][y]
    assert square_grid.get_cell(x,y) == square_grid.cells[y][x]
    assert square_grid.get_cell(y,y) == square_grid.cells[y][y]

def test_get_cell(square_grid):
    x = 0
    y = 3
    square_grid.get_cell = Mock()
    square_grid.get_cell(x,y)
    square_grid.get_cell.assert_called_once()