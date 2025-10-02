"""
Renderer class for visualizing the Game of Life.
Uses Strategy pattern for different rendering approaches.
"""
import pygame


class RenderStrategy:
    """Abstract base class for rendering strategies."""
    
    def render(self, screen, grid, cell_size):
        raise NotImplementedError


class GridRenderStrategy(RenderStrategy):
    """Strategy for rendering the grid with cells and lines."""
    
    def __init__(self, alive_color=(0, 255, 0), dead_color=(0, 0, 0), grid_color=(40, 40, 40)):
        self.alive_color = alive_color
        self.dead_color = dead_color
        self.grid_color = grid_color
    
    def render(self, screen, grid, cell_size):
        """Render the grid with cells and grid lines."""
        # Draw cells
        for y in range(grid.height):
            for x in range(grid.width):
                cell = grid.get_cell(x, y)
                color = self.alive_color if cell.is_alive() else self.dead_color
                
                rect = pygame.Rect(
                    x * cell_size,
                    y * cell_size,
                    cell_size,
                    cell_size
                )
                pygame.draw.rect(screen, color, rect)
        
        # Draw grid lines
        for x in range(grid.width + 1):
            pygame.draw.line(
                screen,
                self.grid_color,
                (x * cell_size, 0),
                (x * cell_size, grid.height * cell_size)
            )
        
        for y in range(grid.height + 1):
            pygame.draw.line(
                screen,
                self.grid_color,
                (0, y * cell_size),
                (grid.width * cell_size, y * cell_size)
            )


class Renderer:
    """Main renderer class that uses a rendering strategy."""
    
    def __init__(self, screen, cell_size, strategy=None):
        self.screen = screen
        self.cell_size = cell_size
        self.strategy = strategy if strategy else GridRenderStrategy()
    
    def set_strategy(self, strategy):
        """Change the rendering strategy."""
        self.strategy = strategy
    
    def render(self, grid):
        """Render the grid using the current strategy."""
        self.strategy.render(self.screen, grid, self.cell_size)
    
    def render_ui(self, game, font):
        """Render UI information."""
        # Render generation counter
        gen_text = font.render(f"Generation: {game.generation}", True, (255, 255, 255))
        self.screen.blit(gen_text, (10, 10))
        
        # Render status
        status = "Running" if game.is_running else "Paused"
        status_text = font.render(f"Status: {status}", True, (255, 255, 255))
        self.screen.blit(status_text, (10, 40))
        
        # Render alive count
        alive_count = game.grid.get_alive_count()
        count_text = font.render(f"Alive: {alive_count}", True, (255, 255, 255))
        self.screen.blit(count_text, (10, 70))
        
        # Render instructions
        instructions = [
            "SPACE: Start/Pause",
            "R: Reset",
            "C: Clear",
            "Click: Toggle cell"
        ]
        y_offset = 110
        for instruction in instructions:
            inst_text = font.render(instruction, True, (200, 200, 200))
            self.screen.blit(inst_text, (10, y_offset))
            y_offset += 25
