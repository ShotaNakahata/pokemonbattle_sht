import random

class Game:
    def __init__(self, pokemon1, pokemon2,):
        self._pokemon1 = pokemon1
        self._pokemon2 = pokemon2
        

    def battle(self):
        self._start()
        winner, loser = self._attack()
        self._show_result(winner, loser)

    def _start(self):
        
        print(f'{self._pokemon1.name}があらわれた。{self._pokemon1.name}の能力は\nHPは{self._pokemon1.hp},atkは{self._pokemon1.atk}、Speedは{self._pokemon1.speed}だ')
        print(f'{self._pokemon2.name}があらわれた。{self._pokemon2.name}の能力は\nHPは{self._pokemon2.hp},atkは{self._pokemon2.atk}、Speedは{self._pokemon2.speed}だ')

    def _attack(self):
        # Speedを比較して、先に攻撃するポケモンを決定
        if self._pokemon1.speed > self._pokemon2.speed:
            first_attacker, second_attacker = self._pokemon1, self._pokemon2
            print(f"{first_attacker._name}が先行")
        elif self._pokemon1.speed < self._pokemon2.speed:
            first_attacker, second_attacker = self._pokemon2, self._pokemon1
            print(f"{first_attacker._name}が先行")
        else:
            # Speedが同じ場合はランダムに決定
            first_attacker, second_attacker = random.choice([(self._pokemon1, self._pokemon2), (self._pokemon2, self._pokemon1)])
            print(f'Speedが同じため、ランダムに{first_attacker.name}が先攻する！')

        while True:
            first_attacker.attack(second_attacker)
            if second_attacker.is_fainted():
                return (first_attacker, second_attacker)

            second_attacker.attack(first_attacker)
            if first_attacker.is_fainted():
                return (second_attacker, first_attacker)

    def _show_result(self, winner, loser):
        print(f'{loser.name}はたおれた。{winner.name}のかち！')
