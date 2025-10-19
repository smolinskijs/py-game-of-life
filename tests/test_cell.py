"""
Unit tests for Cell class.
"""
import pytest

from pgol.cell import AliveState, DeadState ,Cell

def test_alive_state():
    alive_state = AliveState()
    assert alive_state.is_alive() == True

def test_set_dead():
    cell = Cell(state=AliveState())
    cell.set_dead()
    assert cell.is_alive() == False

def test_set_alive():
    cell = Cell(state=DeadState())
    cell.set_alive()
    assert cell.is_alive() == True

def test_update():
    cell = Cell(state=DeadState())
    cell.update(3)
    assert cell.is_alive() == True
