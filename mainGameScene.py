"""  Imports  """
import pygame, random
from functionality import *


"""  Set Global Variables  """
mainGameImg = pygame.image.load("images/mainGame.png")
crotchetP = pygame.image.load("images/Crotchet P.png")
crotchetD = pygame.image.load("images/Crotchet D.png")

black = (0, 0, 0)
white = (255, 255, 255)


"""  Class-Start  """
class _mainGameScene:
    """
    Main Game Scene

    Methods:
    runScene(gameDisplay, clock, master, gameExit)
    'gameDisplay' represents pygame's display.
    'clock' represents pygame's time.Clock function.
    'master' represents the 'masterGameManager' class, used in 'runScene' to swap scenes.
    """


    def __init__(self, gameDisplay, clock, master):
        """  Set Class Variables  """
        self.gameDisplay = gameDisplay
        self.clock = clock
        self.master = master
        self.noteToPlay = False
        self.notePlayed = None
        self.changeNote = True
        self.playerHeath = 1
        self.AiHealth = 1
        self.mainTimerSeconds = 100
        self.noteTimerMAX = 10
        self.noteTimerSeconds = 0
        self.score = 100
        self.changeNote = True
        self.endMainGameLoop = False

        self.mainTimerStartTicks = pygame.time.get_ticks()

        self.mainTimerText = text(452, 55, self.gameDisplay, (0,0,0), 60)
        self.noteToPlayText = text(1250, 120, self.gameDisplay, (0,0,0), 150)
        self.PAUSED_titleText = text(545, 220, self.gameDisplay, (0,0,0), 100)
        self.playerName = text(30, 60, self.gameDisplay, (0,0,0), 45)
        self.AiName = text(816, 60, self.gameDisplay, (0,0,0), 45)

        self.noteTimeStatus = statusBar(992, 360, 348, 45, self.gameDisplay, (0,0,0), (86,204,32), False)
        self.playerHeathStatus = statusBar(21, 52, 426, 44, self.gameDisplay, (0,0,0), (255,0,0), True)
        self.AiHealthStatus = statusBar(531, 52, 426, 44, self.gameDisplay, (0,0,0), (255,0,0), True)

        self.PAUSED_resumeButton = button("rect", self.gameDisplay, 583, 234+80, 200, 75, (0,0,0), (200,200,200), (230,230,230), (0,0,0), 0, "Resume", "unpause")
        self.PAUSED_backTitleButton = button("rect", self.gameDisplay, 495, 324+80, 376, 75, (0,0,0), (200,200,200), (230, 230, 230), (0,0,0), 0, "Quit to Title Screen", "quit")
        self.PAUSED_exitButton = button("rect", self.gameDisplay, 521, 414+80, 324, 75, (0,0,0), (200,200,200), (230, 230, 230), (0,0,0), 0, "Exit to Desktop", "quit")

        self.pianoKeysDict = {"G5": (1074,665,69,112), "F5": (1003,665,69,112), "E5": (932,665,70,112), "D5": (862,665,68,112), "C5": (791, 665, 70, 112), "B4": (720, 665, 70, 112), "A4": (649, 665, 70, 112), "G4": (579,665,69,112), "F4": (508,665,70,112), "E4": (437,665,70,112), "D4": (367,665,69,112), "C4": (296,665,69,112)}
        self.pianoKeysList = ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5", "D5", "E5", "F5", "G5"]
        self.i = 0

        for key in self.pianoKeysDict: exec(f"self.PIANOSOUND_{key} = pygame.mixer.Sound('sound/Piano Samples/{key}.wav')")
        for key in self.pianoKeysDict: exec(f"self.PIANOKEY_{key} = button(None, self.gameDisplay, {self.pianoKeysDict[key][0]}, {self.pianoKeysDict[key][1]}, {self.pianoKeysDict[key][2]}, {self.pianoKeysDict[key][3]}, None, None, None, None, None, None, None)")

        global settingsScene
        from _Main import settingsScene
        if settingsScene.gameMode == "Battle": self.noteTimerMin = 3.5
        else: self.noteTimerMin = 10


    """  Run Scene Method  """
    def runScene(self):
        def pause(PoW="PAUSED"):
            pygame.draw.rect(self.gameDisplay, (10,10,10), (480, 181, 406,406))
            pygame.draw.rect(self.gameDisplay, (255,255,255), (483, 184, 400,400))
            if PoW == "PAUSED":
                self.PAUSED_resumeButton.draw()
            self.PAUSED_exitButton.draw()
            self.PAUSED_backTitleButton.draw()
            Pfont = pygame.font.SysFont('', 100)
            PtextWidth, PtextHeight = Pfont.size(PoW)
            self.PAUSED_titleText.placetext(PoW, x=((1366/2) - (PtextWidth/2)))
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    pos = pygame.mouse.get_pos()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            return
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.PAUSED_resumeButton.isOver(pos):
                            return
                        elif self.PAUSED_backTitleButton.isOver(pos):
                            self.master.set_scene("titleScene")
                            self.endMainGameLoop = True
                            return
                        elif self.PAUSED_exitButton.isOver(pos):
                            pygame.quit(), quit()


        def noteAndTime():
            if self.changeNote == True:
                self.changeNote = None
                self.notePlayed = None

                if settingsScene.gameMode == "Battle":
                    # Random Note Selection Method:
                    randint = random.randint(0, 11)
                    self.noteToPlay = self.pianoKeysList[randint]

                else:
                    # Sequenced Note Selection Method (Good For Songs)
                    # Reference pianoKeysList - ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5", "D5", "E5", "F5", "G5"]
                    #                             0     1     2     3     4     5     6     7     8     9     10    11
                    isequence = [7, 6, 5, 4, 3, 2, 1, 0, 4, 5, 5, 6, 6, 7, 7, 7, 6, 5, 4, 4, 3, 2, 7, 7, 6, 5, 4, 4, 3, 2, 2, 2, 2, 2, 2, 3, 4, 3, 2, 1, 1, 1, 1, 2, 3, 2, 1, 0, 7, 5, 4, 3, 2, 3, 2, 1, 0]
                    self.noteToPlay = self.pianoKeysList[isequence[self.i]]
                    self.i += 1
                    if self.i == len(isequence):
                        self.i = 0

                self.pianoKeysForCrotchetDict = {"C4": 250, "D4": 231, "E4": 216, "F4": 197, "G4": 181, "A4": 162, "B4": 146, "C5": 128, "D5": 111, "E5": 93, "F5": 76, "G5": 59}
                self.noteTimerStartTicks = pygame.time.get_ticks()
            if self.noteToPlay in self.pianoKeysList[:6]:
                self.gameDisplay.blit(crotchetD, (1127,self.pianoKeysForCrotchetDict[self.noteToPlay]-67))
            else:
                self.gameDisplay.blit(crotchetP, (1127,self.pianoKeysForCrotchetDict[self.noteToPlay]))


        # def playMusic(dest):
        #     pygame.mixer.music.load(dest)
        #     pygame.mixer.music.play(-1)
        #
        # playMusic("sound/Piano.ff.Db3.wav")


        while True:
            self.mainTimerSeconds = 150-int(((pygame.time.get_ticks()-self.mainTimerStartTicks)/1000))

            pygame.display.flip()

            """  Event Handling  """
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit(), quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for key in self.pianoKeysList:
                        exec(f"""
if self.PIANOKEY_{key}.isOver(pos):
    pygame.mixer.Sound.play(self.PIANOSOUND_{key})
    self.notePlayed = '{key}'""")


            """  Main Logic  """
            self.gameDisplay.blit(mainGameImg, (0,0))

            noteAndTime()
            if self.notePlayed != None:
                if self.notePlayed == self.noteToPlay:
                    self.changeNote = True
                    if self.noteTimerMAX >= self.noteTimerMin:
                        self.noteTimerMAX -= 0.5
                    if settingsScene.gameMode == "Song": self.AiHealth -= 0.017543859649123
                    else: self.AiHealth -= 0.05
                if self.notePlayed != self.noteToPlay:
                    self.changeNote = False
                    self.playerHeath -= 0.05
                    self.noteTimerMAX += 0.05
                    self.notePlayed = None


            self.noteTimerSeconds = self.noteTimerMAX-((pygame.time.get_ticks()-self.noteTimerStartTicks)/1000)
            self.noteTimerPercent = ((100/self.noteTimerMAX) * self.noteTimerSeconds)/100

            if self.noteTimerPercent <= 0.01:
                self.changeNote = True
                self.playerHeath -= 0.05

            self.mainTimerText.placetext(str(self.mainTimerSeconds))
            self.noteToPlayText.placetext(self.noteToPlay[0])

            self.noteTimeStatus.draw(self.noteTimerPercent)
            self.playerHeathStatus.draw(self.playerHeath)
            self.AiHealthStatus.draw(self.AiHealth)

            self.playerName.placetext("Sub-Zero")
            self.AiName.placetext("Scorpion")

            if self.playerHeath <= 0:
                pause(PoW="DEFEATED")
            elif self.AiHealth <= 0:
                pause(PoW="WINNER")

            if self.endMainGameLoop == True:
                return


            """  Update Handling  """
            pygame.display.update()
            self.clock.tick(60)
