"""  Imports  """
import pygame
from functionality import button


"""  Set Global Variables  """
titleImg = pygame.image.load("images/titleScreen.png")

white = (255, 255, 255)
black = (0, 0, 0)


"""  Class-Start  """
class titleScene:
    """
    Title/Menu Scene

    Methods:
    runScene(gameDisplay, clock, master)
    'gameDisplay' represents pygame's display.
    'clock' represents pygame's time.Clock function.
    'master' represents the 'masterGameManager' class, used in 'runScene' to swap scenes.
    """

    gameExit = False

    def __init__(self, gameDisplay, clock, master):
        """  Set Class Variables  """
        self.gameDisplay = gameDisplay
        self.clock = clock
        self.master = master
        self.currentScene = None
        self.mainGameStatus = "New Game"

        self.exitButton = button("ellipse", self.gameDisplay, 980, 554, 246, 106, black, white, white, black, 10, "Exit", "quit")
        self.settingsButton = button("ellipse", self.gameDisplay, 980, 440, 246, 106, black, white, white, black, 10, "Settings", "settingsScene")
        self.startButton = button("ellipse", self.gameDisplay, 965, 297, 276, 138, black, white, white, black, 10, self.mainGameStatus, "mainGameScene")
        self.resetGameButton = button("ellipse", self.gameDisplay, 980, 187, 246, 106, black, white, white, black, 10, "Reset Game", "resetGame")
        self.instructionsButton = button("ellipse", self.gameDisplay, 980, 73, 246, 106, black, white, white, black, 10, "Instructions", "instructionsScene")

        self.buttonsList = ["self.exitButton", "self.settingsButton", "self.startButton", "self.resetGameButton", "self.instructionsButton"]


    """  Run Scene Method  """
    def runScene(self):
        self.gameDisplay.blit(titleImg, (0,0))
        while True:
            self.setReturn = (False, None)


            """  Event Handling  """
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    self.gameExit = True

                #Buttons
                for buttons in self.buttonsList:  exec(f'''
if event.type == pygame.MOUSEBUTTONDOWN:
    if {buttons}.isOver(pos):
        self.setReturn = (True, "{buttons}.command")

elif event.type == pygame.MOUSEMOTION:
    if {buttons}.isOver(pos):
        {buttons}.currentColour = {buttons}.rolloverColour
        {buttons}.currentTextColour = {buttons}.textRolloverColour
    else:
        {buttons}.currentColour = {buttons}.colour
        {buttons}.currentTextColour = {buttons}.textColour''')


            """  Main Logic  """
            for button in self.buttonsList:
                if button == "self.startButton":
                    exec(f"{button}.draw(self.mainGameStatus)")
                else:
                    exec(f"{button}.draw()")

            """  Update Handling  """
            pygame.display.update()
            self.clock.tick(15)


            """  Returns  """
            if self.setReturn[0] == True:
                if eval(self.setReturn[1]) == "quit":
                    pygame.quit(), quit()
                elif eval(self.setReturn[1]) == "mainGameScene":
                    self.mainGameStatus = "Resume Game"
                    pygame.display.update()
                elif eval(self.setReturn[1]) == "resetGame":
                    self.mainGameStatus = "New Game"
                    pygame.display.update()
                self.master.set_scene(eval(self.setReturn[1]))
                return
