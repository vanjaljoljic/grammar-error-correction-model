from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM

# Učitavanje prethodno obučenog tokenizatora i modela za sekvencu-na-sekvencu jezikovni model
correction_tokenizer = AutoTokenizer.from_pretrained("model3", use_auth_token=False)
correction_model = AutoModelForSeq2SeqLM.from_pretrained("model3", use_auth_token=False)


def correct(input_sentence, max_candidates=1):
    """
    Ispravlja ulaznu rečenicu koristeći prethodno obučeni model.

    Args:
        input_sentence (str): Ulazna rečenica koja se ispravlja.
        max_candidates (int): Maksimalan broj generisanih ispravaka.

    Returns:
        set: Skup ispravljenih rečenica.
    """
    
    # Dodavanje prefiksa ulaznoj rečenici, kako je potrebno za model
    correction_prefix = "gec: "
    input_sentence = correction_prefix + input_sentence
    # Tokenizacija ulazne rečenice i konverzija u PyTorch tenzore
    input_ids = correction_tokenizer.encode(input_sentence, return_tensors='pt')
    
    # Generisanje ispravki koristeći prethodno obučeni model
    preds = correction_model.generate(
        input_ids,
        do_sample=True, 
        max_length=128, 
        num_beams=7,
        early_stopping=True,
        num_return_sequences=max_candidates)

    # Dekodiranje generisanih ispravki i dodavanje u skup
    ispravljeno = set()
    for pred in preds:  
        ispravljeno.add(correction_tokenizer.decode(pred, skip_special_tokens=True).strip())

    return ispravljeno


def process_file(file_path):
    """
    Obradjuje datoteku s rečenicama i generiše ispravljene verzije.

    Args:
        file_path (str): Putanja do datoteke s rečenicama.

    Returns:
        str: Tekst koji sadrži originalne i ispravljene rečenice.
    """

    # Čitanje rečenica iz ulazne datoteke
    with open(file_path, 'r') as file:
        rečenice = file.readlines()

    rezultat = ""
    for rečenica in rečenice:
        # Ispravka svake rečenice i dobijanje skupa ispravki
        ispravljene_rečenice = correct(rečenica, max_candidates=1)
        # Dodavanje originalnih i ispravljenih rečenica u rezultujući tekst
        rezultat += "[Ulaz] " + rečenica
        for ispravljena_rečenica in ispravljene_rečenice:
            rezultat += "[Ispravka] " + ispravljena_rečenica
        # Dodavanje linije razdvajanja između svakog para originalnih i ispravljenih rečenica
        rezultat += "-" * 100

    return rezultat

