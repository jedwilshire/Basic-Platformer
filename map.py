import pygame
from settings import *
class Level:
    def __init__(self):
        self.tiles = []
        with open('level1.txt') as f:
            for line in f:
                self.tiles.append(line.strip())
        self.width = len(self.tiles[0])
        self.height = len(self.tiles)
    
    def get_in_wall(self, x, y):
        

"""
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.type = 'dog'
    
    def speak(self):
        print('woof woof my name is ' + self.name)
"""       
    