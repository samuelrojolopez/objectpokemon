from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(15)
        self.spend_attack(25)
        self.spend_defence(60)
        self.add_move(Mordida())
        self.add_move(Escupitajo())
        self.set_type(Type.WATER)

    def get_name(self):
        return "Psyduck"

    def choose_move(self, enemy):
        return self.get_move_by_name("Mordida")

class Mordida(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(5)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Mordida"


class Escupitajo(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(5)
        self.set_type(Type.NORMAL)

    def get_name(self):
        return "Escupitajo"