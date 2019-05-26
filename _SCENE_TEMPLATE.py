"""  Imports  """
import pygame
from functionality import *


"""  Set Global Variables  """
pass


"""  Class-Start  """
class CLASS_NAME:
    """
    pass
    """

    def __init__(self, gameDisplay, clock, master):
        """  Set Class Variables  """
        self.gameDisplay = gameDisplay
        self.clock = clock
        self.master = master
        self.endMainGameLoop = False


    """  Run Scene Method  """
    def runScene(self):
        while True:
            self.gameDisplay.fill(255,255,255)

            """  Event Handling  """
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit(), quit()


            """  Main Drawing  """
            pass


            """  Main Logic  """
            pass


            """  Update Handling  """
            pygame.display.update()
            self.clock.tick(60)


            """  Returns  """
            if self.endMainGameLoop == True:
                return
