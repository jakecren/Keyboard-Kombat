"""  Imports  """
import pygame  # Importing PyGame Library
from mainGameScene import _mainGameScene  # Importing classes from other files
from titleScene import titleScene
from settingsScene import settingsScene
from instructionsScene import instructionsScene


"""  Class-Start  """
class masterGameManager:
    """
    Master Game Manager:
    Controls scene selection and excecution of scenes.
    """

    def __init__(self, currentScene):
        """  Set Class Variables  """
        self.currentScene = currentScene  # Setting class initialisation parameters


    """  Set Scene Method  """
    def set_scene(self, sceneName):
        # Used to set active scene (to be executed in the next update).
        self.currentScene = sceneName


    def runScene(self):
        eval(f"{self.currentScene}.runScene()")  # Runs scene defined in the scene selection function


"""  Initialization  """
pygame.init()  # Initialising PyGame Library

gameDisplay = pygame.display.set_mode((0,0), pygame.FULLSCREEN)  # Creating Fullscreen Window - 0,0 tuple sets window to the device's native resolution
# gameDisplay = pygame.display.set_mode((1366,786))
pygame.display.set_caption("Keyboard Kombat")
clock = pygame.time.Clock()  # Initialises an instance of pygames inbuilt clock for controling game time (fps, etc).
master = masterGameManager(None)  # Initialises an instance of the masterGameManager class.

titleScene = titleScene(gameDisplay, clock, master)  # Initialises an instance of each scene used in the game.
settingsScene = settingsScene(gameDisplay, clock, master)
instructionsScene = instructionsScene(gameDisplay, clock, master)
mainGameScene = _mainGameScene(gameDisplay, clock, master)


"""  Main Game Loop  """
# Infinate Game loop
while True:
    if master.currentScene == None:  #If none is defined, sets the active scene to 'titleScene'
        master.set_scene("titleScene")
        print("No scene selected, going to scene", master.currentScene +"\n")
    elif master.currentScene == "resetGame":  # If 'resetGame' is passed as the active scene, the game re-initialises the Main Game Scene in order to reset the game.  The Title Scene is then set as the active scene.
        mainGameScene = _mainGameScene(gameDisplay, clock, master)
        master.set_scene("titleScene")

    """  Scene Handling  """
    master.runScene()  # Runs active scene defined with the masterGameManager.set_scene function.
