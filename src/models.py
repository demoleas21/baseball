class Player(object):

    def __init__(self, name, pageId):
        self.name = name
        self.pageId = pageId
        self.stats = None

    def setStats(self, data):
        self.stats = data
