import json

def crea_persona(nome, eta, residenza, professione):
    return {
        "nome": nome,
        "eta": eta,
        "residenza": residenza,
        "professione": professione
    }

def aggiungi_persona(elenco_persone, id_persona, persona):
    elenco_persone[id_persona] = persona

def check_risposta(risposta):
    risposta = risposta.strip().upper()
       
    if risposta == "S":
        return True, "Nuovo inserimento", True
    elif risposta == "N":
        return False, "Alla prossima! Vado via.", True
    else:
        return False, "Hai sbagliato risposta! Ritenta!!!", False

def salva_elenco_persone(elenco_persone, nome_file):
    with open(nome_file, 'w') as file:
        json.dump(elenco_persone, file, indent=4)

def carica_elenco_persone(nome_file):
    try:
        with open(nome_file, 'r') as file:
            elenco_persone = json.load(file)
            elenco_persone = converti_id_persona_a_intero(elenco_persone)
    except FileNotFoundError:
        elenco_persone = {}
    return elenco_persone

def converti_id_persona_a_intero(elenco_persone):
    elenco_convertito = {}
    for id_persona, persona in elenco_persone.items():
        elenco_convertito[int(id_persona)] = persona
    return elenco_convertito

def valida_dato(stringa):
    if stringa != "":
        return stringa, "", True
    else:
        return "", "Il campo non può essere vuoto.", False  

def valida_intero(stringa):
    try:
        numero = int(stringa)
        return numero, "", True
    except ValueError:
        return "", "Inserisci un numero valido.", False      

def chiedi_dato(messaggio):
    while True:
        dato = input(messaggio)
        dato, messaggio_errore, valida = valida_dato(dato)
        if valida:
            return dato
        else:
            print(messaggio_errore)

def chiedi_intero(messaggio):
    while True:
        dato = input(messaggio)

        dato, messaggio_errore, valida = valida_dato(dato)
        if not valida:
            print(messaggio_errore)
            continue
        
        numero, messaggio_errore, valida = valida_intero(dato)
        if valida:
            return numero
        else:
            print(messaggio_errore)          

def trova_persona(elenco_persone, nome):

    for persona in elenco_persone.values():
        if persona["nome"].lower() == nome.lower():
            return persona
    return None

def main():
    #elenco_persone = {}
    elenco_persone = carica_elenco_persone("elenco_persone.json")

    if elenco_persone:
        id_persona = max(elenco_persone.keys())
    else:
        id_persona = 0
    
    while True:
        domanda = "Vuoi inserire una nuova persona? (s/n): "
        risposta = input(domanda)

        scelta, messaggio, valida = check_risposta(risposta)

        # se la risposta non è valida, stampo il messaggio di errore e continuo il ciclo
        if not valida:
            print(messaggio)
            continue
        # se la risposta è valida e l'utente ha scelto di non inserire una nuova persona, esco dal ciclo
        elif not scelta:
            trova = input("Vuoi cercare una persona per nome? (s/n): ")
            if trova.strip().upper() == "S":
                nome_cercato = input("Inserisci il nome della persona da cercare: ")
                persona_trovata = trova_persona(elenco_persone, nome_cercato)
                if persona_trovata:
                    print(f"\nInformazioni sulla persona trovata:")
                    for chiave, valore in persona_trovata.items():
                        print(f"{chiave}: {valore}")
                else:
                    print("Persona non trovata.")
                continue
            else:
                print(messaggio)
                break
        
        nome = chiedi_dato("Inserisci il nome: ")
        eta = chiedi_intero("Inserisci l'età: ")
        residenza = chiedi_dato("Inserisci la residenza: ")
        professione = chiedi_dato("Inserisci la professione: ")

        id_persona += 1
        persona = crea_persona(nome, eta, residenza, professione)
        aggiungi_persona(elenco_persone, id_persona, persona)

    salva_elenco_persone(elenco_persone, "elenco_persone.json")
      
    # for id_persona, persona in elenco_persone.items():
    #     print(f"\nInformazioni sulla persona con ID {id_persona}:")
    #     for chiave, valore in persona.items():
    #         print(f"{chiave}: {valore}")



if __name__ == "__main__":
    main()