import pickle
import os
import tkinter as tki
import tkinter.messagebox
import tkinter.scrolledtext as panel

'''Ak subor neexistuje tak sa na zaciatku vytvori. Ak existuje nijako sa nezmeni'''
file=open("C://Users//Admin//PycharmProjects//ZaverecnyProjekt//data.p", "a")
file.close()
'''Neskor pouzita ako globalna premenna v PRIDAJ kvoli chybnemu vstupu.'''
chyba=False

'''Definicia vlastneho objektu Instruktor.'''
class Instruktor(object):
    def __init__(self, idI="", meno="", priezvisko="", vzdelanie="", mail="", telefon="", adresa=""):
        self._idI = idI
        self.meno = meno
        self.priezvisko = priezvisko
        self._vzdelanie = vzdelanie
        self._mail = mail
        self._telefon = telefon
        self.adresa = adresa

    ''''Zakladne metody objektu'''
    def __repr__(self):
        return "Id:%s  Meno:%s  Priezvisko:%s  Vzdelanie:%s  Email:%s  Telefon:%s  Adresa:%s" \
            % (self._idI, self.meno, self.priezvisko, self._vzdelanie, self._mail, self._telefon, self.adresa)

    def __str__(self):
        return "Id:%s Meno:%s  Priezvisko:%s  Vzdelanie:%s  Email:%s  Telefon:%s  Adresa:%s" \
               % (self._idI, self.meno, self.priezvisko, self._vzdelanie, self._mail, self._telefon, self.adresa)

    '''Property vlastnosti. Odhaluju chyby pri potrebnych atributoch, ked pouzivatel chce pridat novy objekt'''
    @property
    def idI(self):
        return self._idI

    @idI.setter
    def idI(self, value):
        try:
            int(value)
            self._idI = value
        except  ValueError:
            tkinter.messagebox.showinfo('info', "Zadané ID je chybné")
            ukonc()

    @property
    def telefon(self):
        return self._telefon

    @telefon.setter
    def telefon(self, value):
        try:
            int(value)
            self._telefon = value
        except  ValueError:
            tkinter.messagebox.showinfo('info', "Zadaný telefón je chybný")

    @property
    def vzdelanie(self):
        return self._vzdelanie

    @vzdelanie.setter
    def vzdelanie(self, value):
        if len(value) == 1:
            self._vzdelanie = value
        else:
            tkinter.messagebox.showinfo('info', "Zadané vzdelanie je zlé. Musí obsahovat iba 1 písmeno.")
            ukonc()

    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, value):
        if "@" in value:
            self._mail = value
        else:
            tkinter.messagebox.showinfo('info', "Adresa mailu neobsahuje @.")
            ukonc()

'''Otvorenie súboru.
    Ak je prazdny vytvori sa prazdny zoznam, ak v subore nieco je nacita sa do zoznamu uz existujuce.
    Subor sa uzavrie
    Odchytena vynimka ak sa nebude dat zo suboru nacitat alebo nastane nejaky problem.'''
try:
    file=open("C://Users//Admin//PycharmProjects//ZaverecnyProjekt//data.p", "rb")
    if os.path.getsize("C://Users//Admin//PycharmProjects//ZaverecnyProjekt//data.p") > 0:
        Instruktori = pickle.load(file)
        file.close()
    else:
        Instruktori = []

except IOError:
    tkinter.messagebox.showinfo('Chyba', "Problem s nacitanim zo suboru")

"""Pomocna metoda pre metodu PRIDAJ, aby nedovolila metode pridat ale indikovala chybu v zadanom texte
    Vyuziva sa v PROPERTY"""
def ukonc():
    global chyba
    chyba=True

"""Pridanie nového objektu INSTRUKTOR
    Nacitanie zo vstupu z GUI
    Osetrenie ci ID je jedinecne
    Kontrola chyby ci vstup je korektny"""
def pridaj():
    novy = Instruktor()
    novy.idI=entryidI.get()
    novy.meno=entrymeno.get()
    novy.priezvisko=entrypriezvisko.get()
    novy.vzdelanie=entryvzdelanie.get()
    novy.mail=entrymail.get()
    novy.telefon=entrytelefon.get()
    novy.adresa=entryadresa.get()

    for i in Instruktori:
        if i.idI == entryidI.get():
            ukonc()
            tkinter.messagebox.showinfo('Info', "ID uz existuje, zvolte ine.")
            break

    if chyba != True:
        Instruktori.append(novy)
        vypis()
        entryidI.delete(0, 'end')
        entrymeno.delete(0, 'end')
        entrypriezvisko.delete(0, 'end')
        entryvzdelanie.delete(0, 'end')
        entrymail.delete(0, 'end')
        entrytelefon.delete(0, 'end')
        entryadresa.delete(0, 'end')

"""Vypise vsetky udaje do vystupneho poľa"""
def vypis():
    konzola.delete("1.0", "end")
    riadok=""
    for i in Instruktori:
        riadok=riadok+str(i)+ "\n"
    konzola.insert('end', riadok)

"""Vymaze vsetok text vo vystupnom poli"""
def vymaz_konzolu():
    konzola.delete("1.0", "end")

"""Vymazanie instruktora na zakladne jedinecneho ID
    Konstrola ci bolo zadane ID
    Informacia ak sa vymazanie nepodarilo, pretoze take ID a instruktor neboli najdeny"""
def vymaz_instruktora():
    vymazane = False
    if entryvymazanie.get() == "":
        tkinter.messagebox.showinfo('Info', "Nebolo zadane ziadne ID")
    else:
        for i in Instruktori:
            if entryvymazanie.get() == i.idI:
                Instruktori.remove(i)
                vymazane = True
                vypis()
                entryvymazanie.delete(0, 'end')
        if vymazane == False:
            tkinter.messagebox.showinfo('Info', "Nebol najdeny instruktor so zadanym ID")

"""Vyhladanie objektu/objektov Instruktor na zakladne jednotlivych atributov objektu
    Vypis iba najdenych objektov
    Informacia ak sa nepodarilo nic najst"""
def vyhladaj():
    vybranaMoznost = moznost.get()
    text = entryvyhladanie.get().lower()
    vymaz_konzolu()
    vysledky=""
    if vybranaMoznost == "ID":
        for i in Instruktori:
            if text == i.idI:
                vysledky = vysledky + Instruktor.__str__(i) + "\n"
    elif vybranaMoznost == "Meno":
        for i in Instruktori:
            if (text in i.meno.lower()):
                vysledky = vysledky + Instruktor.__str__(i) + "\n"
    elif vybranaMoznost == "Priezvisko":
        for i in Instruktori:
            if (text in i.priezvisko.lower()):
                vysledky = vysledky + Instruktor.__str__(i) + "\n"
    elif vybranaMoznost == "Vzdelanie":
        for i in Instruktori:
            if text == i.vzdelanie.lower():
                vysledky = vysledky + Instruktor.__str__(i) + "\n"
    elif vybranaMoznost == "Email":
        for i in Instruktori:
            if (text in i.mail.lower()):
                vysledky = vysledky + Instruktor.__str__(i) + "\n"
    elif vybranaMoznost == "Telefon":
        for i in Instruktori:
            if text == i.telefon:
                vysledky = vysledky + Instruktor.__str__(i) + "\n"
    elif vybranaMoznost == "Adresa":
        for i in Instruktori:
            if (text in i.adresa.lower()):
                vysledky = vysledky + Instruktor.__str__(i) + "\n"
    if vysledky == "":
        tkinter.messagebox.showinfo('Info', "Neboli najdene ziadne vysledky")
    else:
        konzola.insert('end', vysledky)
    entryvyhladanie.delete(0,'end')

"""GUI PANEL"""
master = tki.Tk(className="Instruktori")

"""Definovanie vsetkych popisov v GUI"""
tki.Label(master, text="Nový Instruktor").grid(row=0, column=1)
tki.Label(master, text="Id:").grid(row=1,column=0)
tki.Label(master, text="Meno:").grid(row=2,column=0)
tki.Label(master, text="Priezvisko:").grid(row=3,column=0)
tki.Label(master, text="Vzdelanie:").grid(row=4,column=0)
tki.Label(master, text="Mail:").grid(row=5,column=0)
tki.Label(master, text="Telefon:").grid(row=6,column=0)
tki.Label(master, text="Adresa:").grid(row=7,column=0)
tki.Label(master, text="ID").grid(row=3, column=3)

"""Definovanie vsetkych vstupnych poli v GUI"""
entryidI = tki.Entry(master)
entrymeno = tki.Entry(master)
entrypriezvisko = tki.Entry(master)
entryvzdelanie = tki.Entry(master)
entrymail = tki.Entry(master)
entrytelefon = tki.Entry(master)
entryadresa = tki.Entry(master)
entryvymazanie = tki.Entry(master)
entryvyhladanie = tki.Entry(master)

"""Umiestnenie vsetkych vstupnych poli do GUI"""
entryidI.grid(row=1, column=1)
entrymeno.grid(row=2, column=1)
entrypriezvisko.grid(row=3, column=1)
entryvzdelanie.grid(row=4, column=1)
entrymail.grid(row=5, column=1)
entrytelefon.grid(row=6, column=1)
entryadresa.grid(row=7, column=1)
entryvymazanie.grid(row=4, column=3)
entryvyhladanie.grid(row=4, column=2)

"""Definovanie vsetkych Button-ou v GUI, ich funckie a umiestnenie"""
vymazInstruktora = tki.Button(master, text="Vymaž", command = vymaz_instruktora).grid(row=5, column=3)
vymazKonzolu = tki.Button(master, text="Vymaž Konzolu", command = vymaz_konzolu).grid(row=9, column=3)
pridat = tki.Button(master, text="Pridať", command = pridaj).grid(row=9, column=1)
vypisButton = tki.Button(master, text="Výpis", command = vypis).grid(row=9, column=2)
vyhladajButton = tki.Button(master, text="Vyhľadaj", command = vyhladaj).grid(row=5, column=2)

"""Definovanie vystupneho pola"""
konzola = panel.ScrolledText(master, width="150", height="10", wrap="word")
konzola.grid(row=10,column=0, columnspan=10)

"""Tlacidlo v GUI, kde sa vybera moznost, ktory atribut z ponuky"""
moznost = tki.StringVar(master)
moznost.set("ID")
moznosti = tki.OptionMenu(master, moznost, "ID", "Meno", "Priezvisko", "Vzdelanie", "Email", "Telefon", "Adresa")
moznosti.grid(row=3, column= 2)

"""Spustenie GUI"""
master.mainloop()

"""Ak sa GUI uzavrie a ukonci, otvori sa subor a ulozia sa do neho vsetky udaje"""
file=open("C://Users//Admin//PycharmProjects//ZaverecnyProjekt//data.p", "wb")
pickle.dump(Instruktori, file)