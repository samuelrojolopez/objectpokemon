from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(51)
        self.spend_attack(49)
        self.spend_defence(0)
        self.add_move(CosmoMemory())
        self.add_move(EarthRave())
        self.add_move(HowlingMoon())
        self.add_move(BloodFang())
        self.move = 0
        self.moves = ["Cosmo Memory","Earth Rave","Howling Moon","Blood Fang"]
        self.set_type(Type.NORMAL)

    def get_name(self):
        return "Red XIII"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)

class CosmoMemory(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)

    def get_name(self):
        return "Cosmo Memory"

class EarthRave(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)

    def get_name(self):
        return "Earth Rave"


class HowlingMoon(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)

    def get_name(self):
        return "Howling Moon"


class BloodFang(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)

    def get_name(self):
        return "Blood Fang"

