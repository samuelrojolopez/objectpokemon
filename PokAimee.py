from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(10)
        self.spend_attack(30)
        self.spend_defence(60)
        self.add_move(Sing())
        self.add_move(Punch())
        self.add_move(Hypnotize())
        self.add_move(invisible())
        self.move = 0
        self.moves = ['Lalala', "Punch ****", "Hypnotizeee @u@", " //invisible//"]


    def get_name(self):
        return "Jigglypuff"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)

class Punch(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(2)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Punch ****"

class Hypnotize(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Hypnotizeee @u@"


class invisible(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.EARTH)

    def get_name(self):
        return "//invisible//"


class Sing(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Lalala"
