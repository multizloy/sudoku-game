import pygame, sys
from settings import WIDTH, HEIGHT, CELL_SIZE
from table import Table

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT + (CELL_SIZE[1] * 3)))
pygame.display.set_caption("Sudoku")

pygame.font.init()


class Main:
    def __init__(self, screen: pygame.Surface) -> None:
        """Initialise the main game class

        Args:
            screen (pygame.Surface): The surface to draw onto

        Sets up the main game class with the given screen, and sets up a few fonts
        and a colour for use later.
        """
        self.screen = screen
        self.FPS = pygame.time.Clock()
        self.lives_font = pygame.font.SysFont("comicsans", CELL_SIZE[0] // 2)
        self.message_font = pygame.font.SysFont("comicsans", CELL_SIZE[0])
        self.color = pygame.Color("darkblue")

    def main(self):
        """Runs the main game loop.

        This is the main entry point for the game, and is responsible for setting up
        the game state, handling events, and updating the display.

        The game loop runs until the user closes the window, at which point it exits
        cleanly.

        The game loop consists of the following steps:

        1. Fill the screen with gray to erase the old frame.
        2. Handle any events that have occurred, such as the user clicking or pressing
           a key.
        3. If the user has clicked, handle the click by calling the
           `handel_mouse_click` method of the `Table` class.
        4. Draw the lives left on the screen.
        5. If the game is over, draw a message on the screen indicating whether the
           user has won or lost.
        6. Update the display to show the new frame.
        7. Cap the frame rate to prevent the game from running too fast.

        The game loop continues until the user closes the window, at which point the
        game exits cleanly.
        """
        table = Table(self.screen)
        while True:
            self.screen.fill("gray")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not table.game_over:
                        table.handle_mouse_click(event.pos)
            if not table.game_over:
                my_lives = self.lives_font.render(
                    f"Lives Left: {table.lives}", True, pygame.Color("black")
                )
                self.screen.blit(
                    my_lives,
                    (
                        (WIDTH // table.SRN) - (CELL_SIZE[0] // 2),
                        HEIGHT + (CELL_SIZE[1] * 2.2),
                    ),
                )
            else:
                if table.lives <= 0:
                    message = self.message_font.render(
                        "GAME OVER!!", True, pygame.Color("red")
                    )
                    self.screen.blit(
                        message,
                        (
                            CELL_SIZE[0] + (CELL_SIZE[0] // 2),
                            HEIGHT + (CELL_SIZE[1] * 2),
                        ),
                    )
                elif table.lives > 0:
                    message = self.message_font.render(
                        "You Made It!!!", True, self.color
                    )
                    self.screen.blit(
                        message, (CELL_SIZE[0], HEIGHT + (CELL_SIZE[1] * 2))
                    )
            table.update()
            pygame.display.flip()
            self.FPS.tick(30)


if __name__ == "__main__":
    play = Main(screen)
    play.main()
