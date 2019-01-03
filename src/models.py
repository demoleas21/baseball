class Player(object):

    def __init__(self, name, pageId):
        self.name = name
        self.pageId = pageId
        self.regularSeasonFall2018 = None

    def setStats(self, category, data):
        setattr(self, category, data)
