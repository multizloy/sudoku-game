import pygame, time
from settings import CELL_SIZE

pygame.font.init()

class Clock:
    def __init__(self):
        """
        Create a new Clock object that can be used to track an amount of time.

        The clock also provides several functions to help control a game's framerate.

        :param self: this object
        :param start_time: the time at which the timer started
        :param elapsed_time: the time elapsed since the timer started
        :param font: the font to use for rendering the timer
        :param message_color: the color of the text
        """
        self.start_time = None
        self.elapsed_time = 0
        self.font = pygame.font.SysFont("monospace", CELL_SIZE[0])
        self.message_color = pygame.Color("black")

    # Start the timer
    def start_timer(self):
        """
        Start the timer.

        This function is used to mark the beginning of a block of code that needs to be timed.

        :param self: this object
        """
        self.start_time = time.time()

    # Update the timer
    def update_timer(self):
        """
        Update the timer.

        This function should be called at the end of a loop iteration to update the
        timer. It calculates the time elapsed since the timer was started and
        assigns it to the elapsed_time attribute of the timer object.

        :param self: this object
        """
        if self.start_time is not None:
            self.elapsed_time = time.time() - self.start_time

    # Display the timer
    def display_timer(self):
        """
        Return a surface with the time elapsed since the timer was started.

        :param self: this object
        :return: a surface with the time elapsed since the timer was started
        """
        secs = int(self.elapsed_time % 60)
        mins = int(self.elapsed_time / 60)
        my_time = self.font.render(f"{mins:02}:{secs:02}", True, self.message_color)
        return my_time

    # Stop the timer
    def stop_timer(self):
        """
        Stop the timer.

        This function is used to mark the end of a block of code that needs to be timed.

        :param self: this object
        """
        self.start_time = None