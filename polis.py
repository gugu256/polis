# POLIS MANAGER
from os import system as cmd

def clear():
    cmd("cls")

"""
ARMY
Bigger army = higher odds of winning wars and successful colonization
Can be changed by: training and recruiting in the army, hiring mercenaries, mobilizing all men

INFLUENCE
Bigger influence = more chances to get allies in wars, more chances to get potential trading partners,
more chances to attract métèques.
Can be changed by sending diplomats and founding colonies

TREASURY
Bigger treasury = uhhh self explanatory everything costs money lol.
Changing taxes, making your population work in mines to produce drachmae, establishing trade routes

HAPPINESS
More happiness = less chances of revolts
Can be changed (positevely) by : organizing games and theater contests, founding colonies (sad people go away),
lowering taxes, winning wars

TRADE PARTNERS
More of them = more trade = more money and influence
Can be changed by asking cities to trade with you (and indirectly founding colonies)

COLONY
Founding colonies increases your citizens' happiness, but requires money and giving part of your army
Increases infuence, happiness, and the number of trade partners

POPULATION
More of it = more chances at winning wars, more taxes coming in, 
"""

class Polis:
    def __init__(self, name, civ, army, metics):
        self.name = name
        self.civ = civ
        self.army = army
        self.metics = metics
        self.pop = self.civ + self.army + self.metics
        self.trade_partners = []
        self.treasury = 100
        self.happiness = 70
        self.colonies = []
        self.influence = 0
    
    def __str__(self):
        tp = ""
        for partner in self.trade_partners:
            tp += partner + " "
        cs = ""
        for colony in self.colonies:
            cs += colony + " "

        return f"""Current state of {self.name}
{"="*(len("Current state of ")+len(self.name))}
Total population: {self.pop}
Native civilians: {self.civ}
Army: {self.army}
Metics: {self.metics}
Treasury: {self.treasury}
Influence: {self.influence}
Colonies: {cs}
Trade partners: {tp}"""
    
polis = Polis(input("Name your city-state: "), 10, 10, 10)
print(polis)