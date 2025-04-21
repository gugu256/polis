# POLIS MANAGER
import os
from random import randint as int_rnd

def do_nothing():
    pass

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    pass

def pe(msg=""):
    if msg=="":
        input("\nPress Enter to continue/")
    else:
        input(f"\nPress Enter {msg}/")

def load(t, l=10, task=""):
    clear()
    i = 0
    while i <=l:
        print(f"[{i*"■"}{(l-i)*" "}]")
        print(task)
        i+=1
        wait(t)
        clear()

def q():
    quit()

def is_int(s):
    return True if s in "0123456789" and s != "" else False

def choose(msg, passages, passages_name, clearscreen=False, passage_title=""):
    if clearscreen: 
        clear()

    if passage_title != "":
        print(passage_title)
        print("="*len(passage_title) + "\n")
    
    print(msg + "\n") if msg != "" else do_nothing()
    i = 1
    
    for passage in passages_name:
        print(f"{i} : {passage}")
        i += 1
    c = input("> ")

    lower_passages = []
    for passage in passages_name:
        lower_passages.append(passage.lower())
    
    if is_int(c) and int(c) >= 1 and int(c) < i:
        print()
        passages[int(c)-1]()
    elif c.lower() in lower_passages:
        passages[lower_passages.index(c.lower())]()
    elif c == "help":
        h()
        choose(msg, passages, passages_name, True, passage_title)
    elif c == "quit":
        q()
    else:
        choose(msg, passages, passages_name, clearscreen, passage_title)

"""
ARMY
Bigger army = higher odds of winning wars and successful colonization
Can be changed by: recruiting, hiring mercenaries, mobilizing all men

INFLUENCE
Bigger influence = more chances to get allies in wars, more chances to get potential trading partners,
more chances to attract metics.
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
        self.trade_partners = [] # trade allies
        self.treasury = 10000
        self.happiness = 70
        self.colonies = []
        self.allies = [] # military allies
        self.influence = 0
        self.tax = {
            "civ": 1,
            "met": 2,
            "arm": 0
        }
        self.army_pay = 3

    def __str__(self):
        tp = ""
        for partner in self.trade_partners:
            tp += partner + " "
        cs = ""
        for colony in self.colonies:
            cs += colony + " "
        al = ""
        for ally in self.allies:
            al += ally + " "  

        return f"""Current state of {self.name}
{"="*(len("Current state of ")+len(self.name))}
Total population: {self.pop}
Native civilians: {self.civ}
Army: {self.army}
Metics: {self.metics}
Treasury: {self.treasury} drachmae
Influence: {self.influence}
Colonies: {cs}
Allies: {al}
Trade partners: {tp}\n"""

    def revolt(self):
        print("This function has not been implemented yet.")

    def collect_taxes(self):
        print("Collecting taxes")
        self.treasury += (self.civ * self.tax["civ"])+(self.metics * self.tax["met"])+(self.army * self.tax["arm"])
        print(f"Collected {self.civ * self.tax['civ']} drachmae from taxes on native civilians")
        print(f'Collected {self.metics * self.tax["met"]} drachmae from taxes on metics')
        print(f'Collected {self.army * self.tax["arm"]} drachmae from taxes on soldiers\n')

    def pay_army(self):
        print(f"Paying the army: {self.army_pay} drachmae/soldier")
        if (self.treasury - self.army_pay * self.army) >= 0:
            self.treasury -= self.army_pay * self.army
            print(f"Paid {self.army_pay * self.army} drachmae to the soldiers")
        else:
            print(f"{self.name} does not have enough money in its treasury to pay its army!")
            if int_rnd(1, 2) == 1:
                self.revolt()
            else:
                print("The soldiers were understanding enough to not overthrow you,\nmake sure they are paid next time...")
        print("")        
    
polis = Polis(input("Name your city-state: "), 3000, 1000, 1000)
clear()

while True:
    clear()
    print(polis)
    polis.collect_taxes()
    polis.pay_army()
    pe()
