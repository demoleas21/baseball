class Player(object):

    def __init__(self, name, pageId):
        self.name = name
        self.pageId = pageId
        self.gameLog = {}

    def setStats(self, category, data):
        setattr(self, category, data)
