"""
Unit tests for Grid class.
"""
import pytest

from pgol.grid import Grid


@pytest.fixture
def square_grid():
    return Grid(4,4)

#Kacper
@pytest.mark.parametrize("x,y", [
    (0,0),
    (1,1),
    (2,2),
    (3,3),]
)
def test_set_cell_alive(square_grid, x, y):
    square_grid.cells[y][x].set_dead()
    square_grid.set_cell_alive(x,y)
    assert square_grid.cells[y][x].is_alive() == True

@pytest.mark.parametrize("x,y",[
    (1,1),
    (2,2)
])
def test_set_cell_dead(square_grid, x, y):
    square_grid.cells[y][x].set_alive()
    square_grid.set_cell_dead(x,y)
    assert square_grid.cells[y][x].is_alive() == False

def test_grid_constructor(square_grid):
    for y in range(square_grid.width):
        for x in range(square_grid.height):
            assert square_grid.cells[y][x].is_alive() == False

@pytest.mark.parametrize("x,y,activated_cells,result", [
    (2,2,[(2,3),(3,2)], 2),
    (2,2,[(2,3),(3,2),(2,1)], 3),
    (1,1,[(0,1),(1,0),(2,1),(1,2),(0,2)], 5)
])
def test_count_alive_neighbors(square_grid, x, y, activated_cells, result):
    square_grid.clear()
    for cell in activated_cells:
        square_grid.set_cell_alive(cell[0], cell[1])
    assert square_grid.count_alive_neighbors(x,y) == result


    # # # #
    # # # #
    # # A A
    # # # #

    # def count_alive_neighbors(self, x, y):
    #     """Count alive neighbors for cell at position (x, y)."""
    #     count = 0
    #     for dy in range(-1, 2):
    #         for dx in range(-1, 2):
    #             if dx == 0 and dy == 0:
    #                 continue
                
    #             nx, ny = x + dx, y + dy
    #             if 0 <= nx < self.width and 0 <= ny < self.height:
    #                 if self.cells[ny][nx].is_alive():
    #                     count += 1
    #     return count