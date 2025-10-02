# py-game-of-life

Conway's Game of Life implementation using design patterns and Pygame.

## Features

- Clean separation of concerns using design patterns:
  - **State Pattern**: Cell states (alive/dead)
  - **Observer Pattern**: Game state notifications
  - **Strategy Pattern**: Rendering strategies
- Interactive GUI with Pygame
- Proper project structure with separate source and test directories

## Project Structure

```
py-game-of-life/
├── src/                    # Source code
│   ├── __init__.py
│   ├── cell.py            # Cell class with State pattern
│   ├── grid.py            # Grid/Board management
│   ├── game.py            # Game controller with Observer pattern
│   ├── renderer.py        # Renderer with Strategy pattern
│   └── main.py            # Main entry point
├── tests/                  # Unit tests
│   ├── __init__.py
│   ├── test_cell.py       # Cell tests (implemented)
│   ├── test_grid.py       # Grid tests (placeholder)
│   ├── test_game.py       # Game tests (placeholder)
│   └── test_renderer.py   # Renderer tests (placeholder)
├── requirements.txt        # Project dependencies
└── README.md              # This file
```

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the game:
```bash
python -m src.main
```

Or:
```bash
cd src
python main.py
```

## Controls

- **SPACE**: Start/Pause the simulation
- **R**: Reset the grid and generation counter
- **C**: Clear the grid
- **Left Click**: Toggle cell state (alive/dead)
- **ESC**: Exit the game

## Running Tests

Run all tests:
```bash
python -m unittest discover tests
```

Run specific test file:
```bash
python -m unittest tests.test_cell
```

## Design Patterns

### State Pattern (Cell)
The cell uses the State pattern to manage its alive/dead states. Each state knows how to transition to the next state based on the Game of Life rules.

### Observer Pattern (Game)
The game uses the Observer pattern to notify observers when the game state changes (running/paused) or when the generation advances.

### Strategy Pattern (Renderer)
The renderer uses the Strategy pattern to allow different rendering approaches. Currently implements a grid-based rendering strategy.

## Game of Life Rules

1. Any live cell with 2 or 3 live neighbors survives
2. Any dead cell with exactly 3 live neighbors becomes alive
3. All other cells die or stay dead