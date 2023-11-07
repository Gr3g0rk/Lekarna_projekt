import sqlite3
import tabele_in_podatki # Uvozimo tabele in podatke
# SAMO V TEM FILU SE LAHKO POGOVARJAS DIREKTNO Z BAZO, DRUGE SAMO PREKO model.py fila

conn = sqlite3.connect("lekarna.db")
tabele_in_podatki.pripravi_vse(conn)

class Zdravila:
    def __init__(self, sifra=None, ime=None, pakiranje=None, imetnik=None, cena=None):
        self.sifra = sifra
        self.ime = ime
        self.pakiranje = pakiranje
        self.imetnik = imetnik
        self.cena = cena
    
    @staticmethod
    def dobi_vsa_zdravila():
        '''Pridobimo vse podatke o zdravilih iz baze.
           Metoda vrne objekt tipa generator'''
        sql = '''
        SELECT * FROM zdravilo;
        '''
        poizvedbe = conn.execute(sql).fetchall() # fetchall zdruzi in vrne seznam naborov zdravil.
        for poizvedba in poizvedbe:
            yield poizvedba

    @staticmethod
    def dobi_zdravilo(ime):
        '''Poiscemo podatke o zdravilu glede na njegovo ime.
           Metoda vrne tabelo naboro.'''
        sql = '''SELECT *
             FROM zdravilo
             WHERE ime LIKE ?'''
        return conn.execute(sql, ['%' + ime + '%']).fetchall()


class Pacient:
    def __init__(self, zzzs=None, ime=None, priimek=None, datumRojstva=None, zdravnik_id=None):
        self.zzzs = zzzs
        self.ime = ime
        self.priimek = priimek
        self.datumRojstva = datumRojstva
        self.zdravnik_id = zdravnik_id
    
    @staticmethod
    def dobi_pacienta(st):
        '''Metoda vrne vse podatke o pacientu glede na njegovo zzzs.'''
        sql = '''SELECT *
             FROM pacient
             WHERE zzzs = ?'''
        return conn.execute(sql, [st]).fetchall()
        

    @staticmethod
    def zdravila_napotnica(st):
        '''Metoda pridobi podatek o imenu zdravila za pacienta'''
        sql = '''SELECT ime
                FROM zdravilo
                WHERE nacionalnaSifra IN (
                        SELECT zdravilo_nacionalnaSifra
                            FROM recept
                            WHERE pacient_zzzs = ?
                )'''
        return conn.execute(sql, [st]).fetchall()
    
    @staticmethod
    def dodaj(ime, priimek, rojstvo, zdr_id):
        '''Dodajanje podatkov o novem pacientu v bazo.'''
        db = sqlite3.connect('lekarna.db') #Povežemo se z bazo.
        with db as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO pacient (ime, priimek, datumRojstva, zdravnik_id) 
                              VALUES (?, ?, ?, ?)''', (ime,priimek,rojstvo, zdr_id)) # Izvedemo poizvedbo vstavljanja.
    @staticmethod
    def napotnica_neobnovljiva(st):
        '''Pridobimo podatke o neobnovljivih zdravilih za pacienta.'''
        sql = '''SELECT zdravilo.ime, recept.obnovljiva
                FROM recept
                JOIN zdravilo ON recept.zdravilo_nacionalnaSifra = zdravilo.nacionalnaSifra
                WHERE recept.obnovljiva = 0 AND recept.pacient_zzzs = ?
                '''
        return conn.execute(sql, [st]).fetchall()
    
    @staticmethod
    def napotnica_obnovljiva(st):
        '''Pridobimo podatke o obnovljivih zdravilih za pacienta.'''
        sql = '''SELECT zdravilo.ime, recept.obnovljiva, recept.pogostost
                FROM recept
                JOIN zdravilo ON recept.zdravilo_nacionalnaSifra = zdravilo.nacionalnaSifra
                WHERE recept.obnovljiva = 1 AND recept.pacient_zzzs = ?
                '''
        return conn.execute(sql, [st]).fetchall()

class Zdravnik:
    def __init__(self, id=None, ime=None, priimek=None):
        self.id = id
        self.ime = ime
        self.priimek = priimek
  
    @staticmethod
    def pacienti(st):
        '''Pridobivanje podatkov pacientov zdravnika.'''
        sql = '''SELECT zzzs,
                        ime,
                        priimek,
                        datumRojstva
                FROM pacient
                WHERE pacient.zdravnik_id = ?;
                '''
        return conn.execute(sql, [st]).fetchall()

    @staticmethod
    def imePriimek(st):
        '''Pridobivanje imena in priimka zdravnika glede na njegov id'''
        sql = '''SELECT ime,
                        priimek
                FROM zdravnik
                WHERE id = ?
                '''
        return conn.execute(sql, [st]).fetchall()

class Recept:
    def __init__(self, id=None, obnovljiva=None, zdravilo_nacionalnaSifra=None, pacient_zzzs=None, zdravnik_id=None):
        self.id = id
        self.obnovlja = obnovljiva
        self.zdravilo_nacionalnaSifra = zdravilo_nacionalnaSifra
        self.pacient_zzzs = pacient_zzzs
        self.zdravnik_id = zdravnik_id
    
    @staticmethod
    def poslji(obn, zdr, pac, zdra, pog):
        '''Vnašanje podatkov recepta v bazo'''
        db = sqlite3.connect('lekarna.db') #Povežemo se z bazo.
        with db as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO recept (obnovljiva, zdravilo_nacionalnaSifra, pacient_zzzs, zdravnik_id, pogostost)
                              VALUES (?, ?, ?, ?, ?)''', (obn, zdr, pac, zdra, pog))