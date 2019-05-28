import bottle
import model

DATOTEKA_STANJA = 'stanje.json'
DATOTEKA_Z_BESEDAMI = 'besede.txt'

vislice = model.Vislice(DATOTEKA_STANJA, DATOTEKA_Z_BESEDAMI)

@bottle.get('/')
def index():
    return bottle.template('index.tpl')

@bottle.get('/img/<ime>')
def vrni_slike(ime):
    return bottle.static_file(ime, root="img")

#@bottle.get('/igra/')
#def nova_igra():
#    id = vislice.nova_igra()
#    bottle.redirect('/igra/{0}/'.format(id))

@bottle.post('/nova_igra/')
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie('id_igre', str(id_igre), path = '/')
    bottle.redirect('/igra/')

@bottle.get('/igra/')
def prikazi_igro():
    id_igre = int(bottle.request.get_cookie('id_igre'))
    igra, poskus = vislice.igre[id_igre]
    return bottle.template('igra.html', id_igre=id_igre, igra=igra, poskus=poskus)

#@bottle.get('/igra/<id:int>/')
#def pokazi_igro(id):
#    igra, poskus = vislice.igre[id]
#    return bottle.template('igra.html', id_igre=id, igra=igra, poskus=poskus)
    

@bottle.post('/igra/')
def ugibaj():
    id_igre = int(bottle.request.get_cookie('id_igre'))
    crka = bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/')

#@bottle.get('/igra/')
#def igratest():
#    return bottle.template('igra.', id_igre=id, igra=igra, poskus=poskus)

bottle.run(reloader=True, debug=True)