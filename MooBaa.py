class MooBaa:
    def __init__(self):
        self.baamoo = 0

    def moo(self) -> str:
        self.baamoo -= 1
        return 'MOO!'

    def baa(self) -> str:
        self.baamoo += 1
        return 'BAA!'

    def getBaaMoo(self) -> int:
        return self.baamoo