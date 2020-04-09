from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(10)
        self.spend_attack(0)
        self.spend_defence(90)
        self.add_move(Burn())
        self.add_move(Waterfall())
        self.add_move(RockSlide())
        self.add_move(Kick())
        self.set_type(Type.NORMAL)
        self.move = 0
        self.moves = ["Burn", "Waterfall", "Rock Slide", "Kick"]

    def get_name(self):
        return "Bulbasaur"

    def choose_move(self, enemy):
        if enemy.type == enemy.type.WATER:
           self.move = self.moves[0]
        elif enemy.type == enemy.type.FIRE:
           self.move = self.moves[1]
        elif enemy.type == enemy.type.EARTH:
            self.move = self.moves[2]  
        elif enemy.type == enemy.type.NORMAL:
           self.move = self.moves[3]
        else:
            self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0

        mov = self.move
        return self.get_move_by_name(mov)

class Burn(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(5)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Burn"

class Waterfall(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(5)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Waterfall"

class RockSlide(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(5)
        self.set_type(Type.EARTH)

    def get_name(self):
        return "Rock Slide"

class Kick(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(5)
        self.set_type(Type.NORMAL)

    def get_name(self):
        return "Kick"

