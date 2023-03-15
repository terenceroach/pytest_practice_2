class Track():
    def __init__(self, title, artisit):
        self.title = title
        self.artist = artisit

    def matches(self, keyword):
        return keyword in self.title or keyword in self.artist