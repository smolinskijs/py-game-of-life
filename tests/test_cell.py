"""
Unit tests for Cell class.
"""
import pytest

from pgol.cell import AliveState, DeadState

@pytest.fixture
def alive_state():
    return AliveState()

def test_alive_state(alive_state):
    assert alive_state.is_alive() == True

def test_str(alive_state):
    assert str(alive_state) == "Alive"

def test_mszypryt_str(alive_state):
    assert alive_state.__str__() == "Alive"

def test_next_gen_alive(alive_state):
    assert isinstance(alive_state.get_next_state(3),AliveState)

def test_next_gen_dead(alive_state):
    assert isinstance(alive_state.get_next_state(1),DeadState)

@pytest.mark.parametrize("num_neighbors,cls",
                         [
                             (3, AliveState),
                             (2, AliveState),
                             (1, DeadState),
                             (4, DeadState),
                         ])
def test_gen_next(alive_state, num_neighbors, cls):
    assert isinstance(alive_state.get_next_state(num_neighbors),cls)