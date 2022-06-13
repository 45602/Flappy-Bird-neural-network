class DataAdapter():
    def __init__(self) :
        self.groundScroll = 0
        self.scrollSpeed = 5
        self.screenWidth = 864
        self.screenHeight = 936
        self.fps = 60
        self.groundSize = (self.screenWidth, 150)
        self.groundHeight = self.screenHeight- self.groundSize[1]