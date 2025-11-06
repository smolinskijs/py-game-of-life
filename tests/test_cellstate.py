import pytest

from pgol.cell import CellState

@pytest.fixture()
def cs():
    return CellState()

def test_cellstate_is_alive(cs):
    with pytest.raises(NotImplementedError):
        cs.is_alive()

def test_cellstate_get_next_state(cs):
    with pytest.raises(NotImplementedError):
        cs.get_next_state(1)

def test_cellstate_str(cs):
    with pytest.raises(NotImplementedError):
        cs.__str__()