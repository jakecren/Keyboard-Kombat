"""  Imports  """
import pygame
from functionality import *


"""  Class-Start  """
class instructionsScene:
    def __init__(self, gameDisplay, clock, master):
        """  Set Class Variables  """
        self.gameDisplay = gameDisplay
        self.clock = clock
        self.master = master
        self.endMainGameLoop = False

        self.backButton = button("rect", self.gameDisplay, 1000, 600, 150, 100, (0,0,0), (255,255,255), (255,255,255), (0,0,0), 10, "Back", "titleScene")


    """  Run Scene Method  """
    def runScene(self):
        while True:
            self.gameDisplay.fill((255,255,255))

            """  Event Handling  """
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit(), quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.backButton.isOver(pos):
                        self.master.set_scene("titleScene")
                        self.endMainGameLoop = True

                elif event.type == pygame.MOUSEMOTION:
                    if self.backButton.isOver(pos):
                        self.backButton.currentColour = self.backButton.rolloverColour
                        self.backButton.currentTextColour = self.backButton.textRolloverColour
                    else:
                        self.backButton.currentColour = self.backButton.colour
                        self.backButton.currentTextColour = self.backButton.textColour


            """  Main Drawing  """
            self.backButton.draw()


            """  Update Handling  """
            pygame.display.update()
            self.clock.tick(60)


            """  Returns  """
            if self.endMainGameLoop == True:
                return
