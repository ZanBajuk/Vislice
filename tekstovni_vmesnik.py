import model #To deluje če je v isti mapi

def izpis_igre(igra):
    tekst = '''
    Število preostalih poskusov: {0}

    {1}

    Napačne črke ({2}): {3}
    '''.format(
        model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1,
        igra.pravilni_del_gesla(),
        igra.stevilo_napak(),
        igra.nepravilni_ugibi()
    )
    return tekst

def izpis_zmage(igra):
    tekst = '''
    ##### BRAVO! Uganil si geslo "{}". Mogoče kaj še bo iz tebe #####
    ##### Res super dosežek. Ko iščeš službo dej to v življenjepis. #####
    '''.format(
        igra.geslo
    )
    return tekst

def izpis_poraza(igra):
    tekst = '''
    ##### Jooooj! Porabil si vse poskuse. Geslo je "{}". #####
    #####  Blo je dost očitno, če sm pošten. ######
    ##### Probi bit ne slab drugič(za razliko od zdej)#####
    ##### ¯\_(ツ)_/¯ #####
    '''.format(igra.geslo)
    return tekst

def zahtevaj_vnos():
    return input("Vnesi črko: ")

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        print(izpis_igre(igra))
        crka = zahtevaj_vnos()
        if len(crka) != 1: # V primeru 'napačnega' inputa
            print("Ne me *****. Vem kje živiš. ಠ╭╮ಠ")
            continue
        rez = igra.ugibaj(crka)
        if rez == model.ZMAGA:
            print(izpis_zmage(igra))
            return
        if rez == model.PORAZ:
            print(izpis_poraza(igra))
            return
########

#print(izpis_igre(igra))
#print(izpis_zmage(igra))
#print(izpis_poraza(igra))

pozeni_vmesnik()