class Unit:

    __name=None
    __hp=None
    __currentHp=None
    __minDamage=None
    __maxDamage=None
    __defence=None
    __type=None

    def __init__(self, name, hp, currentHp, minDamage, maxDamage, defence, type):
        self.__name = name
        self.__hp = hp
        self.__currentHp = currentHp
        self.__minDamage = minDamage
        self.__maxDamage = maxDamage
        self.__defence = defence
        self.__type = type

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


    def get_type(self):
        return self.__type


    def set_name(self, value):
        self.__name = value


    def set_hp(self, value):
        self.__hp = value


    def set_current_hp(self, value):
        self.__currentHp = value


    def set_min_damage(self, value):
        self.__minDamage = value


    def set_max_damage(self, value):
        self.__maxDamage = value


    def set_defence(self, value):
        self.__defence = value


    def set_type(self, value):
        self.__type = value

    name = property(get_name, set_name, None, None)
    hp = property(get_hp, set_hp, None, None)
    currentHp = property(get_current_hp, set_current_hp, None, None)
    minDamage = property(get_min_damage, set_min_damage, None, None)
    maxDamage = property(get_max_damage, set_max_damage, None, None)
    defence = property(get_defence, set_defence, None, None)
    type = property(get_type, set_type, None, None)

    