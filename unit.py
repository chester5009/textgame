class Unit:

    name=None
    hp=None
    currentHp=None
    minDamage=None
    maxDamage=None
    defence=None

    def __init__(self, name, hp, currentHp, minDamage, maxDamage, defence):
        self.name = name
        self.hp = hp
        self.currentHp = currentHp
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.defence = defence

    def get_name(self):
        return self.__name


    def get_hp(self):
        return self.__hp


    def get_current_hp(self):
        return self.__currentHp


    def get_min_damage(self):
        return self.__minDamage


    def get_max_damage(self):
        return self.__maxDamage


    def get_defence(self):
        return self.__defence


    def set_name(self, value):
        self.__name = value


    def set_hp(self, value):
        self.__hp = value


    def set_current_hp(self, value):
        self.__currentHp = value

    name = property(get_name, set_name, None, None)
    hp = property(get_hp, set_hp, None, None)
    currentHp = property(get_current_hp, set_current_hp, None, None)
    minDamage = property(get_min_damage, None, None, None)
    maxDamage = property(get_max_damage, None, None, None)
    defence = property(get_defence, None, None, None)