import random

# Definition des Klasse Spiel
global score
score = 0
global turn
turn = 0

print()

class Spiel:
    def __init__(self):
        random.seed()
        self.points = 0

    
    def spielen(self):
        weiterspielen = True
        while weiterspielen:
            for i in range(1,6):
                task = Aufgabe()
                task.beantworten()
            
            if "n" == input("Möchtest du weiterspielen? - n für nein, beliebige Eingabe um weiter zumachen: "):
                weiterspielen = False
                print("Du hast dich entschieden aufzuhören!")
            
            
        
        


class Aufgabe:
    def __init__(self):
        global turn
        global score
        turn += 1

        self.difficulty = round(score / turn) + 1
        self.reward = 3 * self.difficulty

        self.a = random.randint(1,(10*self.difficulty))

        self.b = random.randint(1,(10*self.difficulty))

        if self.difficulty < 5:
            self.ergebnis = self.a + self.b
            self.aufgabe = f"Aufgabe {turn}: {self.a:3d}  + {self.b:3d}  = ? "
        else:
            self.ergebnis = self.a - self.b
            self.aufgabe = f"Aufgabe {turn}: {self.a:3d}  - {self.b:3d}  = ? "

    def beantworten(self):
        global score
        
        versuch = 1
        while versuch <= 3:
            

            try:
                self.antwort = int(input(self.aufgabe))

                if self.antwort == self.ergebnis:
                    score += self.reward
                    print(f"Dein {versuch}. Versuch war richtig! + {self.reward} Punkte!")
                    break
                else:
                    raise
            except:
                print(f'Deine Antwort ist leider falsch! Das war dein {versuch}. Versuch!')
                self.reward -= round(self.reward/3) # needs to be reviewed in future
                versuch += 1
                
        print()
        print("Dein momentaner Punktestand:", score)
        print("Schwierigkeit:", self.difficulty)
        print()
            
        

s = Spiel()
s.spielen()
print()
print("Dein entgültiger Punktestand:", score)
print()