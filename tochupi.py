from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(10)
        self.spend_attack(40)
        self.spend_defence(50)
        self.add_move(Burbuja_venenosa())
        self.add_move(Tope_para_puerta())
        self.add_move(Devoradora_Koblenz())
        self.add_move(Encendeprende())
        self.move = 0
        self.moves = ['Burbuja_venenosa', "Tope_para_puerta", "Devoradora_Koblenz", "Encendeprende"]


    def get_name(self):
        return "Tochupi"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)

class Burbuja_venenosa(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(2)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Burbuja_venenosa"

class Tope_para_puerta(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(2)
        self.set_type(Type.NORMAL)

    def get_name(self):
        return "Tope_para_puerta"


class Devoradora_Koblenz(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(2)
        self.set_type(Type.EARTH)


    def get_name(self):
        return "Devoradora_Koblenz"


class Encendeprende(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(2)
        self.set_type(Type.FIRE)


    def get_name(self):
        return "Encendeprende"


