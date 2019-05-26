"""  Imports  """
import pygame
from functionality import *


"""  Set Global Variables  """
pass


"""  Class-Start  """
class settingsScene:
    """
    pass
    """

    def __init__(self, gameDisplay, clock, master):
        """  Set Class Variables  """
        self.gameDisplay = gameDisplay
        self.clock = clock
        self.master = master
        self.endMainGameLoop = False
        self.gameMode = "Song"

        self.backButton = button("rect", self.gameDisplay, 1000, 600, 150, 100, (0,0,0), (255,255,255), (255,255,255), (0,0,0), 10, "Back", "titleScene")
        self.changeGameModeButton = button("rect", self.gameDisplay, ((1366/2)-(450/2)), 380, 450, 100, (0,0,0), (255,255,255), (255,255,255), (0,0,0), 10, "Change to Battle Mode", None)

        self.headingText = text(200, 80, self.gameDisplay, (0,0,0), 85)
        self.gameModeText = text(0, 300, self.gameDisplay, (0,0,0), 45, message=("Current Game Mode: " + self.gameMode))

        self.todo = "titleScene"


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
                        self.master.set_scene(self.todo)
                        self.endMainGameLoop = True
                    elif self.changeGameModeButton.isOver(pos):
                        if self.gameMode == "Song": self.gameMode = "Battle"
                        else: self.gameMode = "Song"
                        self.todo = "resetGame"

                elif event.type == pygame.MOUSEMOTION:
                    if self.backButton.isOver(pos):
                        self.backButton.currentColour = self.backButton.rolloverColour
                        self.backButton.currentTextColour = self.backButton.textRolloverColour
                    else:
                        self.backButton.currentColour = self.backButton.colour
                        self.backButton.currentTextColour = self.backButton.textColour

                    if self.changeGameModeButton.isOver(pos):
                        self.changeGameModeButton.currentColour = self.changeGameModeButton.rolloverColour
                        self.changeGameModeButton.currentTextColour = self.changeGameModeButton.textRolloverColour
                    else:
                        self.changeGameModeButton.currentColour = self.changeGameModeButton.colour
                        self.changeGameModeButton.currentTextColour = self.changeGameModeButton.textColour


            """  Main Drawing  """
            self.headingText.placetext("Settings")
            self.gameModeText.placetext(("Current Game Mode: " + self.gameMode), x=((1366/2) - (self.gameModeText.textWidth/2)))

            self.backButton.draw()
            if self.gameMode == "Song":
                self.changeGameModeButton.draw(text="Change to Battle Mode")
            else:
                self.changeGameModeButton.draw(text="Change to Song Mode")

            """  Main Logic  """
            pass


            """  Update Handling  """
            pygame.display.update()
            self.clock.tick(60)


            """  Returns  """
            if self.endMainGameLoop == True:
                return
