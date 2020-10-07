import dataclasses, math, typing

@dataclasses.dataclass
class Vektor:
    x: float = 0.0
    y: typing.Any = 0.0

    def betrag(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
