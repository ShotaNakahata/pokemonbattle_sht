# oop_pokemon.py
import random
from game import Game
from pokemon import Pikachu, Hitokage,Zenigame

# ポケモンのインスタンスを作成
pikachu = Pikachu()
hitokage = Hitokage()
zenigame = Zenigame()

# ポケモンのインスタンスのリストを作成
pokemon_list = [pikachu, hitokage, zenigame]

# random.sampleを使用してリストからランダムに2つのユニークなポケモンを選択
selected_pokemon = random.sample(pokemon_list, 2)

# 選ばれたポケモンでゲームを始める
game = Game(selected_pokemon[0], selected_pokemon[1])
game.battle()