IDENTIFIKACIJA I ISPRAVAK GRAMATIČKIH GREŠAKA U REČENICI
Ovaj program omogućuje ispravku rečenica koristeći prethodno obučeni model za sekvencu-na-sekvencu jezičku obradu. 
Konkretno, koristi se model za ispravku gramatičkih grešaka u tekstu.

Instalacija i Pokretanje
Preporučuje se korišćenje virtualnog okruženja kako bi se izolirale potrebne biblioteke za ovaj projekat.
Instalirajte potrebne biblioteke naredbom: pip install -r requirements.txt.
Preuzmite prethodno obučeni model i tokenizator. Očekuje se da su dostupni u direktoriju "model3".
Pokrenite program naredbom: python correction_program.py.

Korišćenje
Unesite rečenicu u polje za unos teksta koju želite ispraviti.
Pritisnite dugme "Ispravi rečenicu" kako biste videli ispravke na osnovu unesene rečenice.
Rezultat ispravki će biti prikazan ispod polja za unos teksta.

Struktura Koda
correction_program.py: Glavni programski kod koji sadrži funkcije za ispravku rečenica i grafičko korisničko sučelje pomoću biblioteke Tkinter.
requirements.txt: Datoteka sa spiskom svih potrebnih biblioteka i njihovih verzija za ovaj projekat.
model3/: Direktorij koji sadrži prethodno obučeni model i tokenizator za ispravku rečenica.

Napomene
Ovaj program koristi prethodno obučeni model za sekvencu-na-sekvencu jezičku obradu radi ispravke gramatičkih grešaka u tekstu.
Ispravke se generišu na osnovu unete rečenice koristeći model i tokenizator.
Program koristi grafičko korisničko sučelje implementirano pomoću biblioteke Tkinter.

Učitavanje Rečenica iz Datoteke
Program očekuje da će rečenice koje se ispravljaju biti učitane iz datoteke nazvane "input2.txt". 
Ukoliko želite promeniti datoteku ili putanju, prilagodite kod u funkciji process_file u correction_program.py.

Autor
Autor: Vanja Ljoljić