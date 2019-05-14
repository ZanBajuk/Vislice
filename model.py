STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = "+" 
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'X'

class Igra:
    def __init__(self, geslo):
        self.geslo = geslo
        self.crke = []

    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]
    
    def pravilne_crke(self):
        pass

i = Igra("nekaj")
print(i.napacne_crke())
i.crke = ['a',"l","v","n"]
print(i.napacne_crke())
print(i.pravilne_crke())
print("test")