"""
Main entry point for Conway's Game of Life.
"""
import pygame
import sys
from pgol.grid import Grid
from pgol.game import Game
from pgol.renderer import Renderer, GridRenderStrategy


class GameOfLife:
    """Main application class."""
    
    def __init__(self, width=80, height=60, cell_size=10):
        pygame.init()
        
        self.width = width
        self.height = height
        self.cell_size = cell_size
        
        # Create window
        screen_width = width * cell_size
        screen_height = height * cell_size
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Conway's Game of Life")
        
        # Create game components
        self.grid = Grid(width, height)
        self.game = Game(self.grid)
        self.renderer = Renderer(self.screen, cell_size)
        
        # Setup font
        self.font = pygame.font.Font(None, 24)
        
        # FPS control
        self.clock = pygame.time.Clock()
        self.fps = 10
    
    def handle_events(self):
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game.toggle_pause()
                elif event.key == pygame.K_r:
                    self.game.reset()
                elif event.key == pygame.K_c:
                    self.grid.clear()
                    self.game.generation = 0
                elif event.key == pygame.K_ESCAPE:
                    return False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    grid_x = mouse_x // self.cell_size
                    grid_y = mouse_y // self.cell_size
                    self.grid.toggle_cell(grid_x, grid_y)
        
        return True
    
    def update(self):
        """Update game state."""
        self.game.update()
    
    def render(self):
        """Render the game."""
        self.screen.fill((0, 0, 0))
        self.renderer.render(self.grid)
        self.renderer.render_ui(self.game, self.font)
        pygame.display.flip()
    
    def run(self):
        """Main game loop."""
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.fps)
        
        pygame.quit()
        sys.exit()


def main():
    """Entry point."""
    game = GameOfLife(width=80, height=60, cell_size=10)
    game.run()


if __name__ == "__main__":
    main()
