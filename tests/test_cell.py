"""
Unit tests for Cell class.
"""
import pytest

from pgol.cell import AliveState

def test_alive_state():
    alive_state = AliveState()
    assert alive_state.is_alive() == True