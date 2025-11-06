import pytest

from pgol.game import Game
from pgol.grid import Grid
from unittest.mock import MagicMock, patch


def test_game_init():
    grid_value = Grid(2,2)
    game = Game(grid_value)
    assert game.grid == grid_value
    assert game.is_running == False
    assert game.observers.__len__() == 0
    assert game.generation == 0

# THIS IS A UNIT TEST
def test_game_silent_update():
    grid = MagicMock()
    game = Game(grid)
    game.silent_update()
    grid.update.assert_called_once()

# SPYING ON A METHOD WHICH IS STILL EXECUTED
def test_game_silent_update_integration():
    grid = Grid(2,2)
    with patch.object(Grid, "update", wraps=grid.update) as mock_update:
        game = Game(grid)
        game.silent_update()
        mock_update.assert_called_once()

def test_game_silent_update_full_integration():
    grid = Grid(10,10)
    grid.cells[2][3].set_alive()
    grid.cells[2][4].set_alive()
    grid.cells[3][2].set_alive()
    grid.cells[3][3].set_alive()
    game = Game(grid)
    game.silent_update()
    assert game.generation == 1
    assert grid.get_alive_count()
    assert grid.cells[3][4].is_alive()
