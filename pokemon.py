# pokemon.py
import random
class Pokemon:
    def __init__(self, name, hp, atk, speed, accuracy):
        self._name = name
        self._hp = hp
        self._max_hp = hp * 2
        self._atk = atk
        self._speed=speed
        self._accuracy=accuracy

    def attack(self, target):
        target.hp -= self._atk
        print(f'{self._name}のこうげき！', end='')
        self.attack_message(target)
        
        
    

    def attack_message(self, target):
        pass

    def is_fainted(self):
        return self._hp <= 0

    @property
    def hp(self):
        return self._hp
    
    @property
    def atk(self):
        return self._atk
    
    @property
    def speed(self):
        return self._speed

    @hp.setter
    def hp(self, value):
        if value < 0:
            self._hp = 0
        elif value > self._max_hp:
            self._hp = self._max_hp
        else:
            self._hp = value

    @property
    def name(self):
        return self._name
    
    
#pokemon_skill_data

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__('ピカチュウ',
                        random.randint(10,100),
                        random.randint(10,50),
                        random.randint(10,150),
                        (90))

    def attack_message(self, target):
        print(f'10万ボルト！{target.name}は{self._atk}ダメージをもらった。{target.name}のHPは{target.hp}だ。')
        
class Zenigame(Pokemon):
    def __init__(self):
        super().__init__('ゼニガメ',
                        random.randint(10,130),
                        random.randint(30,70),
                        random.randint(10,120),
                        (60))

    def attack_message(self, target):
        print(f'水鉄砲！{target.name}は{self._atk}ダメージをもらった。{target.name}のHPは{target.hp}だ。')

class Hitokage(Pokemon):
    def __init__(self):
        super().__init__('ヒトカゲ', 
                        random.randint(10,160),
                        random.randint(50,120),
                        random.randint(10,100),
                        (30))

    def attack_message(self, target):
        print(f'ひのこ！{target.name}は{self._atk}ダメージをもらった。{target.name}のHPは{target.hp}だ。')



