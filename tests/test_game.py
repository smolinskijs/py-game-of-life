

"""
Unit tests for Game class.
"""

import pytest

from pgol.game import Game, GameObserver


class MiniGrid:

    def __init__(self):
        self.update_calls = 0
        self.clear_calls = 0

    def update(self):
        self.update_calls += 1

    def clear(self):
        self.clear_calls += 1


class RecordingObserver(GameObserver):

    def __init__(self):
        self.state_events = []
        self.generation_events = []

    def on_game_state_changed(self, is_running):
        self.state_events.append(is_running)

    def on_generation_changed(self, generation):
        self.generation_events.append(generation)


def test_initial_state():
    grid = MiniGrid()
    game = Game(grid)

    assert game.is_running is False
    assert game.generation == 0
    assert game.observers == []

    assert grid.update_calls == 0
    assert grid.clear_calls == 0


def test_add_and_remove_observer():
    grid = MiniGrid()
    game = Game(grid)
    obs = RecordingObserver()

    game.add_observer(obs)
    assert obs in game.observers

    game.remove_observer(obs)
    assert obs not in game.observers


def test_start_notifies_running_true():
    grid = MiniGrid()
    game = Game(grid)
    obs = RecordingObserver()
    game.add_observer(obs)

    game.start()

    assert game.is_running is True
    assert obs.state_events == [True]

    assert game.generation == 0
    assert obs.generation_events == []


def test_pause_notifies_running_false():
    grid = MiniGrid()
    game = Game(grid)
    obs = RecordingObserver()
    game.add_observer(obs)

    game.start()
    game.pause()

    assert game.is_running is False

    assert obs.state_events == [True, False]
    assert game.generation == 0
    assert obs.generation_events == []


def test_toggle_pause_toggles_and_notifies():
    grid = MiniGrid()
    game = Game(grid)
    obs = RecordingObserver()
    game.add_observer(obs)


    game.toggle_pause()
    assert game.is_running is True

    game.toggle_pause()
    assert game.is_running is False

    assert obs.state_events == [True, False]
    assert game.generation == 0
    assert obs.generation_events == []


def test_step_updates_grid_increments_generation_and_notifies_generation():
    grid = MiniGrid()
    game = Game(grid)
    obs = RecordingObserver()
    game.add_observer(obs)

    assert game.generation == 0
    assert grid.update_calls == 0

    game.step()

    assert grid.update_calls == 1
    assert game.generation == 1
    assert obs.generation_events == [1]

    assert obs.state_events == []


    game.step()
    assert grid.update_calls == 2
    assert game.generation == 2
    assert obs.generation_events == [1, 2]


def test_reset_clears_grid_resets_state_and_notifies_both():
    grid = MiniGrid()
    game = Game(grid)
    obs = RecordingObserver()
    game.add_observer(obs)

    game.start()
    game.step()  # generation -> 1


    assert game.is_running is True
    assert game.generation == 1
    assert grid.update_calls == 1
    assert obs.state_events == [True]
    assert obs.generation_events == [1]

    game.reset()


    assert grid.clear_calls == 1

    assert game.is_running is False
    assert game.generation == 0

    assert obs.state_events == [True, False]
    assert obs.generation_events == [1, 0]


def test_update_calls_step_only_when_running():
    grid = MiniGrid()
    game = Game(grid)
    obs = RecordingObserver()
    game.add_observer(obs)


    game.update()
    assert grid.update_calls == 0
    assert game.generation == 0
    assert obs.generation_events == []


    game.start()
    game.update()
    assert grid.update_calls == 1
    assert game.generation == 1
    assert obs.generation_events == [1]


    game.pause()
    game.update()
    assert grid.update_calls == 1
    assert game.generation == 1
    assert obs.generation_events == [1]
