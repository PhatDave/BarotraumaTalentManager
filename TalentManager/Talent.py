class Talent:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return f'\t{self.name} {self.level}'
