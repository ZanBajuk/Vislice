import random
import json

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = "+" 
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'X'
ZACETEK = 'B'

bazen_besed = []
with open("besede.txt", encoding = "utf-8") as f:
    bazen_besed = [beseda.strip() for beseda in f.readlines()]

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo.upper()
        if crke is None:
            self.crke = []
        else:
            self.crke = crke

    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]
    
    def pravilne_crke(self):
        return [c for c in self.crke if c in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return all(c in self.crke for c in self.geslo)

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        niz = ""
        for i in self.geslo:
            if i in self.crke:
                niz += i
            else:
                niz += "_"
            niz += " "
        return niz

    def nepravilni_ugibi(self):
        sez = self.napacne_crke()
        if sez == []:
            return ""
        niz = sez[0]

        for i in sez[1:]:
            niz += " "
            niz += i
        return niz

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)
        if crka in self.geslo:
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA

def nova_igra():
    return Igra(random.choice(bazen_besed))

class Vislice:

    def __init__(self, datoteka_s_stanjem, datoteka_s_besedami):
        self.igre = {}
        self.datoteka_s_stanjem = datoteka_s_stanjem
        self.datoteka_s_besedami = datoteka_s_besedami
        with open(self.datoteka_s_besedami, encoding = "utf-8") as f:
            self.bazen_besed = [beseda.strip().upper() for beseda in f.readlines()]
        self.nalozi_igre_iz_datoteke()

    def prost_id_igre(self):
        return len(self.igre)

    def nova_igra(self):
        id = self.prost_id_igre()
        self.igre[id] = (Igra(random.choice(self.bazen_besed)), ZACETEK)
        return id

    def ugibaj(self, id_igre, crka):
        igra, _ = self.igre[id_igre]
        poskus = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, poskus)
        self.zapisi_igre_v_datoteko()

    def zapisi_igre_v_datoteko(self):
        with open(self.datoteka_s_stanjem, 'w') as f:
            igre = {str(id_igre): {'poskus' : poskus, 'geslo' : igra.geslo, 'crke' : igra.crke} for id_igre, (igra, poskus) in self.igre.items()}
            json.dump(igre, f)

    def nalozi_igre_iz_datoteke(self):
        with open (self.datoteka_s_stanjem) as f:
            igre = json.loads(f.read())
            self.igre = {}
            for id_igre, opis_igre in igre.items():
                self.igre[int(id_igre)] = (Igra(opis_igre['geslo'], crke=opis_igre['crke']), opis_igre['poskus'])

#####################
#v = Vislice()
#v.nova_igra()
#v.nova_igra()
#print(v.igre)


#i = Igra("NEKAJ")
#i.crke = ['N',"E","K","A","M","R"]

# print(i.napacne_crke())
# print(i.pravilne_crke())
#print(i.zmaga())
#print(i.ugibaj("N"))
#print(i.ugibaj("Đ"))
#print(i.ugibaj("J"))
# print(i.pravilni_del_gesla())
# print(i.nepravilni_ugibi())
