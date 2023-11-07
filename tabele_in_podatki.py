import sqlite3 
import csv 
from zdravila import pridobi

db = sqlite3.connect('lekarna.db')
def ustvari_tabele():
    '''Ustvarimo tabele zdravil, pacientov, zdravnikov, receptov'''
    with db as cursor: #automatsko zapre kurzor
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS zdravilo
        (
            nacionalnaSifra INTEGER PRIMARY KEY,
            ime VARCHAR(200),
            cena DECIMAL(10, 2),
            imetnikDovoljenja VARCHAR(200)
        );
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pacient
        (
            zzzs INTEGER PRIMARY KEY AUTOINCREMENT,
            ime VARCHAR(200),
            priimek VARCHAR(200),
            datumRojstva DATE,
            zdravnik_id INTEGER,
            FOREIGN KEY(zdravnik REFERENCES zdravnik(id)
        );
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS zdravnik
        (
            id INTEGER PRIMARY KEY,
            ime VARCHAR(200),
            priimek VARCHAR(200)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS recept
        (
            id INTEGER PRIMARY KEY AUTOINCREMET,
            obnovljiva TINYINT(1),
            zdravilo_nacionalnaSifra INTEGER,
            pacient_zzzs INTEGER,
            zdravnik_id INTEGER,
            pogostost VARCHAR(200),
            FOREIGN KEY(zdravilo_nacionalnaSifra) REFERENCES zdravilo(nacionalnaSifra),
            FOREIGN KEY(pacient_zzzs) REFERENCES pacient(zzzs),
            FOREIGN KEY(zdravnik) REFERENCES zdravnik(id)
        );
        """)

def dodaj_v_tabele():
    '''Napolni tabelo 'zdravila' s podatki.'''
    with db as conn:
        cursor = conn.cursor()
        for zdravilo in pridobi():
            cursor.execute('''INSERT OR IGNORE INTO zdravilo (nacionalnaSifra, ime, cena, imetnikDovoljenja)
                                VALUES (?,?,?,?)''', (zdravilo[0], zdravilo[1], zdravilo[2], zdravilo[3]))
        
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (1, 'Raimondo', 'Eustis')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (2, 'Cecilio', 'Cook')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (3, 'Shelli', 'Sobieski')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (4, 'Ash', 'Hundell')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (5, 'Thomasine', 'Renison')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (6, 'Wilmar', 'Le Franc')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (7, 'Woodrow', 'Donhardt')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (8, 'Celine', 'Veschi')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (9, 'Robinett', 'Veschambre')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (10, 'Konstantin', 'Davidovitz')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (11, 'Hartwell', 'Volant')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (12, 'Milo', 'Wilhelmy')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (13, 'Wilhelmine', 'Lyddiatt')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (14, 'Jesse', 'McAdam')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (15, 'Jaquelin', 'Creavin')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (16, 'Ernestine', 'McKeaveney')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (17, 'Kellia', 'Dionisii')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (18, 'Bernardina', 'McKennan')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (19, 'Etty', 'Marcham')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (20, 'Rutger', 'Ramel')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (21, 'Guthrey', 'Crimin')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (22, 'Merwyn', 'Harbage')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (23, 'Sela', 'Beining')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (24, 'Jaime', 'Powley')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (25, 'Vincent', 'Purcell')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (26, 'Cyrille', 'Cahalin')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (27, 'Traci', 'Calan')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (28, 'Cristy', 'Coyle')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (29, 'Wade', 'Lugsdin')''')
        cursor.execute('''insert into zdravnik (id, ime, priimek) values (30, 'Nero', 'Carlino')''')

        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (1, 'Becka', 'Pratt', '8/8/1939', 5)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (2, 'Mozelle', 'Spurling', '3/14/1959', 12)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (3, 'Izaak', 'Pepperd', '10/22/1971', 25)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (4, 'Alysa', 'Welland', '3/15/1980', 2)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (5, 'Christian', 'Batchelar', '1/7/2023', 3)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (6, 'Justino', 'Dennehy', '5/20/1949', 19)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (7, 'Garth', 'Hansbury', '4/8/1998', 5)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (8, 'Avram', 'Streather', '8/13/1948', 7)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (9, 'Cheryl', 'Chatelain', '7/17/1961', 29)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (10, 'Gareth', 'Nisen', '6/16/1937', 10)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (11, 'Noam', 'Boullin', '7/12/1938', 11)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (12, 'Meredith', 'Slight', '12/9/1990', 22)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (13, 'Kathryn', 'Kemish', '4/8/1987', 25)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (14, 'Erastus', 'Farnsworth', '10/2/1942', 12)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (15, 'Trula', 'Shearstone', '10/12/1986', 14)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (16, 'Phyllis', 'Guerreau', '4/16/2012', 6)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (17, 'Gawain', 'Bareford', '6/10/2010', 9)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (18, 'Clive', 'Gregoli', '5/11/2009', 8)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (19, 'Ettore', 'Pitkin', '3/3/1970', 1)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (20, 'Arly', 'Kighly', '1/20/1995', 4)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (21, 'Duane', 'Kirwan', '10/30/2012', 13)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (22, 'Claire', 'Ivushkin', '2/10/1963', 17)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (23, 'Briano', 'Erdes', '11/10/1954', 18)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (24, 'Blondy', 'Scholtis', '11/29/1939', 13)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (25, 'Britney', 'Colquite', '10/13/1970', 9)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (26, 'Brockie', 'Parsell', '5/4/1995', 20)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (27, 'Birgit', 'Simms', '1/6/1980', 7)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (28, 'Gage', 'McVie', '1/13/1959', 17)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (29, 'Nelie', 'Armin', '1/25/1978', 24)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (30, 'Stern', 'Vivash', '4/10/1948', 15)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (31, 'Miles', 'Ashbee', '1/12/1992', 15)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (32, 'Willy', 'Pecht', '6/26/1994', 16)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (33, 'Smitty', 'Coddington', '8/8/2022', 18)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (34, 'Nick', 'Nobles', '4/10/2001', 19)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (35, 'Zenia', 'Maryon', '9/28/1951', 19)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (36, 'Emilie', 'Jirzik', '11/22/2009', 6)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (37, 'Say', 'Wallen', '9/11/1952', 20)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (38, 'Ron', 'Scanterbury', '5/23/2015', 3)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (39, 'Aurore', 'Whyke', '5/17/1961', 11)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (40, 'Elisabet', 'Malone', '7/1/2020', 10)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (41, 'Klara', 'Gerardi', '8/12/2005', 21)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (42, 'Isidora', 'Champagne', '5/10/1992', 23)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (43, 'Dotti', 'Proudler', '1/6/1938', 25)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (44, 'Nathanil', 'Jacqueme', '11/21/1993', 16)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (45, 'Almire', 'Pond', '8/22/1951', 10)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (46, 'Lorilee', 'Danev', '10/8/1973', 2)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (47, 'Theadora', 'Crampsey', '7/19/1981', 1)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (48, 'Lynnelle', 'Belloch', '2/3/1980', 1)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (49, 'Ann-marie', 'Emerine', '8/20/1974', 26)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (50, 'Sande', 'Mathwen', '3/4/2013', 26)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (51, 'Brian', 'Treske', '10/21/2011', 27)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (52, 'Eyde', 'Zwicker', '8/24/1958', 22)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (53, 'Cassius', 'Ducker', '2/18/1981', 9)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (54, 'Garvy', 'De Mattia', '9/15/1974', 5)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (55, 'Selia', 'McGrady', '4/29/2007', 28)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (56, 'Bernadene', 'Wethered', '8/28/1949', 14)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (57, 'Cairistiona', 'Paice', '9/22/1960', 13)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (58, 'Luciana', 'Tippetts', '7/12/2014', 12)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (59, 'Prudy', 'Redmore', '12/12/1968', 28)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (60, 'Svend', 'Bordman', '1/3/2013', 29)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (61, 'Haroun', 'Benns', '6/30/1971', 30)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (62, 'Ezmeralda', 'Robinson', '11/1/1963', 30)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (63, 'Jamil', 'Dreakin', '10/12/1935', 4)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (64, 'Jackqueline', 'Causer', '8/8/1948', 19)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (65, 'Rustin', 'McVee', '9/4/2008', 28)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (66, 'Mercy', 'Vogt', '5/16/1960', 15)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (67, 'Darelle', 'Barthropp', '5/3/1981', 5)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (68, 'Denna', 'West', '4/27/2004', 25)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (69, 'Marion', 'Crocombe', '3/31/1933', 23)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (70, 'Rodolphe', 'Murtell', '10/6/1966', 8)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (71, 'Rem', 'Coundley', '12/26/1987', 29)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (72, 'Daryn', 'Daniells', '5/13/1973', 30)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (73, 'Cirstoforo', 'Barber', '3/5/1978', 27)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (74, 'Leupold', 'Stearn', '3/7/1988', 27)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (75, 'Gretchen', 'Wrought', '5/3/1955', 11)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (76, 'Vi', 'Braunlein', '3/24/1988', 22)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (77, 'Robinson', 'Furmagier', '12/12/1992', 4)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (78, 'Ogdan', 'Piletic', '5/7/1954', 4)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (79, 'Quinlan', 'Spoors', '6/15/2003', 24)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (80, 'Benedicta', 'Littlejohns', '2/17/1949', 26)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (81, 'Elizabeth', 'Dorrington', '1/20/1998', 28)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (82, 'Keelia', 'Whapham', '10/23/2018', 18)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (83, 'Alister', 'Dyhouse', '8/31/1950', 10)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (84, 'Brandy', 'Vickerstaff', '2/3/2016', 20)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (85, 'Barbabas', 'Shewan', '7/24/1975', 20)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (86, 'Andris', 'Pooley', '5/7/2014', 6)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (87, 'Cristina', 'Moral', '3/24/2017', 1)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (88, 'Garvey', 'Lerner', '9/21/1979', 2)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (89, 'Alexandros', 'Aspray', '4/10/1950', 3)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (90, 'Gaylord', 'Bensusan', '2/12/2000', 5)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (91, 'Pete', 'Lofting', '3/4/1999', 19)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (92, 'Norton', 'Bonnar', '3/4/1949', 14)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (93, 'Herold', 'Evett', '1/18/1987', 30)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (94, 'Jacky', 'Angless', '9/21/1953', 21)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (95, 'Lovell', 'Housego', '4/28/1980', 10)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (96, 'Chad', 'Boldecke', '2/22/1960', 10)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (97, 'Bridget', 'Emmot', '1/27/1939', 22)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (98, 'Forbes', 'Daulby', '5/23/1947', 11)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (99, 'Tyne', 'Redsull', '4/21/1959', 7)''')
        cursor.execute('''insert into pacient (zzzs, ime, priimek, datumRojstva, zdravnik_id) values (100, 'Lucinda', 'Ibel', '1/23/1980', 17)''')

def pripravi_vse(conn):
    pass

if __name__ == '__main__':
    # S klicem funkcij ustvari_tabele ter dodaj_v_tabele ustvarimo tabele z bazo ter jih napolnimo s ustreznimi podatki.
    #ustvari_tabele()
    #dodaj_v_tabele()
    pass