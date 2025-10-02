"""
Game class that manages the game state and observers.
Uses Observer pattern to notify observers of state changes.
"""


class GameObserver:
    """Abstract base class for game observers."""
    
    def on_game_state_changed(self, is_running):
        """Called when game running state changes."""
        pass
    
    def on_generation_changed(self, generation):
        """Called when generation number changes."""
        pass


class Game:
    """Main game controller using Observer pattern."""
    
    def __init__(self, grid):
        self.grid = grid
        self.generation = 0
        self.is_running = False
        self.observers = []
    
    def add_observer(self, observer):
        """Add an observer to the game."""
        self.observers.append(observer)
    
    def remove_observer(self, observer):
        """Remove an observer from the game."""
        if observer in self.observers:
            self.observers.remove(observer)
    
    def notify_state_changed(self):
        """Notify all observers of state change."""
        for observer in self.observers:
            observer.on_game_state_changed(self.is_running)
    
    def notify_generation_changed(self):
        """Notify all observers of generation change."""
        for observer in self.observers:
            observer.on_generation_changed(self.generation)
    
    def start(self):
        """Start the game simulation."""
        self.is_running = True
        self.notify_state_changed()
    
    def pause(self):
        """Pause the game simulation."""
        self.is_running = False
        self.notify_state_changed()
    
    def toggle_pause(self):
        """Toggle pause state."""
        if self.is_running:
            self.pause()
        else:
            self.start()
    
    def step(self):
        """Advance one generation."""
        self.grid.update()
        self.generation += 1
        self.notify_generation_changed()
    
    def reset(self):
        """Reset the game."""
        self.grid.clear()
        self.generation = 0
        self.is_running = False
        self.notify_state_changed()
        self.notify_generation_changed()
    
    def update(self):
        """Update game (called every frame)."""
        if self.is_running:
            self.step()
