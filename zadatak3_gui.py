import tkinter as tk
import difflib
from VanjaLjoljic_zadatak3 import correct

file_iterator = None
sentences_to_correct = None
original_text = None
corrected_text = None
add_button = None
correct_button = None

def add_sentence():
    """
    Funkcija za dodavanje rečenice iz datoteke u tekstualni prikaz originalnih rečenica.

    Učitava sljedeću rečenicu iz datoteke "input2.txt" i dodaje je u lijevi tekstualni prikaz. 
    Ako su sve rečenice dodane, onemogućuje dugme za dodavanje novih rečenica.

    Ako su sve rečenice već dodane, dodaje obavještenje o završetku.
    """
    global file_iterator
    global sentences_to_correct
    global original_text
    global add_button

    input_sentence = ""
    line = next(file_iterator, None)
    while line:  
        line = line.strip()
        if line:  
            if '.' in line:
                sentences = line.split('.')
                for sentence in sentences:
                    if sentence.strip():  
                        input_sentence += sentence.strip() + " "  
                        original_text.insert(tk.END, "[Original] " + input_sentence.strip() + "\n", "original_tag")
                        sentences_to_correct.append(input_sentence.strip())
                        input_sentence = ""  
            else:
                input_sentence += line + " "  
        line = next(file_iterator, None) 

    if not line:  
        original_text.insert(tk.END, "[Original] " + input_sentence.strip() + "\n", "original_tag")
        sentences_to_correct.append(input_sentence.strip())
        original_text.insert(tk.END, "KRAJ\n", "end_tag")
        add_button.config(state=tk.DISABLED)


def correct_sentences():
    """
    Funkcija za ispravak trenutno prikazane originalne rečenice i prikaz ispravljenih verzija 
    u tekstualnom prikazu desno.

    Uzima trenutnu originalnu rečenicu iz lijevog tekstualnog prikaza, šalje je funkciji
    `correct` za ispravak i prikazuje generisane ispravke u desnom tekstualnom prikazu.
    
    Ako nema više originalnih rečenica, dodaje obavještenje o završetku i onemogućuje dugme za ispravak.

    Napomena: Svaki put kada se pritisne dugme "Ispravi Rečenicu", ispravljaju se samo trenutno prikazane rečenice.
    """
    global sentences_to_correct
    global corrected_text
    global correct_button

    if sentences_to_correct:
        input_sentence = sentences_to_correct.pop(0)
        corrected_sentences = correct(input_sentence, max_candidates=1)

        for corrected_sentence in corrected_sentences:
            corrected_text.insert(tk.END, "[Correction] " + corrected_sentence + "\n", "corrected_tag")
    else:
        corrected_text.insert(tk.END, "KRAJ\n", "end_tag")
        correct_button.config(state=tk.DISABLED)

def check_correction():
    """
    Funkcija za proveru tačnosti ispravke rečenica.

    Uzima trenutnu originalnu rečenicu i ispravljenu rečenicu iz lijevog i desnog tekstualnog prikaza
    i upoređuje njihovu sličnost. Prikazuje rezultat u desnom tekstualnom prikazu.
    """
    global original_text
    global corrected_text

    original_sentence = original_text.get("1.0", "end-1c").split("[Original] ")[-1].strip()
    corrected_sentence = corrected_text.get("1.0", "end-1c").split("[Correction] ")[-1].strip()

    # Izračunavanje sličnosti između originalne i ispravljene rečenice
    similarity = difflib.SequenceMatcher(None, original_sentence, corrected_sentence).ratio()

    # Prikazivanje rezultata u desnom tekstualnom prikazu
    if similarity == 1.0:
        corrected_text.insert(tk.END, "\nIspravljena rečenica je tačna.\n", "correct_tag")
    else:
        corrected_text.insert(tk.END, "\nIspravljena rečenica nije potpuno tačna.\n", "incorrect_tag")



if __name__ == "__main__":
    # Inicijalizacija Tkinter GUI-a
    root = tk.Tk()
    root.title("Sentence Correction App")
    root.geometry("800x500")

    # Text za otvorene rečenice (levo)
    original_text = tk.Text(root, wrap=tk.WORD, width=40, height=20, background="lightyellow")
    original_text.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
    original_text.tag_configure("original_tag", foreground="darkblue")
    original_text.tag_configure("end_tag", foreground="red")

    # Text za ispravljene rečenice (desno)
    corrected_text = tk.Text(root, wrap=tk.WORD, width=40, height=20, background="lightcoral")
    corrected_text.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")
    corrected_text.tag_configure("corrected_tag", foreground="darkgreen")
    corrected_text.tag_configure("end_tag", foreground="red")

    # Dodajemo tagove za prikaz rezultata provere
    corrected_text.tag_configure("correct_tag", foreground="green")
    corrected_text.tag_configure("incorrect_tag", foreground="red")

    # Dugme za dodavanje rečenica
    add_button = tk.Button(root, text="Dodaj Rečenice", command=add_sentence, bg="lightblue")
    add_button.grid(row=0, column=1, pady=10)

    # Dugme za ispravku rečenica
    correct_button = tk.Button(root, text="Ispravi Rečenicu", command=correct_sentences, bg="lightgreen")
    correct_button.grid(row=1, column=1, pady=10)


    # Otvori datoteku za čitanje
    with open("input2.txt", 'r') as file:
        file_iterator = iter(file.readlines())
        sentences_to_correct = []

    root.mainloop()
