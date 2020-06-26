#die：骰子
from random import randint

class Die():
    def __init__(self,num_sides=6 ):
        '''骰子默认为6面'''
        self.num_sides=num_sides

    def roll(self):
        '''返回一个随机的骰子面'''
        return randint(1,self.num_sides)