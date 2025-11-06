import pytest
from unittest.mock import Mock, patch, MagicMock

from pgol.grid import Grid

w = h = 4
x = y = 1

@pytest.fixture
def square_grid():
    return Grid(w,h)

# Mockowanie metody, obiekt zostaje oryginalny.
def test_set_cell_alive(square_grid):
    square_grid.cells[x][y].set_alive = Mock()
    square_grid.set_cell_alive(x,y)
    square_grid.cells[x][y].set_alive.assert_called_once()

# To jest równowazne i preferowane rozwiazanie.
def test_set_cell_alive_patch_rv():
    with patch('pgol.grid.Cell') as MockedCell: # <- Patchuj klase
        MockedCell.return_value = MagicMock() # <- Przypisz MagicMock do obiektow
        grid = Grid(w, h)
        grid.set_cell_alive(x,y)
        grid.cells[x][y].set_alive.assert_called_once()

# Side effect jest jednym z rozwiazan
def test_set_cell_alive_patch_se():
    with patch('pgol.grid.Cell') as MockedCell: # TO JEST KLASA A NIE OBIEKT
        def mock_cell():
            cell = MagicMock()
            cell.set_alive = MagicMock()
            return cell
        MockedCell.side_effect = mock_cell
        grid = Grid(w, h)
        grid.set_cell_alive(x,y)
        grid.cells[x][y].set_alive.assert_called_once()


