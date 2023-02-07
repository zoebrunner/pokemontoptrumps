class Pokemon:

    id: str
    name: str
    height: float
    hp: float
    attack: float
    defense: float
    speed: float
    weight: float
    xp: float

    def __init__(
        self,
        id: str,
        name: str,
        height: float,
        hp: float,
        attack: float,
        defense: float,
        speed: float,
        weight: float,
        xp: float,
    ):

        self.id = id
        self.name = name
        self.height = height
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.weight = weight
        self.xp = xp

    def __eq__(self, other: 'Pokemon') -> bool:
        return self.id == other.id
