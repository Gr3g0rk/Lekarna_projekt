import bottle
import model

glavni_model = model.Zdravila()
pacient = model.Pacient()
zdravnik = model.Zdravnik()
recept = model.Recept()

@bottle.route("/static/css/<filename>")
def serve_static_files_css(filename):
    return bottle.static_file(filename, root='./static/css/')

#Glavna (zacetna) stran
@bottle.get("/")
def glavna_stran():
    podatki = glavni_model.dobi_vsa_zdravila()
    return bottle.template("glavna.html", zdravila = podatki)

#Stran za izpisovanje podatkov o pacientu.
@bottle.get("/isci/") 
def iskanje1():
    iskalni_niz = bottle.request.query['iskalni_niz']
    oseba = pacient.dobi_pacienta(int(iskalni_niz))
    zdravila_obno = pacient.napotnica_obnovljiva(int(iskalni_niz))
    zdravila_ne = pacient.napotnica_neobnovljiva(int(iskalni_niz))
    return bottle.template("zzzs.html",iskalni_niz = iskalni_niz ,oseba = oseba, zdravila_obno = zdravila_obno, zdravila_ne = zdravila_ne)

#Stran za izpisovanje zdravil.
@bottle.get("/zdravilo/") 
def iskanje2():
    iskalni_niz = bottle.request.query['zdr']
    zdravilo = glavni_model.dobi_zdravilo(iskalni_niz)
    return bottle.template("zdravilo.html",iskalni_niz = iskalni_niz , zdravilo = zdravilo)

#Stran za zdravnike.
@bottle.get("/zdravnik/")
def iskanje3():
    iskalni_niz = bottle.request.query['zdravnikId']
    osebe = zdravnik.pacienti(int(iskalni_niz))
    ime_priimek = zdravnik.imePriimek(int(iskalni_niz))
    return bottle.template("zdravnik.html", iskalni_niz = iskalni_niz , osebe = osebe, ime_priimek = ime_priimek)

# Stran za dodajanje pacienta
@bottle.get("/obrazec/")
def dodaj():
    obnovljiva = bottle.request.query['obnovljiva'] # Pridobimo podatke iz obrazca.
    zdravilo = bottle.request.query['zdravilo']
    pogostost = bottle.request.query['pogosto']
    zzzs = bottle.request.query['zzzs']
    zdravnikid = bottle.request.query['id']
    recept.poslji(obnovljiva, zdravilo, zzzs, zdravnikid, pogostost) # Poklicemo metodo poslji ki nam vstavi podatke v tabelo.
    bottle.redirect("/") # Preusmeri nas na zacetno stran.

@bottle.get("/dodaj_pacienta/")
def dodaj_pacienta():
    return bottle.template("dodaj_pacienta.html")

@bottle.post("/dodaj_pacienta/") # Stran za zdravnike.
def dodaj_pacienta():
    ime = bottle.request.forms.get('ime') # Pridobimo podatke iz obrazca.
    priimek = bottle.request.forms.get('priimek')
    datum = bottle.request.forms.get('rojstvo')
    zdravnikid = bottle.request.forms.get('id')
    pacient.dodaj(ime, priimek, datum, zdravnikid)
    bottle.redirect("/") # Preusmeri nas na zacetno stran.

bottle.run(host='localhost', port=8080 , debug=True, reloader=True)