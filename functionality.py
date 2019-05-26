"""  Imports  """
import pygame  # Importing PyGame Library


"""  Classes  """
class button:
    """
    Button Class:
    Used to create clickable buttons.
    """
    def __init__(self, type, display, x, y, width, height, colour, rolloverColour, textColour, textRolloverColour, outline, text, sceneToGoTo):
        # Setting class variables based on parameters recieved on initialisation.
        self.type = type
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rolloverColour = rolloverColour
        self.textColour = textColour
        self.textRolloverColour = textRolloverColour
        self.text = text
        self.command = sceneToGoTo
        self.currentColour = self.colour
        self.currentTextColour = self.textColour
        self.outline = outline


    def draw(self, text=None):  #Function used to draw the button onto the screen/window.
        if text!= None:  # If a parameter is provided for 'text' set it to the 'self.text' variable.
            self.text = text

        if self.type != None:  #If 'self.type' variable
            if self.outline != None and type(self.outline) == int:
                eval(f"pygame.draw.{self.type}(self.display, (0, 0, 0), (self.x - self.outline/2, self.y - self.outline/2, self.width + self.outline, self.height + self.outline))")
            eval(f"pygame.draw.{self.type}(self.display, self.currentColour, (self.x, self.y, self.width, self.height))")

            if self.text != '':
                font = pygame.font.SysFont('', 55)
                text = font.render(self.text, 1, self.currentTextColour)
                self.display.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))


    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            return False


    def pressed(self):
        return eval(self.command)



class text():
    """
    Text Class:
    Used to place text onto the screen.
    """
    def __init__(self, x, y, display, textColor, fontSize, boxed=False, message=""):
        "-------Setting Values---------"
        self.x = x
        self.y = y
        self.color = textColor
        self.fontSize = fontSize
        self.display = display
        self.boxed = boxed
        self.msg = message
        self.font = pygame.font.SysFont('', self.fontSize)
        self.textWidth, self.textHeight = self.font.size(self.msg)

    def placetext(self, message, x=None, y=None):
        if x != None: self.x = x
        if y != None: self.y = y
        self.msg = message
        "------Main Logic------"
        self.font = pygame.font.SysFont('', self.fontSize)
        if self.boxed == True:
            self.textWidth, self.textHeight = self.font.size(self.msg)
            pygame.draw.rect(self.display, (255,255,255), (self.x-2, self.y-2, self.textWidth+4, self.textHeight+4))
        self.text = self.font.render(self.msg, 1, self.color)
        self.display.blit(self.text, (self.x, self.y))



class statusBar():
    def __init__(self, x, y, width, height, display, bgColour, topColour, outlineTF, outlineThickness=3):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.display = display
        self.bgColour = bgColour
        self.topColour = topColour
        self.outlineTF = outlineTF
        self.outlineThickness = outlineThickness

    def draw(self, statusPercentage):
        self.statusPercentage = statusPercentage
        if self.statusPercentage <= 0:
            self.statusPercentage = 0.001
        if self.outlineTF == True:
            pygame.draw.rect(self.display, self.bgColour, (self.x, self.y, self.width, self.height), self.outlineThickness)
            pygame.draw.rect(self.display, self.topColour, (self.x + self.outlineThickness, self.y + self.outlineThickness, (self.width * self.statusPercentage) - (self.outlineThickness * 2), self.height - (self.outlineThickness * 2)))
        else:
            pygame.draw.rect(self.display, self.topColour, (self.x, self.y, self.width * self.statusPercentage, self.height))
